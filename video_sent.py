import cv2

import base64
import json
import function
import pyaudio
import wave 
from moviepy.editor import VideoFileClip

class Video_sent:

    def __init__(self,name="w1",capture=1):
        print (name)
        # 视频部分初始化
        self.camera_index = 0
        self.name = name
        self.cam = None 
        self.input_stream  = None 
        self.wf = None 
        self.p = pyaudio.PyAudio()
        if capture == 1:
            self.cam = cv2.VideoCapture(self.camera_index)
            self.input_stream = self.p.open(format=pyaudio.paInt16,
                channels=2,
                rate=44100,
                input=True,
                frames_per_buffer=1024)
        else :
            self.cam = cv2.VideoCapture(capture)
            # 音频部分初始化
            video = VideoFileClip(capture)  
            audio= video.audio
            audio.write_audiofile('sound.wav')
            self.wf = wave.open('sound.wav', 'rb')

    #图像转base64
    def get_frame(self):
        ret_val, img = self.cam.read()
        if ret_val :
            # 图像预处理
            img = function.transform(img)
            #图像转base64
            img_bytes = cv2.imencode('.png', img)[1].tostring()
            img_bytes = base64.b64encode(img_bytes)
            
            return img_bytes
        return None
    
    #音频转base64
    def get_audio(self):
        # 存在上传的视频时
        if self.wf:
            # 从上传的视频流中获取音频信息
            audio_data = self.wf.readframes(1024) 

        else:
            # 从麦克风的输入中获取音频信息
            audio_data = self.input_stream.read(1024)
        return audio_data
    


    def colse(self):
        # 如果存在已经开启的视频文件
        self.cam.release()
        if self.input_stream:
            self.input_stream.stop_stream()
            self.input_stream.close()
        self.p.terminate()
        
        

