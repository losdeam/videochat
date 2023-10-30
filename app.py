from flask import Flask, render_template,request,make_response, redirect
from flask_socketio import SocketIO,join_room, leave_room
# from utils.function import call
from utils.video_load import Video_load
from utils.video_sent import Video_sent
import time 
import json 

connected_users = {}
user_to_sid = {}

app=Flask(__name__)
socketio = SocketIO(app)

####### 连接部分 #########
@socketio.on('connect') 
# 当连接完毕
def connect():
    global connected
    connected = True 

# 当连接断开
@socketio.on('disconnect') 
def disconnect ():
    global connected
    connected = False


####### 聊天室部分
# 加入房间
@socketio.on('join')
def on_join(data):
    response = make_response(redirect('/'))
    response.set_cookie('username', data["name"])
    join_room(data['room'])
    socketio.emit("join",{"roomId":data['room'],"content":"加入房间"},room=request.sid)  


# 离开房间
@socketio.on('leaveRoom')
def on_leave(data):
    room = data['room']
    leave_room(room)
    print(request.cookies.get('username')+"离开了房间")

# 发送信息
@socketio.on('chat_send')
def chat_send(data):
    if data["flag"]:
        data["message"] = request.cookies.get('username')  + data["message"]
    socketio.emit("chat_recv_"+str(data['room_id']),data)  

@app.route('/room/<room_id>') 
def get_room_page(room_id):
  # 渲染房间页面
  return render_template('room.html', room_id=room_id)

########## 视频播放部分
# 当连接完毕,收到test信号时
@socketio.on('test') 
def test():
    print('已成功连接')
    global Video_loads
    video_name = "1.mp4"
    Video_loads = Video_load("client",video_name)
    datas = {
        "msg" : f"video {video_name} load  finish", 
        "time": Video_loads.video_time
    }
    datas = json.dumps(datas)
    socketio.emit("read",datas)  
    print("视频读取完毕")

    print("开始发送")
    video = Video_sent(Video_loads)
    #持续从视频流中获取帧信息
    n = 0
    # 当连接时，持续发送
    while connected:
        # print("传输进行中",n)
        # 通过Video_sent来获取本机的视频流数据
        frame=video.get_frame()
        audio,n= video.get_audio(n)
        # print(type(frame),type(audio))
        if not (frame or   audio):
            break
        datas =  {
            'time' : time.time(),
            'frame' : frame,
            'audio' : str(audio)
        }
        datas = json.dumps(datas)
        socketio.emit('play',datas)  
    print("发送完毕")
    socketio.emit('sent_finish')  

# 用户上传视频
@socketio.on('user_video_cam')
def  user_video_cam():
    pass 
# 用户本地视频
@socketio.on('user_video_vid')
def  user_video_cam():
    pass 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test_():
    return render_template('test.html')
# 接口
@app.route('/emit', methods=['POST']) 
def emit_event():
    print('已成功连接')
    global Video_loads
    video_name = "1.mp4"
    Video_loads = Video_load("client",video_name)
    datas = {
        "msg" : f"video {video_name} load  finish", 
        "time": Video_loads.video_time
    }
    datas = json.dumps(datas)
    socketio.emit("read",datas)  
    print("视频读取完毕")

    print("开始发送")
    video = Video_sent(Video_loads)
    #持续从视频流中获取帧信息
    n = 0
    # 当连接时，持续发送
    while connected:
        # print("传输进行中",n)
        # 通过Video_sent来获取本机的视频流数据
        frame=video.get_frame()
        audio,n= video.get_audio(n)
        # print(type(frame),type(audio))
        if not (frame or   audio):
            break
        datas =  {
            'time' : time.time(),
            'frame' : frame,
            'audio' : str(audio)
        }
        datas = json.dumps(datas)
        socketio.emit('play',datas)  
    print("发送完毕")
    socketio.emit('sent_finish')  
@app.route('/upload', methods=['POST'])
def upload_video():
    video = request.files['video']
    in_bytes = video.read()
    print(video.filename)
    Video_loads = Video_load("client",in_bytes)
    socketio.emit("read",f"video {video.filename} load  finish")  
    print("视频读取完毕")
    # 保存视频文件
    return {'status': 'success'}

# 加入房间（接受房间的信号）
@app.route('/join_post', methods=['POST'])
def join_post(data):
    room = data['room']
    join_room(room)
    socketio.emit("join",{"roomId":str(room),"content":"加入房间"})  


# 
# 开启直播（接受房间的信号）
@app.route('/broadcast', methods=['POST'])
def broadcast(data):
    flag = 1 
    Video_loads = Video_load("client",0)
    print("开始发送")
    video = Video_sent(Video_loads)
    #持续从视频流中获取帧信息
    n = 0
    # 当连接时，持续发送
    while connected:
        # print("传输进行中",n)
        # 通过Video_sent来获取本机的视频流数据
        frame=video.get_frame()
        audio,n= video.get_audio(n)
        # print(type(frame),type(audio))
        if not (frame or   audio):
            break
        datas =  {
            'time' : time.time(),
            'frame' : frame,
            'audio' : str(audio)
        }
        datas = json.dumps(datas)
        socketio.emit('play',datas)  
    print("发送完毕")
    socketio.emit('sent_finish')  

if __name__=="__main__":
    app.run(debug=True, host = "0.0.0.0",port=50000)
    socketio.run(app)
