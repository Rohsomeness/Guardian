"""Main file for the Guardian project"""
import argparse
from pi_face_recognition import pi_face_recognition
from create_train_file import TrainData


if __name__ == "__main__":
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()

    # make a store true argument for visualize, default to False
    ap.add_argument("-v", "--visualize", action="store_true",
        help="visualize the video stream")
    # make another store true argument for printing the phrases
    ap.add_argument("-p", "--print_phrases", action="store_true",
        help="print the phrases")

    # parse the arguments
    args = vars(ap.parse_args())

    # create a new TrainData object
    data = TrainData()

    # call the pi_face_recognition method with the visualize and phrases_dict arguments
    pi_face_recognition(
        visualize=args["visualize"],
        print_phrases = args["print_phrases"],
        phrases_dict=data.phrases_dict
    )
