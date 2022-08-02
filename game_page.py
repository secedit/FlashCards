from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
from flashcard_game import Game
import menu_page
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

class GameWindow(QtWidgets.QMainWindow):
    def __init__(self,object):
        self.object=object
        self.game=Game(self.object)
        self.game.starting_time()
        super(GameWindow, self).__init__()
        GameForm = resource_path('ui/game.ui')
        uic.loadUi(GameForm, self)
        self.true_button.setEnabled(False)
        self.false_button.setEnabled(False)
        self.back_button.clicked.connect(self.menu_show)
        self.true_button.clicked.connect(self.true_button_function)
        self.false_button.clicked.connect(self.false_button_function)
        self.exit_button.clicked.connect(self.exit)
        self.timer_()
        self.show()

    def menu_show(self):
        self.cams=menu_page.MainWindow(self.object)
        self.passedTime=int(self.game.totalTime())
        self.object.registerUserStat(self.object.level, self.passedTime)
        self.cams.show()
        self.close()
        
    def starting(self):
        self.word_nl, self.word_en , self.true_num = self.game.show_words()
        self.totalTry_num=self.game.attempts_number
        self.language_label.setText("NEDERLANDS")
        self.label_2.setStyleSheet("background-color:rgb(5, 119, 161);\nborder-radius:40px;\nborder-style:solid;\nborder-width:3px;\nborder-color: rgb(184, 88, 44);\n")
        self.true_button.setEnabled(False)
        self.false_button.setEnabled(False)
        self.progressBar.setProperty('value', self.true_num)
        self.word_label.setText(self.word_nl)
        self.true_label.setText(str(self.true_num))
        self.try_label.setText(str(self.totalTry_num))
        self.level_label.setText("LEVEL "+ str(self.object.level))
        
           
    def en_word(self, en):
        self.en=en
        self.language_label.setText("ENGLISH")
        self.label_2.setStyleSheet("background-color:rgb(255,255,220);\nborder-radius:40px;\nborder-style:solid;\nborder-width:3px;\nborder-color: rgb(184, 88, 44);\n")
        self.word_label.setText(self.en)
    
    def update(self):
        self.timelabel.setText(str(self.count))
        if self.count == 0:
            self.true_button.setEnabled(True)
            self.false_button.setEnabled(True)
            self.timer.stop()
            self.en_word(self.word_en)
        self.count -= 1
        
    def timer_(self):
            self.timer=QTimer(self)
            self.timer.timeout.connect(self.update)
            self.timer.start(1000)
            self.count=3
            self.starting()
        
    def true_button_function(self):
       self.game.true()
       self.game.total_attempt_number()
       self.timer_()
        
    def false_button_function(self):
       self.game.false()
       self.game.total_attempt_number()
       self.timer_()
           
    def exit(self):
       self.passedTime=int(self.game.totalTime())
       self.object.registerUserStat(self.object.level, self.passedTime)
       self.close()