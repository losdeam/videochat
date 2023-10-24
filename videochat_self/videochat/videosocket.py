import socket
import io
import function 

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

    # 实现接收
    def vreceive(self):
        totrec=0
        metarec=0
        flag = 0 
        msgArray = b''
        flagbyte = b''
        metaArray = []
        
        
        while flag < 5:
            chunk = self.sock.recv(5 - metarec)
            if function.reconnect(chunk):
                return None,None
            flagbyte += chunk
            flag += len(chunk)
        
        while metarec < 10:
            #从嵌套字中接受数据，最大获取量为10 - metarec
            chunk = self.sock.recv(10 - metarec)
            if function.reconnect(chunk):
                return None,None
            metaArray.append(chunk.decode("utf-8"))
            metarec += len(chunk)
        
        
        lengthstr= ''.join(metaArray)
        length=int(lengthstr)
        # print(length)
        while totrec<length :
            chunk = self.sock.recv(length - totrec)
            if function.reconnect(chunk):
                return None,None
            msgArray+=chunk
            totrec += len(chunk)
            # print("已成功接收",totrec,"剩余",length-totrec)
        
        return flagbyte,msgArray
   


        
