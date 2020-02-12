from imageai.Detection import ObjectDetection
import os
import cv2

PATH = "capture/test.jpg"   #path to image for detection (same as the one we save in camera.py)

def load_model():   # function to load model
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    return detector

def user_prompt(error, error_type=None): # function to ask display a user prompt to use the platform
    if(error):
        print("##############################################")
        print("This error occurred: " + str(error_type) + ". Do you want to try again or exit?")
        print("1. Type 'p' for Try Again")
        print("2. Type 'e' for Exit")
        decision = input("Please select: ")
        print("##############################################")
    else:
        print("##############################################")
        print("1. Type 'p' for Predict")
        print("2. Type 'e' for Exit")
        decision = input("Please select: ")
        print("##############################################")
    return decision

def predict():
    # returned_image is a the original image with highlight on the detected images
    # detections is an array of dictionaries for predictions and their probability
    # detected_images is an array of arrays of the individual objects that were detected
    # For more details, Imageai website: https://imageai.readthedocs.io/en/latest/detection/index.html
    returned_image, detections, detected_images = detector.detectObjectsFromImage(input_image=PATH, input_type='file', output_type="array", extract_detected_objects=True)

    if(len(detections) == 0):
        print("No object detected!")
    else:
        for det in detections:  # display predictions
            print("Predictions:")
            print("- " + det['name'] + " : " + str.format('{0:.2f}', det['percentage_probability']))
    return returned_image, detections, detected_images

detector = load_model()
decision = user_prompt(0)   # 0 means no error
while (decision == 'p'):
    try:
        returned_image, detections, detected_images = predict()
        cv2.imwrite("capture/returned_image.jpg", returned_image) # Saving the returned image
        decision = user_prompt(0)
    except Exception as e:
        decision = user_prompt(1, e)   # 1 means there is an error