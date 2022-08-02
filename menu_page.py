from PyQt5 import QtWidgets, uic
import login_page
import game_page
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


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,object):
        self.object=object
        super(MainWindow, self).__init__()
        MenuForm = resource_path('ui/menu.ui')
        uic.loadUi(MenuForm, self)
        self.username_label.setText("WELCOME " + str(self.object.name.upper()))
        self.level_label.setText("LEVEL " + str(self.object.level))
        self.totaltime_label.setText("TOTALTİME " + str(self.object.totalTime))
        self.level_progress.setProperty('value', self.progress_bar())
        self.logout_button.clicked.connect(self.login_window_show)
        self.play_button.clicked.connect(self.play_window_show)
        self.show()
    
    def login_window_show(self):
       self.cams=login_page.LoginWindow()
       self.cams.show()
       self.close()
   
    def play_window_show(self):
       self.cams=game_page.GameWindow(self.object)
       self.cams.show()
       self.close()
        
    def progress_bar(self):
       return (self.object.level/250)*100