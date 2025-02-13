

from PyQt5 import QtCore, QtGui, QtWidgets


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
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget) ### progress bar
        self.progressBar.setGeometry(QtCore.QRect(400, 310, 381, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        ### msg
        self.Progress_msg = QtWidgets.QLabel(self.centralwidget)
        self.Progress_msg.setGeometry(QtCore.QRect(20, 170, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(26)
        self.Progress_msg.setFont(font)
        self.Progress_msg.setObjectName("Progress_msg")

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

        ### msg
        self.status_msg = QtWidgets.QLabel(self.centralwidget)
        self.status_msg.setGeometry(QtCore.QRect(20, 220, 141, 41))
        self.status_msg.setObjectName("status_msg")


        self.status_info = QtWidgets.QLineEdit(self.centralwidget)      ### line edit status
        self.status_info.setGeometry(QtCore.QRect(170, 230, 611, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_info.setFont(font)
        self.status_info.setReadOnly(True)
        self.status_info.setObjectName("status_info")

        ### msg
        self.finisher = QtWidgets.QLabel(self.centralwidget)
        self.finisher.setGeometry(QtCore.QRect(20, 380, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.finisher.setFont(font)
        self.finisher.setObjectName("finisher")
        
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
        self.url_input.setPlaceholderText(_translate("MainWindow", "https://www.pornhub.com/view_video.php?viewkey="))
        self.url_submit.setText(_translate("MainWindow", "Submit"))
        self.path_msg.setText(_translate("MainWindow", "Enter the path to save ->"))
        self.path_input.setPlaceholderText(_translate("MainWindow", "/path/to/download/folder/or/other/folder"))
        self.path_submit.setText(_translate("MainWindow", "Submit"))
        self.Progress_msg.setText(_translate("MainWindow", "Progress:)"))
        self.name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">name</p></body></html>"))
        self.status_msg.setText(_translate("MainWindow", "Current status:"))
        self.status_info.setText(_translate("MainWindow", "good"))
        self.finisher.setText(_translate("MainWindow", "Finished!!!"))
        self.menuoption.setTitle(_translate("MainWindow", "option"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.action_new_download.setText(_translate("MainWindow", "new download"))
        self.action_new_download.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.actionfix_save_dir.setText(_translate("MainWindow", "fix save dir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
