


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopUp(object):
    def setupUi(self, PopUp):
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


        self.confirm_button = QtWidgets.QPushButton(PopUp)      ### button
        self.confirm_button.setGeometry(QtCore.QRect(190, 180, 121, 31))
        self.confirm_button.setObjectName("confirm_button")

        self.retranslateUi(PopUp)
        QtCore.QMetaObject.connectSlotsByName(PopUp)

    def retranslateUi(self, PopUp):
        _translate = QtCore.QCoreApplication.translate
        PopUp.setWindowTitle(_translate("PopUp", "Choose Quality"))
        self.quality_msg.setText(_translate("PopUp", "SELECT QUALITY"))
        item = self.Quality_list.verticalHeaderItem(0)
        item.setText(_translate("PopUp", "Quality"))
        item = self.Quality_list.horizontalHeaderItem(0)
        item.setText(_translate("PopUp", "4k"))
        item = self.Quality_list.horizontalHeaderItem(1)
        item.setText(_translate("PopUp", "1080p"))
        item = self.Quality_list.horizontalHeaderItem(2)
        item.setText(_translate("PopUp", "720p"))
        item = self.Quality_list.horizontalHeaderItem(3)
        item.setText(_translate("PopUp", "360p"))
        item = self.Quality_list.horizontalHeaderItem(4)
        item.setText(_translate("PopUp", "240p"))
        self.confirm_button.setText(_translate("PopUp", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopUp = QtWidgets.QDialog()
    ui = Ui_PopUp()
    ui.setupUi(PopUp)
    PopUp.show()
    sys.exit(app.exec_())
