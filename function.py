import cv2 
import numpy as np
import base64
# 需要一个函数来对视频进行裁剪以压缩大小
def resize(frame):
    return cv2.resize(frame,(320,320))



def cvRead(img):
    '''
    Args:
        img: base64格式的图片
    Returns:array格式RGB形式的图片
    '''
    #将以Base64格式编码的字符串转换回其原始形式
    img = base64.b64decode(img)
    #将图片数据转换为numpy数组
    img2 = np.frombuffer(img, dtype=np.uint8)
    #将转换后的数组解码为图像
    img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)
    # #将BGR形式图像转为RGB形式
    # img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    return img2