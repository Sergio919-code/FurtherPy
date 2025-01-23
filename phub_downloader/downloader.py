import bs4
import requests
import os
import re
import json
from tqdm import tqdm
import threading

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

url = 'https://www.pornhub.com/view_video.php?viewkey=676451e4a3c07'

def connect(url : str , headers : dict):
    global session
    index = 1
    try:
        while index <= 5:
            try:
                session = requests.session()
                resp = session.get(url, headers=headers)
            except requests.exceptions.ConnectionError as e:
                print(f'Error: {e}, Tried times: {index}')
            
            index += 1
    except:
        return -1
    return resp

def parse(resp):
    soup = bs4.BeautifulSoup(resp.text , "html.parser")
    try:
        name = soup.find('head').find('title').text
        name = name.replace(" - Pornhub.com" , "")
        ###
        half_main = (soup.find("div" , attrs={"class" : "clearfix" , "id" : "main-container"}).find_all("script" , attrs={"type" : "text/javascript"}))[1].text    
        pattern = re.compile(r"var\s.*?\s=\s(\{.*?\});")
        main = re.findall(pattern, half_main)[0]
        print("Everything good in parse() func:)")
    except Exception as e:
        return -1 , -1

    return json.loads(main) , name

###     mediaDefinitions    defaultQuality
def choose_quality(dict : dict):
    while True:
        try:
            quality_list = dict["defaultQuality"]
            for resol in quality_list:
                print(resol)
            quality = int(input("Choose quality: "))
            if quality not in quality_list:
                raise Exception
            break
        except:
            continue
    return quality

def get_master(dict: dict , choice : int , headers: dict):
    global session 
    mediaDef = dict["mediaDefinitions"]
    try:
        for medias in mediaDef:
            if medias["quality"] == str(choice):
                master_url = medias["videoUrl"]
                base = (master_url.split("/master.m3u8"))[0]
    except Exception as e:
        return -1, -1
    ###
    try:
        index = 1
        while index <= 5:
            try:
                resp = session.get(master_url , headers=headers)
                print("Everything good in get_master() func:)")
                break
            except requests.exceptions.ConnectionError:
                print("Connection Error")
                index += 1
    except:
        return -1 , -1

    return resp.text , base

def get_playlist(txt: str , base:str , headers: dict):
    global session
    parts = txt.split("\n")
    for part in parts:
        if "m3u8" in part:
            url_parts = part
    url = base +'/' + url_parts
    ###
    try:
        resp = session.get(url , headers=headers)
        resp.encoding="utf-8"
        print("Everything good in get_playlist() func:)")
    except requests.exceptions.ConnectionError:
        print("Connection Error")
        return -1
    
    return resp.text    ###playlist

def save_video(txt:str , base: str , headers: dict , path: str , name: str):
    global session
    not_playlist = txt.split("\n")
    playlist = [(base + "/" + url) for url in not_playlist if "seg" in url]

    def get_ts(url, headers):
        global session
        trials = 1
        while trials <= 5:
            try:
                ts = session.get(url, headers=headers, stream=True)
                if ts.status_code == 200:
                    return ts
            except requests.exceptions.ConnectionError:
                trials += 1
                print("Connection error, retrying...")
        return None

    Invalid_char = ["<" , ">" , ":" , "\"" , "/" , "\\" , "|" , "?" , "*"]
    for char in name:
        if char in Invalid_char:
            name = name.replace(char , "_")
    path += fr"\{name}.mp4"
        
    open(path , "wb").close()
    
    with open(path, "ab") as video:
        for url in tqdm(playlist, desc=name):
            ts = get_ts(url, headers)
            if ts:
                for chunk in ts.iter_content(chunk_size=4096):
                    if chunk:
                        video.write(chunk)
            else:
                print(f"Failed to download segment: {url}")
                return
    print("Video saved successfully.")

def Input_validation():
    ###url input
    while True:
        try:
            url = input("Enter the correct format URL: ")
            if "viewkey" not in url:
                raise Exception
            break
        except:
            print("Invalid URL.")
            continue
    ### path input
    while True:
        try:
            path = input("Enter the path you want to save: ")
            path_ = path + r"\test.mp4"
            open(path_, "wb").close()
            os.remove(path_)
            break
        except:
            print("Invalid path.")
            continue
    return url , path




def downloader():
    while True:
        url, path = Input_validation()
        first_resp = connect(url, headers)
        if first_resp == -1:
            print("Failed to connect.")
            continue
        
        main_dict, name = parse(first_resp)
        if main_dict == -1 or name == -1:
            print("Failed to parse the response.")
            continue
        
        quality = choose_quality(main_dict)
        
        intermediate, base = get_master(main_dict, quality, headers)
        if intermediate == -1 or base == -1:
            print("Failed to get master URL.")
            continue
        
        playlist = get_playlist(intermediate, base, headers)
        if playlist == -1:
            print("Failed to get playlist.")
            continue
        
        save_video(playlist, base, headers, path, name)
        break


if __name__ == "__main__":
    try:
        downloader()
    except Exception as e:
        print(f'Error: {e}')
    input("All finished --press Enter to exit")







    
        



    

    











    


