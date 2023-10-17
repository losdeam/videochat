import cv2
import numpy
import io
from PIL import Image

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
        # c = cv2.waitKey(1)
        # if (c == "n"): #in "n" key is pressed while the popup window is in focus
        #     self.camera_index += 1 #try the next camera index
        #     self.cam = cv2.VideoCapture(self.camera_index)
        #     if not self.cam: #if the next camera index didn't work, reset to 0.
        #         self.camera_index = 0
        #         self.cam = cv2.VideoCapture(self.camera_index)

        if ret_val :
            cv2_im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            pil_im = Image.fromarray(cv2_im)
            
            #创建一个转换为byte类型的方法
            b = io.BytesIO()
            # 将 pil_im中内容以'jpg'的格式使用b所表示方法（转换为byte类型)进行保存
            pil_im.save(b, format='PNG')
            im_bytes = b.getvalue()

            return im_bytes
        return None

    def set_frame(self, frame_bytes):
        pil_bytes = io.BytesIO(frame_bytes)
        pil_image = Image.open(pil_bytes)
        cv_image = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
        cv2.imshow(self.name, cv_image)
        cv2.waitKey(1)

if __name__=="__main__":
    vf = VideoFeed("test",1)
    while 1:
        m = vf.get_frame()
        vf.set_frame(m)

