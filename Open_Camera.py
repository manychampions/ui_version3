from Ui_Pingan_face import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import cv2
import dlib
import numpy as np
import face_recognition
import os
from scipy.spatial import distance as dist
import time

class CameraThread(QThread, Ui_MainWindow):
    CameraFram = pyqtSignal(QImage)
    trigger_name = pyqtSignal(str)
    trigger_sex = pyqtSignal(str)
    trigger_age = pyqtSignal(str)
    trigger_id = pyqtSignal(str)
    trigger_position = pyqtSignal(str)
    trigger_emotion = pyqtSignal(str)
    OpenVideoFlage = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()

    def eye_aspect_ratio(self, eye):
        # compute the euclidean distances between the two sets of
        # vertical eye landmarks (x, y)-coordinates
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])

        # compute the euclidean distance between the horizontal
        # eye landmark (x, y)-coordinates
        C = dist.euclidean(eye[0], eye[3])

        # compute the eye aspect ratio
        ear = (A + B) / (2.0 * C)

        # return the eye aspect ratio
        return ear

    def run(self):

        def face_emotion(face_landmarks, faces_locations):
            top, right, bottom, left = faces_locations[0]
            face_landmarks = face_landmarks[0]
            face_width = right - left  # 脸宽
            face_height = bottom - top  # 脸高
            #__import__('pudb').set_trace()
            mouth_width = abs(face_landmarks['top_lip'][6][0] - face_landmarks['top_lip'][0][0]) / face_width
            mouth_height = abs(face_landmarks['bottom_lip'][6][1] - face_landmarks['top_lip'][6][1]) / face_height

            # 通过两个眉毛上的10个特征点，分析挑眉程度和皱眉程度
            line_brow_x = []
            line_brow_y = []
            brow_sum = 0  # 高度之和
            frown_sum = 0  # 两边眉毛距离之和
            for l_e, r_e in zip(face_landmarks['left_eyebrow'], face_landmarks['right_eyebrow']):
                brow_sum += (l_e[1] - top) + (r_e[1] - top)
                frown_sum += r_e[0] - l_e[0]
                line_brow_x.append(l_e[0])
                line_brow_y.append(l_e[1])

            # self.brow_k, self.brow_d = self.fit_slr(line_brow_x, line_brow_y)  # 计算眉毛的倾斜程度
            tempx = np.array(line_brow_x)
            tempy = np.array(line_brow_y)
            z1 = np.polyfit(tempx, tempy, 1)  # 拟合成一次直线
            brow_k = -round(z1[0], 3)  # 拟合出曲线的斜率和实际眉毛的倾斜方向是相反的

            brow_hight = (brow_sum / 10) / face_width  # 眉毛高度占比
            brow_width = (frown_sum / 5) / face_width  # 眉毛距离占比

            # 眼睛睁开程度
            eye_sum = abs(face_landmarks['right_eyebrow'][4][1] - face_landmarks['right_eyebrow'][1][1]) + abs(
                face_landmarks['right_eyebrow'][3][1] - face_landmarks['right_eyebrow'][2][1]) + abs(
                face_landmarks['left_eyebrow'][4][1] - face_landmarks['left_eyebrow'][1][1]) + abs(
                face_landmarks['left_eyebrow'][3][1] - face_landmarks['left_eyebrow'][2][1])
            eye_hight = (eye_sum / 4) / face_width
            # 分情况讨论
            # 张嘴，可能是开心或者惊讶
            if round(mouth_height >= 0.03):
                if eye_hight >= 0.056:
                    face_emotion = 'amazing'
                else:
                    face_emotion = 'happy'
            # 没有张嘴，可能是正常和生气
            else:
                if brow_k <= -0.3:
                    face_emotion = 'angry'
                else:
                    face_emotion = 'nature'
            return face_emotion

        know_faces_path = 'know_face_lib'  # 已知图片库文件夹
        staff_information = 'staff_information.txt'  # 员工信息数据库

        self.Run_Camera = 1
        self.cap = cv2.VideoCapture(0) # 0是摄像头位置
        
        #预定义人脸信息
        known_face_encodings = []
        know_face_names = []
        know_staff_information = []
        COUNT = 0
        EYE_AR_THRESH = 0.28
        EYE_AR_CONSEC_FRAMES = 1
        COUNTER = 0
        TOTAL = 0

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
            while self.Run_Camera:
                ret, self.img_read = self.cap.read()
                cv2.waitKey(1)  # 延时1s
                if ret != None:
                    # 考虑把图像缩小0.25来检测识别
                    h, w = self.img_read.shape[:2]
                    input_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2RGB)
                    # gray_img = cv2.cvtColor(self.img_read, cv2.COLOR_BGR2GRAY)

                    faces_location = face_recognition.face_locations(input_img)
                    face_encodings = face_recognition.face_encodings(input_img)
                    face_landmarks = face_recognition.face_landmarks(input_img, faces_location)
                    face_names = []

                    for face_encoding in face_encodings:
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        name = 'unknown'

                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

                        best_match_inxd = np.argmin(face_distances)

                        if matches[best_match_inxd]:
                            name = know_face_names[best_match_inxd]

                        face_names.append(name)
                    # 人脸情绪分类
                    if len(face_names) == 1:
                        emotion = face_emotion(face_landmarks, faces_location)

                    # if len(face_landmarks)==1:
                    #     # 眨眼检测
                    #     leftEye = np.array(face_landmarks[0]['left_eye'])
                    #     rightEye = np.array(face_landmarks[0]['right_eye'])
                    #     leftEAR = self.eye_aspect_ratio(leftEye)
                    #     rightEAR = self.eye_aspect_ratio(rightEye)
                    #     ear = (leftEAR + rightEAR) / 2.0
                    #     # compute the convex hull for the left and right eye, then
                    #     # visualize each of the eyes
                    #     leftEyeHull = cv2.convexHull(leftEye)
                    #     rightEyeHull = cv2.convexHull(rightEye)
                    #     cv2.drawContours(input_img, [leftEyeHull], -1, (0, 255, 0), 1)
                    #     cv2.drawContours(input_img, [rightEyeHull], -1, (0, 255, 0), 1)
                    #
                    #     # check to see if the eye aspect ratio is below the blink
                    #     # threshold, and if so, increment the blink frame counter
                    #     if ear < EYE_AR_THRESH:
                    #         COUNTER += 1
                    #
                    #     # otherwise, the eye aspect ratio is not below the blink
                    #     # threshold
                    #     else:
                    #         # if the eyes were closed for a sufficient number of
                    #         # then increment the total number of blinks
                    #         if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    #             TOTAL += 1
                    #
                    #         # reset the eye frame counter
                    #         COUNTER = 0
                    #
                    #     # draw the total number of blinks on the frame along with
                    #     # the computed eye aspect ratio for the frame
                    #     cv2.putText(input_img, "Blinks: {}".format(TOTAL), (10, 30),
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    #     cv2.putText(input_img, "EAR: {:.2f}".format(ear), (300, 30),
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                    # 绘框
                    for name, d in zip(face_names, faces_location):
                        x1, y1, x2, y2 = d[0], d[1], d[2], d[3]
                        input_img = cv2.rectangle(input_img, (y2, x1), (y1, x2), (255, 0, 0), 2)
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(input_img, name, (y2 - 6, x2 + 6), font, 1.0, (255, 255, 255), 1)

                    show_pic = QImage(input_img.data, w, h, QImage.Format_RGB888)

                    if self.Run_Camera:
                        self.CameraFram.emit(show_pic)
                        if len(face_names) == 1:
                            if name == 'unknown':
                                self.trigger_name.emit(name)
                                self.trigger_sex.emit('')
                                self.trigger_age.emit('')
                                self.trigger_id.emit('')
                                self.trigger_position.emit('')
                                self.trigger_emotion.emit(emotion)
                            else:
                                sex, age, id_, position = si_dict[name]
                                self.trigger_name.emit(name)
                                self.trigger_sex.emit(sex)
                                self.trigger_age.emit(age)
                                self.trigger_id.emit(id_)
                                self.trigger_position.emit(position)
                                self.trigger_emotion.emit(emotion)
                        else:
                            self.trigger_name.emit('')
                            self.trigger_sex.emit('')
                            self.trigger_age.emit('')
                            self.trigger_id.emit('')
                            self.trigger_position.emit('')
                            self.trigger_emotion.emit('')
                    else:
                        break
                    # time.sleep(0.005)

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
            
