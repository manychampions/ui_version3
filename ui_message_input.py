from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon

class Ui_MI_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 692)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)


        self.Camera_label = QtWidgets.QLabel(self.centralwidget)
        self.Camera_label.setGeometry(QtCore.QRect(400, 70, 120, 120))  # 视频的位置及大小
        self.Camera_label.setObjectName("Camera_label")


        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(180, 270, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")

        self.lineEdit_sn0 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sn0.setGeometry(QtCore.QRect(290, 280, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_sn0.setFont(font)
        self.lineEdit_sn0.setObjectName("lineEdit_sn0")

        self.age_label = QtWidgets.QLabel(self.centralwidget)
        self.age_label.setGeometry(QtCore.QRect(180, 320, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.age_label.setFont(font)
        self.age_label.setObjectName("age_label")
        self.lineEdit_sn1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sn1.setGeometry(QtCore.QRect(290, 330, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_sn1.setFont(font)
        self.lineEdit_sn1.setObjectName("lineEdit_sn1")

        self.sex_label = QtWidgets.QLabel(self.centralwidget)
        self.sex_label.setGeometry(QtCore.QRect(180, 370, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")
        self.lineEdit_sn2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sn2.setGeometry(QtCore.QRect(290, 380, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_sn2.setFont(font)
        self.lineEdit_sn2.setObjectName("lineEdit_sn2")

        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(180, 420, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.id_label.setFont(font)
        self.id_label.setObjectName("sex_label")
        self.lineEdit_sn3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sn3.setGeometry(QtCore.QRect(290, 430, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_sn3.setFont(font)
        self.lineEdit_sn3.setObjectName("lineEdit_sn3")

        self.position_label = QtWidgets.QLabel(self.centralwidget)
        self.position_label.setGeometry(QtCore.QRect(180, 470, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.position_label.setFont(font)
        self.position_label.setObjectName("sex_label")
        self.lineEdit_sn4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sn4.setGeometry(QtCore.QRect(290, 480, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_sn4.setFont(font)
        self.lineEdit_sn4.setObjectName("lineEdit_sn4")

        self.camera_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.camera_pushButton.setGeometry(QtCore.QRect(300, 230, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.camera_pushButton.setFont(font)
        self.camera_pushButton.setObjectName("camera_pushButton")

        self.button_Take_Photo = QtWidgets.QPushButton(self.centralwidget)
        self.button_Take_Photo.setGeometry(QtCore.QRect(470, 230, 112, 34))
        self.button_Take_Photo.setObjectName("take_photo")

        # self.camera_pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.camera_pushButton.setGeometry(QtCore.QRect(300, 230, 112, 34))
        # self.camera_pushButton.setObjectName("open_camera")

        self.button_OK = QtWidgets.QPushButton(self.centralwidget)
        self.button_OK.setGeometry(QtCore.QRect(300, 550, 112, 34))
        self.button_OK.setObjectName("button_OK")
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setGeometry(QtCore.QRect(470, 550, 112, 34))
        self.button_cancel.setObjectName("button_cancel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 10, 301, 51))

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 状态栏
        self.statusBar().showMessage('Ready')

        # 工具栏
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.Camera_label.setText(_translate("MainWindow", "Video Area"))
        self.name_label.setText(_translate("MainWindow", "姓名:"))
        self.age_label.setText(_translate("MainWindow", "年龄:"))
        self.sex_label.setText(_translate("MainWindow", "性别:"))
        self.id_label.setText(_translate("MainWindow", "工号:"))
        self.position_label.setText(_translate("MainWindow", "职位:"))
        self.button_OK.setText(_translate("MainWindow", "OK"))
        self.button_cancel.setText(_translate("MainWindow", "Cancel"))
        self.camera_pushButton.setText(_translate("MainWindow", "打开摄像头"))
        self.button_Take_Photo.setText(_translate('MainWindow', '拍照并保存'))
        self.label_3.setText(_translate("MainWindow", "请录入该用户的相关信息"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MI_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())