import socket, videosocket
from video_receive import Video_receive
from video_sent import Video_sent
import sys
import function
import threading
import queue


class Client:
    def __init__(self, ip_addr = "127.0.0.1"):
        # 创建一个socket连接,socket.SOCK_STREAM表示是有那个TCP作为传输协议，socket.AF_INET表示使用IPv4地址
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接至服务器的6000端口中
        self.client_socket.connect((ip_addr, 6000))
        # 将所创建的socket连接通过videosocket进行进一步的封装
        self.vsock = videosocket.videosocket (self.client_socket)
        self.Video_sent = None
        self.audio = None 
    
    # 连接
    def connect(self,video):
        # self.videofeed = VideoFeed("client",1)
        self.Video_sent = Video_sent("client",video)

        n = 0
        # 持续从视频流中获取帧信息
        while True:
            # 通过videofeed来获取本机的视频流数据
            frame=self.Video_sent.get_frame()
            
            audio = self.Video_sent.get_audio()

            # print(type(frame))
            # print(type(audio))
            # print(msg.encode())
            if frame or audio :
                video_thread = threading.Thread(target=self.vsock.vsend(frame))
                video_thread.start()
                audio_thread = threading.Thread(target=self.vsock.vsend(audio))
                audio_thread.start()  
                n=0
            else:
                print("上传数据获取失败")
                n+=1 
                if n == 10 :
                    print("获取失败次数过多，已中断连接")
                    break
                continue 

            # 从服务器接受返回数据，受设备限制，暂不启用
            # frame = self.vsock.vreceive()
            # 将从服务器返回的视频流数据进行播放
            # self.videofeed.set_frame(frame)

            # msg = self.vsock.vreceive()
            # print(msg)

        self.videofeed.colse()


if __name__ == "__main__":
    #
    ip_addr = "192.168.56.1"
    if len(sys.argv) == 2:
        ip_addr = sys.argv[1]

    print ("Connecting to " + ip_addr + "....")
    video = 'D:\\learn\\videochat\\videochat_self\\videochat\\1.mp4'
    client = Client(ip_addr)
    client.connect(video=video)
