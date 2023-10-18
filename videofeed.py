import cv2

import base64

import function

class VideoFeed:

    def __init__(self,name="w1",capture=1):
        print (name)
        self.camera_index = 0
        self.name = name
        self.cam = None 
                # print(capture)
        if capture == 1:
            self.cam = cv2.VideoCapture(self.camera_index)
        else :
            self.cam = cv2.VideoCapture(capture)

    def get_frame(self):
        ret_val, img = self.cam.read()
        if ret_val :
            img = function.resize(img)
            img_bytes2 = cv2.imencode('.png', img)[1].tostring()
            img_bytes2 = base64.b64encode(img_bytes2)
            return img_bytes2
        return None
    def get_video(self):
        pass
    def set_frame(self, frame_bytes):
        cv_image = function.cvRead(frame_bytes)
        cv2.imshow(self.name, cv_image)
        cv2.waitKey(1)
    def get_video(self,video_bytes):
        pass
if __name__=="__main__":
    vf = VideoFeed("test",1)
    while 1:
        m = vf.get_frame()
        vf.set_frame(m)

