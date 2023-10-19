import cv2 
import numpy as np
import base64
import json
# 需要一个函数来对视频进行裁剪以压缩大小
def resize(frame):
    return cv2.resize(frame,(320,320))

# 图像预处理整合
def transform(img):
    img = resize(img)
    return img 

# 将base64格式的图片转化为array格式BGR形式的图片
def cvRead(img):
    '''
    Args:
        img: base64格式的图片
    Returns:array格式BGR形式的图片
    '''
    #将以Base64格式编码的字符串转换回其原始形式
    img = base64.b64decode(img)
    #将图片数据转换为numpy数组
    img2 = np.frombuffer(img, dtype=np.uint8)
    #将转换后的数组解码为图像
    img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)
    return img2

def combine(frame ,audio):
    msg = {
        "frame" : str(frame),
        "audio" : str(audio)
    }
    return json.dumps(msg)

def get_json(msg_byte):
    msg_str = msg_byte.decode()
    return  json.loads(msg_str)