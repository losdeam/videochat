import cv2
import base64
import wave 

import utils.function as function 



class Video_sent:

    def __init__(self,load):

        # 以迭代器的形式获取video中的视频数据
        self.video = load.video.iter_frames()
        # 打开soumd.wav文件
        self.wf = wave.open(load.name + '.wav', 'rb')
        # 获取音频长度（以byte为单位）
        self.len = self.wf.getnframes()
        # self.len_frame = 0 
    #图像转base64
    def get_frame(self):
        if self.video:
            try :
                img = next(self.video)
            except:
                return None 
            # 图像预处理
            img = function.transform(img)
            #图像转base64
            img_bytes = cv2.imencode('.png', img)[1].tostring()
            img_str = base64.b64encode(img_bytes).decode('utf-8')
            return img_str

    
    #音频读取
    def get_audio(self,n):
        if n < self.len:
            # 从上传的视频流中获取音频信息
            audio_data = self.wf.readframes(1024) 
            # 获取以发送的字节数，用于结束判断
            n+= len(audio_data)
            return audio_data ,n 
        return None ,n 
    


        

