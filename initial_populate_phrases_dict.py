# from create_train_file import TrainData
from win32com.client import Dispatch
import pickle

phrases_dict = {"sahil":["When I want a manfriend, I'll let you know", "This candle smells like fire!", "Someone's been feeding the beast a little too much lately", \
                         "When I want a manfriend, I'll let you know", "This candle smells like fire!", "Someone's been feeding the beast a little too much lately", \
                         "When I want a manfriend, I'll let you know", "This candle smells like fire!", "Someone's been feeding the beast a little too much lately", \
                         "When I want a manfriend, I'll let you know", "This candle smells like fire!", "Someone's been feeding the beast a little too much lately", \
                         "When I want a manfriend, I'll let you know", "This candle smells like fire!", "Someone's been feeding the beast a little too much lately", \
                         "Out of both of us, guess who has Aashvi's number?", "Out of both of us, guess who has Aashvi's number?", "Out of both of us, guess who has Aashvi's number?", \
                         "Out of both of us, guess who has Aashvi's number?", "Out of both of us, guess who has Aashvi's number?", "Out of both of us, guess who has Aashvi's number?", \
                         "4 0 4 3 3 1 one thousand", "4 0 4 3 3 1 one thousand", "4 0 4 3 3 1 one thousand", "4 0 4 3 3 1 one thousand",\
                         "I want to come on Silly's titties", "I want to come on Silly's titties", "I want to come on Silly's titties",\
                         "I want to come on Silly's titties", "I want to come on Silly's titties", "I want to come on Silly's titties",\
                         "I want to come on Silly's titties", "I want to come on Silly's titties", "I want to come on Silly's titties",\
                         "You're so silly!", "You're so silly!", "You're so silly!", "You're so silly!", "You're so silly!", "You're so silly!", "You're so silly!", \
                         "Silly is hot", "Silly is hot", "Silly is hot", "Silly is hot", "Silly is hot", "Silly is hot",\
                         "Imagine having to listen to a computer insult you for hours while you wait for your clue", "Imagine having to listen to a computer insult you for hours while you wait for your clue", \
                         "Imagine having to listen to a computer insult you for hours while you wait for your clue", "Imagine having to listen to a computer insult you for hours while you wait for your clue", \
                         "Imagine having to listen to a computer insult you for hours while you wait for your clue", "Imagine having to listen to a computer insult you for hours while you wait for your clue", \
                         "Imagine having to listen to a computer insult you for hours while you wait for your clue", "Imagine having to listen to a computer insult you for hours while you wait for your clue", \
                         "Imagine having to listen to a computer insult you for hours while you wait for your clue", "Imagine having to listen to a computer insult you for hours while you wait for your clue", \
                         "Imagine having to listen to a computer insult you for hours while you wait for your clue", "Imagine having to listen to a computer insult you for hours while you wait for your clue", \
                         "Imagine having to listen to a computer insult you for hours while you wait for your clue", "Imagine having to listen to a computer insult you for hours while you wait for your clue", \
                         "It's getting kind of hard to recognize you, you should probably lay off the cookies for a while.", "It's getting kind of hard to recognize you, you should probably lay off the cookies for a while.", \
                         "It's getting kind of hard to recognize you, you should probably lay off the cookies for a while.", "It's getting kind of hard to recognize you, you should probably lay off the cookies for a while.", \
                         "It's getting kind of hard to recognize you, you should probably lay off the cookies for a while.", "It's getting kind of hard to recognize you, you should probably lay off the cookies for a while.", \
                         "It took you this long to get here!? I've been waiting for days", "It took you this long to get here!? I've been waiting for days", "It took you this long to get here!? I've been waiting for days", \
                         "It took you this long to get here!? I've been waiting for days", "It took you this long to get here!? I've been waiting for days", "It took you this long to get here!? I've been waiting for days", \
                         "It took you this long to get here!? I've been waiting for days", "It took you this long to get here!? I've been waiting for days", "It took you this long to get here!? I've been waiting for days", \
                         "You have a 1 in 100 chance to hear the clue. Good luck!", "You have a 1 in 100 chance to hear the clue. Good luck!",\
                         "You have a 1 in 100 chance to hear the clue. Good luck!", "You have a 1 in 100 chance to hear the clue. Good luck!",\
                         "You have a 1 in 100 chance to hear the clue. Good luck!", "You have a 1 in 100 chance to hear the clue. Good luck!",\
                         "You have a 1 in 100 chance to hear the clue. Good luck!", "You have a 1 in 100 chance to hear the clue. Good luck!",\
                         "You have a 1 in 100 chance to hear the clue. Good luck!", "You have a 1 in 100 chance to hear the clue. Good luck!",\
                         "Go eat your cookies", "Go eat your cookies", "Go eat your cookies",\
                         "Go eat your cookies", "Go eat your cookies", "Go eat your cookies",\
                         "L plus ratio", "L plus ratio", "L plus ratio",\
                         "L plus ratio", "L plus ratio", "L plus ratio",\
                          "lihas"], 
                "maanas":["heh... heh... heh... hello mah... mah... manas", "Man... Ass.", "ss... ss... sanam"], 
                "aditi":["Go away we don't have any chocolate.", "Go away we don't have any food.", "itida"], 
                "rohit":["Hey sexy", "Hey daddy", "Hey mommy", "Hey papi", "Mommy", "Daddy"], 
                "vinnie": ["Mah nayum issa veeennee yand yim a homo phoobe", "Please stand up for proper face detection", "einniv"],
                "vatan":["smoking again?", "stop doing weed", "natav"], "dwayne":["Why T F are you here?"]}

speak = Dispatch("SAPI.SpVoice").Speak
print(len(phrases_dict["sahil"]))
# for i in range(len(phrases_dict["sahil"])):
#     speak(phrases_dict["sahil"][i])

with open("phrases_dict.pickle", "wb") as f:
    pickle.dump(phrases_dict, f)

# with open("phrases_dict.pickle", "rb") as f:
#     d = pickle.load(f)

# print(d.keys())