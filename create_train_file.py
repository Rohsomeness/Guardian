# pylint: disable=E0611, R1722, W0719, E0401
"""Create training data for the model"""
import time
import os
from typing import List
import pickle
# from cv2 import *
from cv2 import (VideoCapture,
                imshow,
                imwrite,
                waitKey,
                destroyWindow,
                destroyAllWindows)

class TrainData():
    """Class for training data"""

    def __init__(self, phrases_dict_path="phrases_dict.pickle"):
        """Init class and load phrases dict from file"""
        self.unique_counter = 0
        self.phrases_dict = {}
        self.load_phrases_dict(phrases_dict_path)

    def add_new_train_data(self, name:str, phrases:List[str]=None, take_pics=False):
        """Add new training data for name and provided phrases"""
        print("Adding new training data for ", name)
        self.phrases_dict[name] = [("Hi " + name)]
        for phrase in phrases:
            self.phrases_dict[name].append(phrase)
        self.unique_counter+=1
        self.store_phrases_dict()

        if take_pics:
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
            destroyAllWindows()

    def store_phrases_dict(self, path:str="phrases_dict.pickle"):
        """Write phrases dict to file"""
        with open(path, 'wb') as f:
            pickle.dump(self.phrases_dict, f)

    def load_phrases_dict(self, path:str="phrases_dict.pickle"):
        """Read phrases dict from file"""
        if not os.path.isfile(path):
            with open(path, 'rb') as f:
                pickle.dump({}, f)
        with open(path, 'rb') as f:
            self.phrases_dict = pickle.load(f)

    def add_phrases(self, name: str, phrases: List[str]):
        """Add phrases for existing name"""
        if name not in self.phrases_dict:
            raise Exception("name not recognized")
        self.phrases_dict[name] += phrases
        self.store_phrases_dict()

    def set_unique_counter(self, num=9):
        """Set counter, useful for if adding images through camera"""
        self.unique_counter = num

def test_image_capture():
    """Test image capture"""
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
    """Test video capture"""
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

if __name__ == "__main__":
    train_data = TrainData()


    # Example usage of adding new training data:
    # train_data.add_new_train_data(
    #     name="example_name",
    #     phrases=[
    #         "example phrase 1",
    #         "example phrase 2"
    #     ],
    #     take_pics=False,
    # )

    # Example usage of adding phrases for existing name:
    # train_data.add_phrases(
    #     name="example_name",
    #     phrases=["example phrase 3", "example phrase 4"]
    # )

    print(train_data.phrases_dict.keys())
    print("Done")
