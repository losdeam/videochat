
import utils.function as function 
import ffmpeg
from moviepy.editor import VideoFileClip
from io import BytesIO


class Video_load:

    def __init__(self,name="w1",video=0,flag = 0 ):
        # 初始化
        self.name = name
        if flag == 0 :
            in_mem_file = BytesIO(video)
            video = ffmpeg.input(in_mem_file)
            audio = video.audio
            print(type(video),type(audio))
            self.out_frame_file = BytesIO()
            self.out_audio_file = BytesIO()
            video.output(self.out_frame_file).run()
            audio.output(self.out_audio_file).run()
            
            self.out_audio_file = self.out_frame_file.seek(0)
            self.out_audio_file = self.out_audio_file.getvalue()
            print(type(self.out_frame_file))
            print(type(self.out_audio_file))

        elif flag ==1 :
            pass # 摄像头
        else :
            self.video = VideoFileClip(video)  
            # 获取音频时长以确定视频的总时长
            self.video_time = self.video.duration
            audio= self.video.audio
            # 将音频信息暂存为wav文件方便进行读取
            audio.write_audiofile(self.name + '.wav')


        


        

