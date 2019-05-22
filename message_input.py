
import os
import sys
from Open_Camera import CameraFrame
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui_message_input import Ui_MI_MainWindow
from PyQt5 import  QtGui,  QtWidgets
import cv2

class Sub_Mainwindow(QMainWindow, Ui_MI_MainWindow):
    global card_num
    def __init__(self):
        super(Sub_Mainwindow, self).__init__()
        self.setupUi(self)
        self.sn_message = ''
        self.staff_names = []
        self.Camera = CameraFrame()
        # self.cap = cv2.VideoCapture(0)
        self.button_OK.clicked.connect(self.begin_get)
        self.button_cancel.clicked.connect(self.cancel)
        # self.button_Open_Camera.clicked.connect(self.OpenCamera)
        # self.button_Take_Photo.clicked.connect(self.Take_Photo)

    def scan_sn(self, sn0, sn1, sn2, sn3, sn4):
        if sn0 != "" and sn1 != "" and sn2 != "" and sn3 != "" and sn4 != "":
            sn = (str(sn0) + '\t' + str(sn1) + '\t' + str(sn2) + '\t' + str(sn3) + '\t' + str(sn4))
            self.sn_message += sn

            with open("./staff_information.txt", "r") as fr:
                staffs_messages = fr.readlines()
                for staff_messages in staffs_messages:
                    staff_name = staff_messages.strip().split('\t')[0].split('.')[0]
                    if staff_name not in self.staff_names:
                        self.staff_names.append(staff_name)
            fr.close()

            if sn0 not in self.staff_names:
                with open("./staff_information.txt", "a+") as fw:
                    fw.writelines(self.sn_message + '\n')
                    QMessageBox.information(self, '提示信息', '保存成功')
                    self.lineEdit_sn0.clear()
                    self.lineEdit_sn1.clear()
                    self.lineEdit_sn2.clear()
                    self.lineEdit_sn3.clear()
                    self.lineEdit_sn4.clear()
                fw.close()
            else:
                QMessageBox.information(self, '提示信息', '重复')
                self.lineEdit_sn0.clear()
                self.lineEdit_sn1.clear()
                self.lineEdit_sn2.clear()
                self.lineEdit_sn3.clear()
                self.lineEdit_sn4.clear()
        else:
            QMessageBox.information(self,  '提示信息', '请完整输入相关信息')

    def keyPressEvent(self, event):
        sn0 = self.lineEdit_sn0.text()
        sn1 = self.lineEdit_sn1.text()
        sn2 = self.lineEdit_sn2.text()
        sn3 = self.lineEdit_sn3.text()
        sn4 = self.lineEdit_sn4.text()
        if str(event.key()) == "16777220":
            self.scan_sn(sn0, sn1, sn2, sn3, sn4)

    def begin_get(self):
        sn0 = self.lineEdit_sn0.text()
        sn1 = self.lineEdit_sn1.text()
        sn2 = self.lineEdit_sn2.text()
        sn3 = self.lineEdit_sn3.text()
        sn4 = self.lineEdit_sn4.text()
        self.scan_sn(sn0, sn1, sn2, sn3, sn4)

    def cancel(self):
        self.lineEdit_sn0.clear()
        self.lineEdit_sn1.clear()
        self.lineEdit_sn2.clear()
        self.lineEdit_sn3.clear()
        self.lineEdit_sn4.clear()

    # def Take_Photo(self):
    #     ret, image = self.Camera.CAP(self.cap)
    #     if ret !=None:
    #         cv2.imwrite('./zjh.jpg', image)

    def OpenCamera(self):
        if not self.Camera.isRunning():
            self.Camera.start()
            self.camera_pushButton.setText('关闭摄像头')
        else:
            self.Camera.Stop_Video()
            self.camera_pushButton.setText('打开摄像头')
            # self.Camer_label.setPixmap(QPixmap.fromImage())  #设置图片还原

    def Fresh_Camera(self, show_pic):
        self.Camera_label.setScaledContents(True) #图片自适应大小
        self.Camera_label.setPixmap(QPixmap.fromImage(show_pic))



    def Un_Open(self):
        QtWidgets.QMessageBox.warning(self, '警告',  '打开摄像头失败')

    @pyqtSlot()
    def on_camera_pushButton_clicked(self):
        self.OpenCamera()
        self.Camera.CameraFram.connect(self.Fresh_Camera)
        self.Camera.OpenVideoFlage.connect(self.Un_Open)


if __name__ == '__main__':
    # if os.path.exists("sn.txt"):
    #     os.remove("sn.txt")
    app = QApplication(sys.argv)
    mainWindow = Sub_Mainwindow()
    mainWindow.show()
    sys.exit(app.exec_())