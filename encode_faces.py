# pylint: disable=E1101, W0311, R0914
"""Encode faces in images and save them to a pickle file"""
import argparse
import os
import pickle

import cv2
import face_recognition
from imutils import paths


def test_encode_faces(input_args=None):
	"""encode faces"""
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--dataset", required=False,
		help="path to input directory of faces + images")
	ap.add_argument("-e", "--encodings", required=False,
		help="path to serialized db of facial encodings")
	ap.add_argument("-d", "--detection-method", type=str, default="hog",
		help="face detection model to use: either `hog` or `cnn`")
	args = vars(ap.parse_args())
	if input_args:
		args = {
			"dataset":"dataset",
			"detection_method":"hog",
			"encodings":"encodings.pickle",
			"cascade":"haarcascade_frontalface_default.xml"
		}

	# grab the paths to the input images in our dataset
	print("[INFO] quantifying faces...")
	image_paths = list(paths.list_images(args["dataset"]))

	# initialize the list of known encodings and known names
	known_encodings = []
	known_names = []

	# loop over the image paths
	for (i, image_path) in enumerate(image_paths):
		# extract the person name from the image path
		print(f"[INFO] processing image {i+1}/{len(image_paths)}")
		name = image_path.split(os.path.sep)[-2]
		name = name.split("_")[0]

		# load the input image and convert it from BGR (OpenCV ordering)
		# to dlib ordering (RGB)
		image = cv2.imread(image_path)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb,
			model=args["detection_method"])

		# compute the facial embedding for the face
		encodings = face_recognition.face_encodings(rgb, boxes)

		# loop over the encodings
		for encoding in encodings:
			# add each encoding + name to our set of known names and
			# encodings
			known_encodings.append(encoding)
			known_names.append(name)

	# dump the facial encodings + names to disk
	print("[INFO] serializing encodings...")
	data = {"encodings": known_encodings, "names": known_names}

	with open(args["encodings"], "wb") as f:
		f.write(pickle.dumps(data))

test_encode_faces(input_args=True)
