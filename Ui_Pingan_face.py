# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\0-比赛\Pingan_face\Pingan_face.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 550)#主界面尺寸
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Camer_label = QtWidgets.QLabel(self.centralWidget)
        self.Camer_label.setGeometry(QtCore.QRect(60, 100, 300, 330))#视频的位置及大小
        self.Camer_label.setObjectName("Camer_label")

        self.video_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.video_pushButton.setGeometry(QtCore.QRect(20, 35, 100, 31))#x,y轴位置,长宽
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.video_pushButton.setFont(font)
        self.video_pushButton.setObjectName("video_pushButton")

        self.camera_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.camera_pushButton.setGeometry(QtCore.QRect(170, 35, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.camera_pushButton.setFont(font)
        self.camera_pushButton.setObjectName("camera_pushButton")
        self.info_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.info_pushButton.setGeometry(QtCore.QRect(320, 35, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.info_pushButton.setFont(font)
        self.info_pushButton.setObjectName("info_pushButton")
        self.name_label = QtWidgets.QLabel(self.centralWidget)
        self.name_label.setGeometry(QtCore.QRect(420, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")

        self.sex_label = QtWidgets.QLabel(self.centralWidget)
        self.sex_label.setGeometry(QtCore.QRect(420, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")

        self.age_label = QtWidgets.QLabel(self.centralWidget)
        self.age_label.setGeometry(QtCore.QRect(420, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.age_label.setFont(font)
        self.age_label.setObjectName("age_label")

        self.id_label = QtWidgets.QLabel(self.centralWidget)
        self.id_label.setGeometry(QtCore.QRect(420, 290, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")

        self.position_label = QtWidgets.QLabel(self.centralWidget)
        self.position_label.setGeometry(QtCore.QRect(420, 340, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.position_label.setFont(font)
        self.position_label.setObjectName("position_label")

        self.emotion_label = QtWidgets.QLabel(self.centralWidget)
        self.emotion_label.setGeometry(QtCore.QRect(420, 390, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.emotion_label.setFont(font)
        self.emotion_label.setObjectName("emotion_label")

        self.staff_name = QtWidgets.QLabel(self.centralWidget)
        self.staff_name.setGeometry(QtCore.QRect(500, 140, 120, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.staff_name.setFont(font)
        self.staff_name.setObjectName("staff_name")

        self.staff_sex = QtWidgets.QLabel(self.centralWidget)
        self.staff_sex.setGeometry(QtCore.QRect(500, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.staff_sex.setFont(font)
        self.staff_sex.setObjectName("staff_sex")

        self.staff_age = QtWidgets.QLabel(self.centralWidget)
        self.staff_age.setGeometry(QtCore.QRect(500, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.staff_age.setFont(font)
        self.staff_age.setObjectName("staff_age")

        self.staff_id = QtWidgets.QLabel(self.centralWidget)
        self.staff_id.setGeometry(QtCore.QRect(500, 290, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.staff_id.setFont(font)
        self.staff_id.setObjectName("staff_id")

        self.staff_position = QtWidgets.QLabel(self.centralWidget)
        self.staff_position.setGeometry(QtCore.QRect(500, 340, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.staff_position.setFont(font)
        self.staff_position.setObjectName("staff_position")

        self.staff_emotion = QtWidgets.QLabel(self.centralWidget)
        self.staff_emotion.setGeometry(QtCore.QRect(500, 390, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.staff_emotion.setFont(font)
        self.staff_emotion.setObjectName("staff_emotion")

        self.recognition_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.recognition_pushButton.setGeometry(QtCore.QRect(470, 35, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Jenson Pro Lt Disp")
        font.setPointSize(11)
        self.recognition_pushButton.setFont(font)
        self.recognition_pushButton.setObjectName("recognition_pushButton")

        MainWindow.setCentralWidget(self.centralWidget)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition By Team Villaaaa"))

        self.Camer_label.setText(_translate("MainWindow", "Video Area"))
        self.video_pushButton.setText(_translate("MainWindow", "打开视频"))
        self.camera_pushButton.setText(_translate("MainWindow", "打开摄像头"))
        self.info_pushButton.setText(_translate("MainWindow", "信息采集"))
        self.name_label.setText(_translate("MainWindow", "姓名:"))
        self.sex_label.setText(_translate("MainWindow", "性别:"))
        self.age_label.setText(_translate("MainWindow", "年龄:"))
        self.id_label.setText(_translate("MainWindow", "工号:"))
        self.position_label.setText(_translate("MainWindow", "职位:"))
        self.emotion_label.setText(_translate("MainWindow", "表情:"))
        # self.staff_name.setText(_translate("MainWindow", "黄宇星"))
        # self.staff_sex.setText(_translate("MainWindow", "male"))
        # self.staff_age.setText(_translate("MainWindow", "26"))
        # self.staff_id.setText(_translate("MainWindow", "10086"))
        # self.staff_position.setText(_translate("MainWindow", "老总"))

        self.recognition_pushButton.setText(_translate("MainWindow", "人脸识别"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())