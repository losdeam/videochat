import socket, videosocket
from videofeed import VideoFeed

class Server:
    # 
    def __init__(self):
        # 创建一个socket连接,socket.SOCK_STREAM表示是有那个TCP作为传输协议，socket.AF_INET表示使用IPv4地址
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定服务器地址与端口号
        self.server_socket.bind(("127.0.0.1", 6000))
        # socket中等待队列的最大数量
        self.server_socket.listen(5)
        # 创建名为server的视频流
        self.videofeed = VideoFeed("server")
        

    def start(self):
        print(1)
        while 1:
            print ("TCPServer Waiting for client on port 6000")
            client_socket, address = self.server_socket.accept()
            print ("I got a connection from ", address)
            vsock = videosocket.videosocket(client_socket)
            n = 0 
            while True:
                # print(1)
                frame=vsock.vreceive()
                # print(2)
                if frame :
                    print("成功接受到数据,类型为", type(frame))
                    self.videofeed.set_frame(frame)
                else:
                    print("客户端",address,"断开连接" )
                    break 

                # 获取视频数据，
                # frame=self.videofeed.get_frame()
                # 将视频数据方式发送给对应端口
                # vsock.vsend(frame)
                # vsock.msgsent("服务器成功收到数据")

if __name__ == "__main__":
    server = Server()
    server.start()
