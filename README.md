# Object-Identifier
A python project that uses ImageAI to identify objects from real-time webcam video.

## Descriptions

The project uses ImageAI to process real-time video from webcam and identifies the objects within the image. 
The Deep Neural Network is developed by the ImageAI library and can identify up to 80 objects. 
A flask app is used to turn the webcam on and display the video for reference. predict.py loads the DNN model and 
starts predicting the objects in the images.
The images of predicted objects are available for future processing.

## How to use

1. Clone the repo to your local computer.
2. Download resnet50_coco_best_v2.0.1.h5 (DNN) and add it to the folder: https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0 
3. Open terminal and navigate to the folder
4. Run the following command: flask_run
5. You can open the URL to see the video (click on see for yourself in the website).
6. Run the following command: python3 predict.py
7. The code will ask you to choose type p to predict and e to exit
8. Predictions are displayed along with the confidence level of the DNN

Note: There are error handling messeges that might appear. You can choose to retry or to exit.

## Dependencies

1. Download python3: 

```https://python.org```
2. Install tensorflow 1.4.0 or newer: 

```pip3 install tensorflow```
3. Install OpenCV: 

```pip3 install opencv-python```
4. Install Keras: 

```pip3 install keras```
5. Install Imageai: 

```pip3 install imageai --upgrade```

## Reference

1. https://imageai.readthedocs.io/en/latest/index.html
2. https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606
