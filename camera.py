import cv2
from imageai.Detection import ObjectDetection

COLOR = (255,132,100)   # color of rectangle
# X and Y coordinates for rectangle (coordinates for upper left corner)
X = 250
Y = 100
# width and heigh of rectangle
W = 800
H = 550

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0 (webcam). If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        cv2.rectangle(image,(X,Y),(X+W,Y+H),COLOR,2)    # drawing the rectangle
        cv2.imwrite("capture/test.jpg", image[Y:Y+H, X:X+W])    # saving the an image constantly for prediction
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()