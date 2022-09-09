# Create training dataset for new user
import time
import os
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
        print("Adding new training data for ", name)
        self.unique_counter+=1
        path = "dataset/" + str(name).lower() + "_" + str(self.unique_counter)
        counter = 0

        os.mkdir(path)

        cam = VideoCapture(0)
        image_count = 0
        while cam.isOpened() and image_count < 10:
            image_path = path + "/image" + str(counter) + ".png"
            counter+=1
            fail_count = 0

            result, img = cam.read()

            if not result:
                fail_count += 1
                if fail_count >= 5:
                    print("Error opening camera")
                    exit()
                continue
            
            imwrite(image_path, img)
            image_count += 1
            time.sleep(1)
        
        cam.release()
        # destroyAllWindows()

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
    cam = VideoCapture(0)

    while cam.isOpened():
        ret, frame = cam.read()
        if not ret:
            print("Can not receive frame")
            break
        imshow('video_window', frame)
        if waitKey(1) == ord('q'):
            break

    cam.release()
    destroyAllWindows()

train_data = TrainData()
train_data.add_new_train_data("Rohit")
print("Done")
# test_video_capture()
# test_image_capture()