from PyQt5 import QtWidgets, uic
from logo import logo_rc
from flashcard_user import User
import menu_page
import about_page
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

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        LoginForm = resource_path('ui/login.ui')
        uic.loadUi(LoginForm, self)
        self.enter_button.clicked.connect(self.create)
        self.about_button.clicked.connect(self.aboutus_show)
        self.show()

    def create(self):
        user=User(self.username_line.text())
        user.login()
        self.menu_show(user)
        
    def menu_show(self,object):
        self.object=object
        self.cams=menu_page.MainWindow(self.object)
        self.cams.show()
        self.close()
        
    
    def aboutus_show(self):
        self.cams=about_page.AboutWindow()
        self.cams.show()