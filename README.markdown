Video Chat
=================

A simple video chat client implementation using sockets. 
It's created and maintained by [Anil Shanbhag](http://github.com/anilshanbhag) & [Ashwin Paranjpee](http://www.cse.iitb.ac.in/~ashwinp), IIT Bombay.


Hack Night
-----------
This application was developed in Hack Night , a fun coding weekend . This project is only for educational purposes .


Installation
----------
On one session  
> $ python server.py

Another session
> $ python client.py [optional ip]

For example, if you are doing locally
> $ python client.py

If the server is on a remote machine
> $ python client.py {server-ip}

Working
----------
Sockets and OpenCV are two main things in this app. 

Client connects to server socket . PyOpenCV library is used to retrieve frames from webcam feed , they are compressed to jpg to save on the amount of data to be sent across the socket and transmitted . At the other end the image is decompressed and shown. The data being well above 4096 is sent split and reassembled at the other end .

PS : This implementation is two way 


Copyright and license
---------------------

Copyright 2016 Anil Shanbhag

Distributed under GPL v2

2023.10.17 fork
需要：基于当前项目进行远程的视频通话
由于设备过少无法进行双端测试，今日目标为通过让服务器获取到client所上传的视频流信息


2023.10.18 
任务：
1. 实现视频流的中断，即客户端与服务器的独立。
2. 实现多客户端的同时传输
3. 对传输速度进行优化，力求达到实时播放
4. 实现音频的传输，
   
已完成内容：
1. 实现视频流的中断，即客户端与服务器的独立。
2. 通过对于画面的压缩，提高了传输的效率

![Alt text](结构文件_1.png)
          第一版结构

2023.10.20
经过测试，发现json在socket传输解码的过程中会导致混乱，使得解码错误。转而使用多线程进行操作。在后续实现web端时可以考虑使用json。