from pi_face_recognition import pi_face_recognition
from create_train_file import TrainData

data = TrainData()
pi_face_recognition(visualize=False, phrases_dict=data.phrases_dict)