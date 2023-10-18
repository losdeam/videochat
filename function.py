import cv2 
import numpy as np
# 需要一个函数来对视频进行裁剪以压缩大小
def resize(frame):
    return cv2.resize(frame,(320,320))