from PyQt5 import QtWidgets, uic
from logo import logo_rc
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
class AboutWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        AboutForm = resource_path('ui/about.ui')
        uic.loadUi(AboutForm, self)
        self.ok_button.clicked.connect(self.exit)
        self.show()
        
    def exit(self):
        self.close()

