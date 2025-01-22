import requests
import bs4,re,json
import os
from tqdm import tqdm
from pathlib import Path
from lxml import etree
import shutil




def get_info(url , headers):
    global session
    try:
        session = requests.Session()
        res = session.get(url , headers=headers)
    except Exception as e:
        print('Connection Error')
        print(e)
        exit()
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text , 'html.parser')
    main = soup.select_one('div#main-container.clearfix')
    sub_name = etree.HTML(res.text).xpath('/html/head/title/text()')
    sub_name_ = sub_name[0].replace(' - Pornhub.com' , '')
    pattern = re.compile(r"'video_uploader_name'\s*:\s*'(?P<author>.+?)'")
    match = pattern.search(res.text)
    if match:
        author = match.group('author')
    else:
        author = 'Unknown'
    name = author +'-' + sub_name_ + '.mp4'
    script_tag = main.find_all('script' , {'type' : 'text/javascript'})
    script_tag = script_tag[1]
    script_content = script_tag.string.strip()
    match = re.search(r"=\s*({.*});", script_content)
    if match:
            json_string = match.group(1)  # Get the matched JSON portion
            try:
                # Parse the extracted JSON string
                parsed_data = json.loads(json_string)
                #print("Parsed JSON:", parsed_data)
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)
    else:
            print("No valid JSON found in the script content.")
    return parsed_data , name


def get_seg_urls(parsed_data , headers):
    global session
    video_data = parsed_data['mediaDefinitions']
    quality_list = []
    quality_list.extend([element['quality'] for element in video_data[:-1]])
    print(quality_list)
    while True:
        input_ = input('Enter the quality you want: ')   
        if input_ in quality_list:
            break
        else:
            print('Enter valid option')
    index = quality_list.index(input_)
    m3u8_master_link = parsed_data['mediaDefinitions'][index]['videoUrl']
    base_link = m3u8_master_link.split('master')[0]
    print(base_link)
    res = session.get(m3u8_master_link ,headers=headers)
    res.raise_for_status()
    m3u8_info = res.text  
    index_link = m3u8_info.split('\n')
    res = session.get(base_link + index_link[2], headers=headers)
    m3u8_content = res.text
    ### for debug
    with open('m3u8_content.txt', 'w', encoding='utf-8') as f:
        f.write(m3u8_content)

    return m3u8_content, base_link

def save_video_segs(m3u8_content, base_link, headers, seg_dir):
    global session
    seg_dir = Path(seg_dir)  # Ensure seg_dir is a Path object
    lines = m3u8_content.split('\n')
    seg_links = [base_link + line for line in lines if '.ts' in line]
    print(f'Found {len(seg_links)} segments')
    for index, seg_link in enumerate(tqdm(seg_links)):
        res = session.get(seg_link, headers=headers)
        res.raise_for_status()
        with open(seg_dir.joinpath(f'seg-{index+1}.ts'), 'wb') as f:
            for chunk in res.iter_content(chunk_size=2048):
                if chunk:
                    f.write(chunk)
    print('All segments downloaded')
    return seg_dir

def comb_seg(seg_dir, comb_dir, name):
    # Combine all the .ts files in the seg_dir into a single video file
    # and save it in the comb_dir
    seg_dir = Path(seg_dir)  # Ensure seg_dir is a Path object
    comb_dir = Path(comb_dir)  # Ensure comb_dir is a Path object
    num_files = len(list(seg_dir.glob('*.ts')))
    with open(comb_dir.joinpath(name), 'wb') as video:
        for index in range(1, num_files + 1):
            file_path = seg_dir.joinpath(f'seg-{index}.ts')
            with open(file_path, 'rb') as source:
                while chunk := source.read(2048):
                    video.write(chunk)
    print('Video combined successfully')
    return comb_dir

def main():
    url = input('Enter the url of the video: ')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    parsed_data , name= get_info(url , headers)
    seg_dir = input('Enter the directory to save the segments: ')
    seg_dir = os.path.abspath(seg_dir)
    seg_dir = os.path.join(seg_dir , 'tschunks')
    seg_dir = os.path.abspath(seg_dir)
    if os.path.exists(seg_dir):
        try:
            shutil.rmtree(seg_dir)
        except PermissionError:
            print('wrong path')
    os.makedirs(seg_dir , exist_ok=True)
    m3u8_content , base_link = get_seg_urls(parsed_data , headers)
    seg_dir = save_video_segs(m3u8_content , base_link , headers , seg_dir)
    session.close()
    comb_dir = input('Enter the directory to save the combined video: ')
    comb_dir = os.path.abspath(comb_dir)
    os.makedirs(comb_dir , exist_ok=True)
    comb_dir = comb_seg(seg_dir , comb_dir , name)
    print(f'Video saved successfully at {comb_seg}')


if __name__ == '__main__':
    input("PRess Enter")
    main()
    input("Press Enter")
