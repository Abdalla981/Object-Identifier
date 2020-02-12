from imageai.Detection import ObjectDetection
import os

PATH = "capture/test.jpg"
TYPE = 'file'
X = 250
Y = 100
W = 800
H = 550

def load_model():
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    return detector

detector = load_model()
while True:
    try:
        a, detections = detector.detectObjectsFromImage(input_image=PATH, input_type=TYPE, output_type="array")
        for det in detections:
            print("Predictions:")
            print(">>>>>>>>>" + det['name'])
    except:
        continue
