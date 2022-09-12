# from create_train_file import TrainData
from win32com.client import Dispatch
import pickle

phrases_dict = {"sahil":["When I want a manfriend, I'll let you know", "Ahhhhhhhhhhhhhhhh!", "Someone's been feeding the beast a little too much huh", "lihas"], 
                "maanas":["heh... heh... heh... hello mah... mah... manas", "Man... Ass.", "ss... ss... sanam"], 
                "aditi":["Go away we don't have any chocolate.", "Go away we don't have any food.", "itida"], 
                "rohit":["Hey sexy", "Hey daddy"], 
                "vinnie": ["Mah nayum issa veeennee yand yim a homo phoobe", "Please stand up for proper face detection", "einniv"],
                "vatan":["smoking again?", "stop doing weed", "natav"], "dwayne":["Why T F are you here?"]}

speak = Dispatch("SAPI.SpVoice").Speak
speak(phrases_dict["sahil"][2])

with open("phrases_dict.pickle", "wb") as f:
    pickle.dump(phrases_dict, f)

# with open("phrases_dict.pickle", "rb") as f:
#     d = pickle.load(f)

# print(d.keys())