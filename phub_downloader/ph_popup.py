from PyQt5 import QtCore, QtGui, QtWidgets

quality_list = [1080 , 720]
class Ui_PopUp(QtWidgets.QDialog):
    def __init__(self, quality_list: list, parent = None):
        super(Ui_PopUp, self).__init__(parent)
        self.setupUi(self)
        self.quality_list = quality_list
        self.col_dict = {
            0 : 2160,
            1 : 1080,
            2 : 720,
            3 : 480,
            4 : 240
        }
        self.choice = None

    def closeEvent(self, event):
        event.ignore()

    def setupUi(self, PopUp):
        self.PopUp = PopUp  # Store the PopUp instance
        PopUp.setObjectName("PopUp")
        PopUp.setWindowModality(QtCore.Qt.ApplicationModal)
        PopUp.resize(500, 258)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        PopUp.setFont(font)
        PopUp.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        ### msg
        self.quality_msg = QtWidgets.QLabel(PopUp)
        self.quality_msg.setGeometry(QtCore.QRect(140, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.quality_msg.setFont(font)
        self.quality_msg.setObjectName("quality_msg")

        self.Quality_list = QtWidgets.QTableWidget(PopUp)       ###table
        self.Quality_list.setGeometry(QtCore.QRect(10, 60, 481, 91))
        self.Quality_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Quality_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Quality_list.setAutoScroll(True)
        self.Quality_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Quality_list.setObjectName("Quality_list")
        self.Quality_list.setColumnCount(5)
        self.Quality_list.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Quality_list.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Quality_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Quality_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Quality_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Quality_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Quality_list.setHorizontalHeaderItem(4, item)
        self.Quality_list.horizontalHeader().setStretchLastSection(True)
        self.Quality_list.verticalHeader().setVisible(False)

        ### my change, add checkbox
        self.Quality_list.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        self.Quality_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Quality_list.setShowGrid(False)
        for col in range(5):
            checkbox = QtWidgets.QRadioButton()
            self.Quality_list.setCellWidget(0, col, checkbox)
            checkbox.toggled.connect(lambda checked, col=col: self.radio_button_toggled(checked, col))      
        ###

        self.confirm_button = QtWidgets.QPushButton(PopUp)      ### button
        self.confirm_button.setGeometry(QtCore.QRect(190, 180, 121, 31))
        self.confirm_button.setObjectName("confirm_button")
        self.confirm_button.clicked.connect(self.confirmed)
        self.retranslateUi(PopUp)
        QtCore.QMetaObject.connectSlotsByName(PopUp)

    def retranslateUi(self, PopUp):
        _translate = QtCore.QCoreApplication.translate
        PopUp.setWindowTitle(_translate("PopUp", "Choose Quality"))
        self.quality_msg.setText(_translate("PopUp", "SELECT QUALITY"))
        item = self.Quality_list.verticalHeaderItem(0)
        item.setText(_translate("PopUp", "Quality"))
        item = self.Quality_list.horizontalHeaderItem(0)
        item.setText(_translate("PopUp", "2160p"))
        item = self.Quality_list.horizontalHeaderItem(1)
        item.setText(_translate("PopUp", "1080p"))
        item = self.Quality_list.horizontalHeaderItem(2)
        item.setText(_translate("PopUp", "720p"))
        item = self.Quality_list.horizontalHeaderItem(3)
        item.setText(_translate("PopUp", "480p"))
        item = self.Quality_list.horizontalHeaderItem(4)
        item.setText(_translate("PopUp", "240p"))
        self.confirm_button.setText(_translate("PopUp", "Confirm"))
    
    def radio_button_toggled(self, checked:bool, col):
        if checked == True:
            self.choice = self.col_dict.get(col)
        

    def confirmed(self):
        if self.choice in self.col_dict.values() and self.choice in self.quality_list:
            self.PopUp.accept()
        else:
            self.show_warning("Your choice is unavailable")
        
        
    def get_return_value(self):
        return self.choice
    
    def show_warning(self, text:str):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Warning")
        msg.setText(text)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopUp = Ui_PopUp(quality_list)
    ui = Ui_PopUp(quality_list)
    ui.setupUi(PopUp)
    PopUp.show()
    sys.exit(app.exec_())
