# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
点击，打开摄像头（多线程 ），或者显示失败
点击，开始识别：能识别，显示信息，不能识别，信息采集
点击，信息采集，添加新人信息（数据库或者动态数组）
"""
from PyQt5 import  QtGui,  QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_Pingan_face import Ui_MainWindow
from Open_Camera import CameraThread
from Read_Video import VideoThread
#from Add_person import Add_Person


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Video = VideoThread()
        self.Camera = CameraThread()
        #self.Add = Add_Person()   
        
    def OpenCamera(self):
        if not self.Camera.isRunning():
            self.Camera.start()
            self.camera_pushButton.setText('关闭摄像头')
        else:
            self.Camera.Stop_Video()
            self.camera_pushButton.setText('打开摄像头')
            #self.Camer_label.setPixmap(QPixmap.fromImage())  #设置图片还原

    def OpenVideo(self):
        if not self.Video.isRunning():
            self.Video.start()
            self.video_pushButton.setText('关闭视频')
        else:
            self.Video.Stop_Video()
            self.video_pushButton.setText('打开视频')
            #self.Camer_label.setPixmap(QPixmap.fromImage())  #设置图片还原

    def Fresh_Video(self, show_pic):
        self.Camer_label.setScaledContents(True) #图片自适应大小
        self.Camer_label.setPixmap(QPixmap.fromImage(show_pic))

    def Fresh_Name(self, name):
        self.staff_name.setText(name)

    def Fresh_Sex(self, sex):
        self.staff_sex.setText(sex)

    def Fresh_Age(self, age):
        self.staff_age.setText(age)

    def Fresh_Id(self, id):
        self.staff_id.setText(id)

    def Fresh_Position(self, position):
        self.staff_position.setText(position)

    def Fresh_Emotion(self, emotion):
        self.staff_emotion.setText(emotion)

    def Fresh_Camera(self, show_pic):
        self.Camer_label.setScaledContents(True) #图片自适应大小
        self.Camer_label.setPixmap(QPixmap.fromImage(show_pic))
    
    def Un_Open(self):
        QtWidgets.QMessageBox.warning(self, '警告',  '打开摄像头失败')

    @pyqtSlot()
    def on_video_pushButton_clicked(self):
        self.OpenVideo()
        self.Video.VideoFram.connect(self.Fresh_Video)#VideoFram是每一帧视频图像
        #self.Video.OpenVideoFlage.connect(self.Un_Open)
        self.Video.trigger_name.connect(self.Fresh_Name)
        self.Video.trigger_sex.connect(self.Fresh_Sex)
        self.Video.trigger_age.connect(self.Fresh_Age)
        self.Video.trigger_id.connect(self.Fresh_Id)
        self.Video.trigger_position.connect(self.Fresh_Position)
        self.Video.trigger_emotion.connect(self.Fresh_Emotion)

    @pyqtSlot()
    def on_camera_pushButton_clicked(self):
        self.OpenCamera()
        self.Camera.CameraFram.connect(self.Fresh_Camera)
        self.Camera.trigger_name.connect(self.Fresh_Name)
        self.Camera.trigger_sex.connect(self.Fresh_Sex)
        self.Camera.trigger_age.connect(self.Fresh_Age)
        self.Camera.trigger_id.connect(self.Fresh_Id)
        self.Camera.trigger_position.connect(self.Fresh_Position)
        self.Camera.trigger_emotion.connect(self.Fresh_Emotion)
        self.Camera.OpenVideoFlage.connect(self.Un_Open)

        
    @pyqtSlot()
    def on_recognition_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_info_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
