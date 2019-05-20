from Ui_Pingan_face import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import cv2
import dlib
import numpy as np
import face_recognition
import os

class CameraThread(QThread, Ui_MainWindow):
    CameraFram = pyqtSignal(QImage)
    trigger_name = pyqtSignal(str)
    trigger_sex = pyqtSignal(str)
    trigger_age = pyqtSignal(str)
    trigger_id = pyqtSignal(str)
    trigger_position = pyqtSignal(str)
    OpenVideoFlage = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()

    def run(self):
        know_faces_path = 'know_face_lib'  # 已知图片库文件夹
        staff_information = 'staff_information.txt'  # 员工信息数据库

        self.Run_Camera = 1
        self.cap = cv2.VideoCapture(0) # 0是摄像头位置
        
        #预定义人脸信息
        known_face_encodings = []
        know_face_names = []
        know_staff_information = []

        with open(staff_information, 'r') as si:
            si_lines = si.readlines()
        si_dict = {}
        for si_line in si_lines:
            name = si_line.split('\t')[0].split('.')[0]
            si_dict[name] = si_line.strip().split('\t')[1:]

        for face in os.listdir(know_faces_path):
            com_one_face_path = os.path.join(know_faces_path, face)
            face_name = face.split('.')[0]
            face_img = face_recognition.load_image_file(com_one_face_path)
            face_encoding = face_recognition.face_encodings(face_img)[0]
            known_face_encodings.append(face_encoding)
            know_face_names.append(face_name)
            know_staff_information.append(si_dict[face_name])

        ret, self.img_read = self.cap.read()
        if ret:
            h, w = self.img_read.shape[:2]#视频尺寸
        
        if (not self.cap.isOpened()):
            self.cap.open()
            self.cap.set(3, 500)
            self.cap.set(4, 600)
            
        elif (self.cap.isOpened()):
            timeF = 2  # 视频帧计数间隔频率
            c = 0
            while self.Run_Camera:
                ret,  self.img_read = self.cap.read()
                cv2.waitKey(1) #延时1s
                if ret !=None:
                    if (c % timeF == 0):
                        #处理帧
                        input_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2RGB)

                        faces_location = face_recognition.face_locations(input_img)
                        face_encodings = face_recognition.face_encodings(input_img, faces_location)
                        face_names =[]

                        for face_encoding in face_encodings:
                            matches = face_recognition.compare_faces(known_face_encodings,  face_encoding)
                            name = 'unknown'

                            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

                            best_match_inxd = np.argmin(face_distances)

                            if matches[best_match_inxd]:
                                name = know_face_names[best_match_inxd]

                            face_names.append(name)

                        #绘框
                        for name, d in zip(face_names, faces_location):
                            x1, y1, x2, y2= d[0], d[1], d[2], d[3]
                            input_img = cv2.rectangle(input_img, (y2, x1), (y1, x2), (255, 0, 0), 2)
                            font = cv2.FONT_HERSHEY_DUPLEX
                            cv2.putText(input_img, name, (y2- 6, x2 + 6), font, 1.0, (255, 255, 255), 1)

                        show_pic = QImage(input_img.data,  w, h, QImage.Format_RGB888)
                        c += 1

                        if self.Run_Camera:
                            self.CameraFram.emit(show_pic)
                            if len(face_names) == 1:
                                if name == 'unknown':
                                    self.trigger_name.emit(name)
                                    self.trigger_sex.emit('')
                                    self.trigger_age.emit('')
                                    self.trigger_id.emit('')
                                    self.trigger_position.emit('')
                                else:
                                    sex, age, id_, position = si_dict[name]
                                    self.trigger_name.emit(name)
                                    self.trigger_sex.emit(sex)
                                    self.trigger_age.emit(age)
                                    self.trigger_id.emit(id_)
                                    self.trigger_position.emit(position)
                            else:
                                self.trigger_name.emit('')
                                self.trigger_sex.emit('')
                                self.trigger_age.emit('')
                                self.trigger_id.emit('')
                                self.trigger_position.emit('')
                        else:
                            break
                        #time.sleep(0.005)

                    else:
                        # 非处理帧
                        self.OpenVideoFlage.emit(self.cap.isOpened())
                        input_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2RGB)
                        # 绘框
                        for name, d in zip(face_names, faces_locations):
                            x1, y1, x2, y2 = d[0], d[1], d[2], d[3]
                            input_img = cv2.rectangle(input_img, (y2, x1), (y1, x2), (255, 0, 0), 2)
                            font = cv2.FONT_HERSHEY_DUPLEX
                            cv2.putText(input_img, name, (y2 - 6, x2 + 6), font, 1.0, (255, 255, 255), 1)
                        show_pic = QImage(input_img, w, h, QImage.Format_RGB888)
                        c += 1
                        COUNT = COUNT + 1
                        time.sleep(0.02)  # 控制播放速度
                        if self.Run_Camera:
                            self.VideoFram.emit(show_pic)
                        else:
                            break
                else:
                    print('摄像头已打开')
            self.cap.release()
            self.quit()
        else:
            self.OpenVideoFlage.emit(self.cap.isOpened())
    
    def Stop_Video(self):
        self.Run_Camera = 0
        
            
        
    
#    def identify(self):
#        
#        
#    def save_img(self):
            
