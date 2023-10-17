import socket, videosocket
from io import StringIO
from videofeed import VideoFeed
import sys
import os 

class Client:
    def __init__(self, ip_addr = "127.0.0.1"):
        # 创建一个socket连接,socket.SOCK_STREAM表示是有那个TCP作为传输协议，socket.AF_INET表示使用IPv4地址
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接至服务器的6000端口中
        self.client_socket.connect((ip_addr, 6000))
        # 将所创建的socket连接通过videosocket进行进一步的封装
        self.vsock = videosocket.videosocket (self.client_socket)
        self.videofeed = None
        self.data = StringIO()

    # 连接
    def connect(self):
        self.videofeed = VideoFeed("client",1)
        # self.videofeed = VideoFeed("client",'D:\\learn\\videochat\\videochat_self\\videochat\\1.mp4')
        frame=self.videofeed.get_frame()
        # 持续从视频流中获取帧信息
        while True:
            # 通过videofeed来获取本机的视频流数据
            if frame :
                self.vsock.vsend(frame) 
                print(type(frame))
            else:
                print("frame获取失败")
                continue 
            # 
            

            # 从服务器接受返回数据，受设备限制，暂不启用
            # frame = self.vsock.vreceive()
            # 将从服务器返回的视频流数据进行播放
            # self.videofeed.set_frame(frame)

            # msg = self.vsock.vreceive()
            # print(msg)

if __name__ == "__main__":
    #
    ip_addr = "127.0.0.1"
    if len(sys.argv) == 2:
        ip_addr = sys.argv[1]

    print ("Connecting to " + ip_addr + "....")
    client = Client(ip_addr)
    client.connect()
