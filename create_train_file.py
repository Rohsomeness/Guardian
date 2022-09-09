# Create training dataset for new user
import time
# from cv2 import *
from cv2 import (VideoCapture, 
                imshow, 
                imwrite, 
                waitKey, 
                destroyWindow, 
                destroyAllWindows)

class TrainData():
    def __init__(self):
        self.unique_counter = 0

    def add_new_train_data(self, name:str):
        self.unique_counter+=1
        path = "dataset/" + str(name).lowercase() + "_" + str(self.unique_counter) + "/"
        counter = 0

        cam = VideoCapture(0)
        image_count = 0
        while cam.isOpened() and image_count < 10:
            image_path = path + "image" + str(counter) + ".png"
            counter+=1
            fail_count = 0

            result, img = cam.read()

            if not result:
                fail_count += 1
                continue
                if fail_count >= 5:
                    print("Error opening camera")
                    exit()
            
            imwrite(image_path, img)
            image_count += 1
            time.sleep(1)

def test_image_capture():
    cam_port = 0   
    cam = VideoCapture(cam_port)

    if not cam.isOpened():
        print("Error openening camera")
        exit()

    result, image = cam.read()

    if result:
        imshow("ImCapWindow", image)
        imwrite("Testimage.png", image)
        waitKey(0)
        destroyWindow("ImCapWindow")
    else:
        print("Error capturing image")
    
    cam.release()
    destroyAllWindows()

def test_video_capture():
    cam = VideoCapture('video_test.avi')

    while cam.isOpened():
        ret, frame = cam.read()
        if not ret:
            print("Can not receive frame")
            break
        imshow('video_window', frame)
        if waitKey(0):
            break

    cam.release()
    destroyAllWindows()

test_image_capture()