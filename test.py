import cv2 
import os 
import pyaudio
import function
from moviepy.editor import VideoFileClip
import wave

p = pyaudio.PyAudio()
video = VideoFileClip('D:\\learn\\videochat\\videochat_self\\videochat\\1.mp4')  

audio= video.audio
audio.write_audiofile('sound.wav')
wf = wave.open('sound.wav', 'rb')
output_stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
print(type(output_stream))
while True:

    data = wf.readframes(1024) 

    output_stream.write(data)


cv2.destroyAllWindows()


p.terminate()