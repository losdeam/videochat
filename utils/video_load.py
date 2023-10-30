
import utils.function as function 
import ffmpeg
from moviepy.editor import VideoFileClip
from io import BytesIO
import pyaudio

class Video_load:

    def __init__(self,name="w1",video=0):
        # 初始化
        self.name = name
        # 客户端上传视频（未完成）

        if  video  :
            self.inout_ = audio.open(format=pyaudio.paInt16,  # 指定数据类型是int16，也就是一个数据点占2个字节；paInt16=8，paInt32=2，不明其含义，先不管
                        channels=2,  # 声道数，1或2
                        rate=44100,  # 采样率，44100或16000居多
                        frames_per_buffer=1024,  # 每个块包含多少帧，详见下文解释
                        output=True)  # 表示这是一个输出流，要对外播放的
        else :
            # 本地上传视频
            self.video = VideoFileClip(video)  
            # 获取音频时长以确定视频的总时长
            self.video_time = self.video.duration
            audio= self.video.audio
            # 将音频信息暂存为wav文件方便进行读取
            audio.write_audiofile(self.name + '.wav')


        


        

