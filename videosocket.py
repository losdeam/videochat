import socket
import io

class videosocket:
    '''A special type of socket to handle the sending and receiveing of fixed
       size frame strings over ususal sockets
       Size of a packet or whatever is assumed to be less than 100MB
    '''

    def __init__(self , sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock= sock
    
    # 实现连接
    def connect(self,host,port):
        self.sock.connect((host,port))

    # 实现输出
    def  vsend(self, framestring):
        '''
        发送framestring中的视频流，通过metasent来发送视频流当前帧的总长度，以便以接收端进行确认。通过totalsent来发送当前帧的数据。
        '''
        totalsent = 0
        metasent = 0
        length =len(framestring)
        # zfill 在字符串前补0 ，以满足需要
        lengthstr=str(length).zfill(8)
        # print(lengthstr)
        while metasent < 8 :
            # sent 为成功发送的数量
            sent = self.sock.send(lengthstr[metasent:].encode())
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            # 
            metasent += sent
        
        # print(framestring[totalsent:])
        while totalsent < length :
            sent = self.sock.send(framestring[totalsent:])
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            totalsent += sent
    # 实现接收
    def vreceive(self):
        totrec=0
        metarec=0
        msgArray = b''
        metaArray = []
        n = 0 
        count = 10
        while metarec < 8:
            #从嵌套字中接受数据，最大获取量为8 - metarec
            chunk = self.sock.recv(8 - metarec)
            #当chunk == b''，即无接收值时表示接收失败
            if chunk == b'':
                n  += 1 
                print("数据接受失败,失败次数为",n )
                if n == count :
                    return None
                continue 
            if n != 0 :
                n =0 
                print("重连成功")

            
            metaArray.append(chunk.decode("utf-8"))
            metarec += len(chunk)

        # print(metaArray)
        lengthstr= ''.join(metaArray)
        length=int(lengthstr)

        while totrec<length :
            chunk = self.sock.recv(length - totrec)
            if chunk == b'':
                raise RuntimeError("Socket connection broken")
            msgArray+=chunk
            totrec += len(chunk)
        return msgArray
   


        
