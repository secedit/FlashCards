import time
import json
from flashcard_user import User
import sys
import os
# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
class Game:
    def __init__(self, obj):
        self.object = obj
        self.true_number = 0
        self.attempts_number = 0
        self.word_list = self.words()
    
    def starting_time(self):
        self.start_time = time.time()
        return self.start_time

    def totalTime(self):
        end_time = time.time()
        self.total_time = end_time - self.start_time
        return self.total_time

    def words(self):
        dataFile = resource_path('data/word.json')
        self.level = str(self.object.level)
        with open(dataFile,'r') as json_file:
            data = json.load(json_file)
            words = []
            for word in data[self.level]:
                level_words = []
                level_words.append(word)
                level_words.append(data[self.level][word])
                words.append(level_words)
        return words 

    def show_words(self):
        if self.true_number == 20:
            self.object.level += 1
            self.totalTime()
            self.object.registerUserStat(self.object.level, self.total_time)
            self.starting_time()
            self.word_list = self.words()
            self.true_number = 0
            self.attempts_number = 0
        self.nl = self.word_list[self.true_number][0]
        self.en = self.word_list[self.true_number][1]
        return self.nl, self.en, self.true_number


    def total_attempt_number(self):
        self.attempts_number += 1
        return self.attempts_number

    def true(self):
        self.true_number += 1

    def false(self):
        self.false_word = self.word_list.pop(self.true_number)
        self.word_list.append(self.false_word)