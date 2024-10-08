# pylint: disable=W0311, E1101, R0914, R0912, R0915, R1732, E0401
"""Run facial recognition for Raspberry Pi using OpenCV and face_recognition library."""
import argparse
import pickle
import time
from random import randint

import cv2
import face_recognition
import imutils
from imutils.video import FPS, VideoStream
from win32com.client import Dispatch


def pi_face_recognition(visualize=False, phrases_dict=None, print_phrases=False):
	"""Run facial recognition for Raspberry Pi using OpenCV and face_recognition library."""
	if phrases_dict is None:
		phrases_dict = {}
	# construct the argument parser and parse the arguments
	# ap = argparse.ArgumentParser()
	# ap.add_argument("-c", "--cascade", required=True,
	# 	help = "path to where the face cascade resides")
	# ap.add_argument("-e", "--encodings", required=True,
	# 	help="path to serialized db of facial encodings")
	# args = vars(ap.parse_args())
	args = {"cascade":"haarcascade_frontalface_default.xml", "encodings":"encodings.pickle"}

	speak = None
	if not print_phrases:
		speak = Dispatch("SAPI.SpVoice").Speak
	# load the known faces and embeddings along with OpenCV's Haar
	# cascade for face detection
	print("[INFO] loading encodings + face detector...")
	data = pickle.loads(open(args["encodings"], "rb").read())
	detector = cv2.CascadeClassifier(args["cascade"])

	# initialize the video stream and allow the camera sensor to warm up
	# if visualize:
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	# vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)

	# start the FPS counter
	fps = FPS().start()

	# loop over frames from the video file stream
	while True:
		# grab the frame from the threaded video stream and resize it
		# to 500px (to speedup processing)
		frame = vs.read()
		frame = imutils.resize(frame, width=500)

		# convert the input frame from (1) BGR to grayscale (for face
		# detection) and (2) from BGR to RGB (for face recognition)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		# detect faces in the grayscale frame
		rects = detector.detectMultiScale(gray, scaleFactor=1.1,
			minNeighbors=5, minSize=(30, 30))

		# OpenCV returns bounding box coordinates in (x, y, w, h) order
		# but we need them in (top, right, bottom, left) order, so we
		# need to do a bit of reordering
		boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

		# compute the facial embeddings for each face bounding box
		encodings = face_recognition.face_encodings(rgb, boxes)
		names = []

		# loop over the facial embeddings
		for encoding in encodings:
			# attempt to match each face in the input image to our known
			# encodings
			matches = face_recognition.compare_faces(data["encodings"],
				encoding)
			name = "Unknown"

			# check to see if we have found a match
			if True in matches:
				# find the indexes of all matched faces then initialize a
				# dictionary to count the total number of times each face
				# was matched
				matched_idxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}

				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matched_idxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1

				# determine the recognized face with the largest number
				# of votes (note: in the event of an unlikely tie Python
				# will select first entry in the dictionary)
				name = max(counts, key=counts.get)

			# update the list of names
			names.append(name)

		# loop over the recognized faces
		if visualize:
			for ((top, right, bottom, left), name) in zip(boxes, names):
				# draw the predicted face name on the image
				cv2.rectangle(frame, (left, top), (right, bottom),
					(0, 255, 0), 2)
				y = top - 15 if top - 15 > 15 else top + 15
				cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
					0.75, (0, 255, 0), 2)

		for n in names:
			if n in phrases_dict:
				if print_phrases:
					print(phrases_dict[n][randint(0, len(phrases_dict[n])-1)])
				else:
					speak(phrases_dict[n][randint(0, len(phrases_dict[n])-1)])
				time.sleep(1)


		# display the image to our screen
		if visualize:
			cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

		# update the FPS counter
		fps.update()

	# stop the timer and display FPS information
	fps.stop()
	print(f"[INFO] elasped time: {fps.elapsed():.2f}")
	print(f"[INFO] approx. FPS: {fps.fps():.2f}")
	# do a bit of cleanup
	cv2.destroyAllWindows()
	vs.stop()

def test_pi_face_recognition(input_args=None):
	"""Test facial recognition for Raspberry Pi using OpenCV and face_recognition library."""
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-c", "--cascade", required=False,
		help = "path to where the face cascade resides")
	ap.add_argument("-e", "--encodings", required=False,
		help="path to serialized db of facial encodings")
	args = vars(ap.parse_args())
	if input_args:
		args = {"cascade":"haarcascade_frontalface_default.xml", "encodings":"encodings.pickle"}

	# load the known faces and embeddings along with OpenCV's Haar
	# cascade for face detection
	print("[INFO] loading encodings + face detector...")
	data = pickle.loads(open(args["encodings"], "rb").read())
	detector = cv2.CascadeClassifier(args["cascade"])

	# initialize the video stream and allow the camera sensor to warm up
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	# vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)

	# start the FPS counter
	fps = FPS().start()

	# loop over frames from the video file stream
	while True:
		# grab the frame from the threaded video stream and resize it
		# to 500px (to speedup processing)
		frame = vs.read()
		frame = imutils.resize(frame, width=500)

		# convert the input frame from (1) BGR to grayscale (for face
		# detection) and (2) from BGR to RGB (for face recognition)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		# detect faces in the grayscale frame
		rects = detector.detectMultiScale(gray, scaleFactor=1.1,
			minNeighbors=5, minSize=(30, 30))

		# OpenCV returns bounding box coordinates in (x, y, w, h) order
		# but we need them in (top, right, bottom, left) order, so we
		# need to do a bit of reordering
		boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

		# compute the facial embeddings for each face bounding box
		encodings = face_recognition.face_encodings(rgb, boxes)
		names = []

		# loop over the facial embeddings
		for encoding in encodings:
			# attempt to match each face in the input image to our known
			# encodings
			matches = face_recognition.compare_faces(data["encodings"],
				encoding)
			name = "Unknown"

			# check to see if we have found a match
			if True in matches:
				# find the indexes of all matched faces then initialize a
				# dictionary to count the total number of times each face
				# was matched
				matched_idxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}

				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matched_idxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1

				# determine the recognized face with the largest number
				# of votes (note: in the event of an unlikely tie Python
				# will select first entry in the dictionary)
				name = max(counts, key=counts.get)

			# update the list of names
			names.append(name)

		# loop over the recognized faces
		for ((top, right, bottom, left), name) in zip(boxes, names):
			# draw the predicted face name on the image
			cv2.rectangle(frame, (left, top), (right, bottom),
				(0, 255, 0), 2)
			y = top - 15 if top - 15 > 15 else top + 15
			cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
				0.75, (0, 255, 0), 2)

		# display the image to our screen
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

		# update the FPS counter
		fps.update()

	# stop the timer and display FPS information
	fps.stop()
	print(f"[INFO] elasped time: {fps.elapsed():.2f}")
	print(f"[INFO] approx. FPS: {fps.fps():.2f}")
	# do a bit of cleanup
	cv2.destroyAllWindows()
	vs.stop()

# speak = Dispatch("SAPI.SpVoice").Speak
# speak("Hi Yamini and Adhi thee")
# test_pi_face_recognition(input_args=True)
