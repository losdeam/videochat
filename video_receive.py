import cv2
import function
import pyaudio

class   Video_receive:
    def __init__(self,name="w1",):
        print (name)
        self.name = name
        self.p = pyaudio.PyAudio()
        self.output_stream = self.p.open(format=pyaudio.paInt16,
            channels=2,
            rate=44100,
            output=True,
            frames_per_buffer=1024)


    #展示所收到的视频文件
    def set_frame(self, frame_bytes):
        cv_image = function.cvRead(frame_bytes)
        cv2.imshow(self.name, cv_image)
        cv2.waitKey(1)

    #播放所收到的音频文件
    def set_audio(self,audio_bytes):
        self.output_stream.write(audio_bytes)

    def colse(self):
        if cv2.getWindowProperty(self.name, cv2.WND_PROP_VISIBLE) > 0:
        # 关闭窗口
            cv2.destroyWindow(self.name)
        # 如果存在视频流，关闭它
        if self.output_stream:
            self.output_stream.stop_stream()
            self.output_stream.close()

        self.p.terminate()
        
        