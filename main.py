from login_page import LoginWindow
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = LoginWindow()
app.exec_()