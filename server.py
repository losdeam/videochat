import socket, videosocket
from video_receive import Video_receive
from video_sent import Video_sent
import threading
import cv2 
import function

class Server:
    # 
    def __init__(self,ip,port):
        # 创建一个socket连接,socket.SOCK_STREAM表示是有那个TCP作为传输协议，socket.AF_INET表示使用IPv4地址
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定服务器地址与端口号
        self.server_socket.bind((ip, port))
        # socket中等待队列的最大数量
        self.server_socket.listen(5)
        # 创建名为server的视频流
        self.Video_receive = Video_receive("server")
        while True:
            print ("TCPServer Waiting for client on port 6000")
            # 持续等待客户端请求
            client_socket, client_address = self.server_socket.accept()
            # 显示客户端的连接信息
            print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
            # 多线程
            client_thread = threading.Thread(target=self.start(client_socket,client_address), args=(self.server_socket,))
            client_thread.start()

    def start(self,client_socket,address):
            #获取客户端所上传的视频流信息
            vsock = videosocket.videosocket(client_socket)
            
            while vsock:
                try :
                    video_thread = threading.Thread(target=self.receive_video(vsock))
                    audio_thread = threading.Thread(target=self.receive_audio(vsock))
                    audio_thread.start()
                    video_thread.start()
                    
                except:
                    print("客户端断开连接")
                    self.Video_receive.colse()
                    break
                # print("成功接受到数据,类型为", type(frame))


                # 获取视频数据，
                # frame=self.videofeed.get_frame()
                # 将视频数据方式发送给对应端口
                # vsock.vsend(frame)
                # vsock.msgsent("服务器成功收到数据")
    def receive_audio(self,vsock):
        audio = vsock.vreceive()
        self.Video_receive.set_audio(audio)

    def receive_video(self,vsock):
        frame = vsock.vreceive()
        self.Video_receive.set_frame(frame)
if __name__ == "__main__":
    ip = "192.168.56.1"
    port = 6000
    server = Server(ip=ip,port=port )

