from downloader import *
from ph_popup import Ui_PopUp  
from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys , threading

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

url = ""
path = ""

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 586)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ### msg
        self.Welcome = QtWidgets.QLabel(self.centralwidget)
        self.Welcome.setGeometry(QtCore.QRect(20, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(26)
        self.Welcome.setFont(font)
        self.Welcome.setObjectName("Welcome")

        ### msg
        self.url_msg = QtWidgets.QLabel(self.centralwidget)
        self.url_msg.setGeometry(QtCore.QRect(20, 80, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.url_msg.setFont(font)
        self.url_msg.setObjectName("url_msg")

        self.url_input = QtWidgets.QLineEdit(self.centralwidget)  ### line edit
        self.url_input.setGeometry(QtCore.QRect(260, 79, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setUnderline(True)
        self.url_input.setFont(font)
        self.url_input.setClearButtonEnabled(True)
        self.url_input.setObjectName("url_input")

        self.url_submit = QtWidgets.QPushButton(self.centralwidget) ### push button
        self.url_submit.setGeometry(QtCore.QRect(720, 80, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.url_submit.setFont(font)
        self.url_submit.setObjectName("url_submit")
        self.url_submit.clicked.connect(self.handle_url_submit)




        ### msg
        self.path_msg = QtWidgets.QLabel(self.centralwidget)
        self.path_msg.setGeometry(QtCore.QRect(20, 120, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.path_msg.setFont(font)
        self.path_msg.setObjectName("path_msg")

        self.path_input = QtWidgets.QLineEdit(self.centralwidget)   ### line edit
        self.path_input.setGeometry(QtCore.QRect(260, 120, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.path_input.setFont(font)
        self.path_input.setClearButtonEnabled(True)
        self.path_input.setObjectName("path_input")

        self.path_submit = QtWidgets.QPushButton(self.centralwidget)    #push button
        self.path_submit.setGeometry(QtCore.QRect(720, 120, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.path_submit.setFont(font)
        self.path_submit.setObjectName("path_submit")
        self.path_submit.clicked.connect(self.handle_path_input)
        
        ### start button
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(720, 160, 75,23))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.handle_start)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget) ### progress bar
        self.progressBar.setGeometry(QtCore.QRect(400, 310, 381, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide() ### HIDE

        ### msg
        self.Progress_msg = QtWidgets.QLabel(self.centralwidget)
        self.Progress_msg.setGeometry(QtCore.QRect(20, 170, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(26)
        self.Progress_msg.setFont(font)
        self.Progress_msg.setObjectName("Progress_msg")
        self.Progress_msg.hide() ### HIDE progress

        self.name = QtWidgets.QTextEdit(self.centralwidget)     ### text edit
        self.name.setGeometry(QtCore.QRect(20, 290, 371, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.name.setFont(font)
        self.name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.name.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.name.setReadOnly(True)
        self.name.setObjectName("name")
        self.name.setStyleSheet("background-color: transparent; color: black;") ### HIDE bg
        self.name.hide() #HIDE

        ### msg
        self.status_msg = QtWidgets.QLabel(self.centralwidget)
        self.status_msg.setGeometry(QtCore.QRect(20, 220, 141, 41))
        self.status_msg.setObjectName("status_msg")
        self.status_msg.hide() ###HIDE
        


        self.status_info = QtWidgets.QLineEdit(self.centralwidget)      ### line edit status
        self.status_info.setGeometry(QtCore.QRect(170, 230, 611, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_info.setFont(font)
        self.status_info.setReadOnly(True)
        self.status_info.setObjectName("status_info")
        self.status_info.hide()     #HIDE
        self.status_info.setStyleSheet("background-color: transparent; color: black;")

        ### msg
        self.finisher = QtWidgets.QLabel(self.centralwidget)
        self.finisher.setGeometry(QtCore.QRect(20, 380, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.finisher.setFont(font)
        self.finisher.setObjectName("finisher")
        self.finisher.hide() #HIDE

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuoption = QtWidgets.QMenu(self.menubar)
        self.menuoption.setObjectName("menuoption")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_new_download = QtWidgets.QAction(MainWindow)
        self.action_new_download.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        self.action_new_download.setObjectName("action_new_download")
        self.actionfix_save_dir = QtWidgets.QAction(MainWindow)
        self.actionfix_save_dir.setObjectName("actionfix_save_dir")
        self.menuoption.addAction(self.action_new_download)
        self.menuSetting.addAction(self.actionfix_save_dir)
        self.menubar.addAction(self.menuoption.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Downloader"))
        self.Welcome.setText(_translate("MainWindow", "Welcome!!!"))
        self.url_msg.setText(_translate("MainWindow", "Enter the url that has \"viewkey\" in it ->"))
        self.url_input.setStatusTip(_translate("MainWindow", "enter url"))
        self.url_input.setPlaceholderText(_translate("MainWindow", "https://www.something.com/view_video.php?viewkey=")) ### need to replace back
        self.url_submit.setText(_translate("MainWindow", "Submit"))
        self.path_msg.setText(_translate("MainWindow", "Enter the path to save ->"))
        self.path_input.setPlaceholderText(_translate("MainWindow", "/path/to/download/folder/or/other/folder"))
        self.path_submit.setText(_translate("MainWindow", "Submit"))
        self.Progress_msg.setText(_translate("MainWindow", "Progress:)"))
        self.name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.status_msg.setText(_translate("MainWindow", "Current status:"))
        self.status_info.setText(_translate("MainWindow", "good"))
        self.finisher.setText(_translate("MainWindow", "Finished!!!"))
        self.menuoption.setTitle(_translate("MainWindow", "option"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.action_new_download.setText(_translate("MainWindow", "new download"))
        self.action_new_download.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.actionfix_save_dir.setText(_translate("MainWindow", "fix save dir"))
        self.start_button.setText(_translate("MainWindow", "Start"))

    def handle_url_submit(self):
        global url
        input_ = self.url_input.text()
        if "viewkey" and "http" not in input_:
            url = ""
            self.url_input.setText("Invalid input, please enter again")
        else:
            url = input_
            self.url_input.setText("valid url")  

    def handle_path_input(self):
        global path
        input_ = self.path_input.text()
        try:
            path_ = input_ + r"\test.mp4"
            open(path_ , "wb").close()
            os.remove(path_)
            self.path_input.setText("Valid path")
            path = input_
            print(path)
        except:
            self.path_input.setText("Invalid path")
            path = ""

    def handle_start(self):
        global url, headers
        if url == "" or path == "":
            return
        self.Worker = ph_sys()

        self.Progress_msg.show()
        self.status_msg.show()
        self.status_info.show()
        self.name.show()
        self.progressBar.show()

        self.thread = threading.Thread(target=self.Worker.connect ,args=(url , headers)) 
        self.Worker.connect_finish.connect(lambda: threading.Thread(target=self.Worker.parse , args=(self.Worker.resp,)).start())
        self.Worker.connect_fail.connect(lambda: self.status_info.setText("Connection failed"))

        def func_in_func():

            print("execution to inner func")
            self.status_info.setText(f"HTTP {self.Worker.status_code} {'OK' if self.Worker.status_code == 200 else "CONNECTION ERROR"}")
            self.name.setText(self.Worker.name)

            quality_list = self.Worker.get_quality(self.Worker.main)

            PopUp = Ui_PopUp(quality_list)
            pop = Ui_PopUp(quality_list)
            pop.setupUi(PopUp)

            if PopUp.exec_() == QtWidgets.QDialog.Accepted:
                return_value = pop.get_return_value() 
                print(str(return_value) + "get quality success")
            self.Worker.user_choice = return_value

            QtCore.QTimer.singleShot(0 , intermediate)

        def intermediate():
            threading.Thread(target=self.starter).start()
            self.Worker.total_length.connect(lambda value: self.progressBar.setMaximum(value + 1))
            self.Worker.update_progress.connect(lambda i: self.increase_progress(i))
            self.Worker.all_finish.connect(self.when_finished)
            self.Worker.update_playlist.connect(lambda: self.status_info.setText("Get playlist success"))
            self.Worker.get_master_fail.connect(lambda string: self.status_info.setText(string))
            self.Worker.get_playlist_fail.connect(lambda string: self.status_info.setText(string))

        self.Worker.parse_finish.connect(func_in_func)        
        self.thread.start() ### starter


    def when_finished(self):
        self.progressBar.setValue(self.progressBar.maximum())
        self.finisher.show()
        
        
    def increase_progress(self , max:int):
        current = self.progressBar.value()
        if current < max:
            self.progressBar.setValue(current + 1)

    def starter(self):
        global headers, path
        self.Worker.get_master(self.Worker.main, self.Worker.user_choice, headers)
        self.Worker.get_playlist(self.Worker.master , self.Worker.base , headers)
        print(f"choice: {self.Worker.user_choice}")
        self.Worker.save_video(self.Worker.playlist , self.Worker.base , headers , path, self.Worker.name)





class ph_sys(QtCore.QObject):
    connect_finish = QtCore.pyqtSignal()
    connect_fail = QtCore.pyqtSignal()
    parse_finish = QtCore.pyqtSignal()
    update_progress = QtCore.pyqtSignal(int)
    all_finish = QtCore.pyqtSignal()
    total_length = QtCore.pyqtSignal(int)
    update_playlist = QtCore.pyqtSignal()
    get_master_fail = QtCore.pyqtSignal(str)
    get_playlist_fail = QtCore.pyqtSignal(str)



    def __init__(self):
        super().__init__()
        self.user_choice = None

    def __str__(self):
        return "ph_sys"

    def connect(self, url:str, headers:dict):
        global session
        index = 1
        try:
            while index <= 10:
                try:
                    session = requests.session()
                    session.headers.update(headers)
                    resp = session.get(url, headers=headers)
                    if resp.status_code == 200:
                        break
                except requests.exceptions.ConnectionError as e:
                    print(f'Error: {e}, Tried times: {index}')
                
                index += 1
        except:
            self.connect_fail.emit()
            return
        self.resp , self.status_code= resp.text , resp.status_code
        self.connect_finish.emit()

    def parse(self, dict:dict):
        self.main , self.name = parse(dict)
        self.parse_finish.emit()

    def get_quality(self,main:dict):
        medialist = main.get("mediaDefinitions")
        r_list = []
        for dict in medialist:
            r_list.append(dict.get("quality"))
        r_list.remove([])
        
        return [int(value) for value in r_list] #list 
    
    def get_master(self, main:dict, choice:int , headers:dict ):
        global session 
        mediaDef = main["mediaDefinitions"]
        try:
            for medias in mediaDef:
                if medias["quality"] == str(choice):
                    master_url = medias["videoUrl"]
                    base = (master_url.split("/master.m3u8"))[0]
        except Exception as e:
            print(f"Upper part Error: {e}")
            return 
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
        except Exception as e:
            print(f"get_master: {e}")
            self.get_master_fail.emit(f"Error: {e}")
            return 
        self.master , self.base = resp.text, base


    def get_playlist(self , txt:str , base:str , headers):
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
        except requests.exceptions.ConnectionError as e:
            print("Connection Error")
            self.get_playlist_fail.emit(f"Error: {e}")
            return 
        self.playlist = resp.text
        self.update_playlist.emit()


    def save_video(self, txt:str, base:str, headers:dict, path:str, name:str):
            global session
            not_playlist = txt.split("\n")
            playlist = [(base + "/" + url) for url in not_playlist if "seg" in url]
            self.total_length.emit(len(playlist))

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
                for i , url in enumerate(playlist):
                    ts = get_ts(url, headers)
                    if ts:
                        for chunk in ts.iter_content(chunk_size=4096):
                            if chunk:
                                video.write(chunk)
                        self.update_progress.emit(i)
                    else:
                        print(f"Failed to download segment: {url}")
                        return
            self.all_finish.emit()
            print("Video saved successfully.")


if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # Enable high-DPI scaling
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)    # Scale images properly
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  

    sys.exit(app.exec_())







