import math
from scipy.stats import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QCheckBox, QLineEdit, QPushButton
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSize, Qt

font = QtGui.QFont()
font.setFamily("Segoe UI Symbol")
font.setPointSize(20)
font.setWeight(100)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Setting up the app
        self.setWindowTitle("Statistics")
        self.setWindowIcon(QtGui.QIcon("Path/to/Your/image/file.png"))
        self.setMinimumWidth(resolution.width() / 3)
        self.setMinimumHeight(resolution.height() / 1.5)
        self.setStyleSheet(
            "QWidget {background-color: rgba(45,45,45,255);} QScrollBar:horizontal {width: 1px; height: 1px;"
            "background-color: rgba(45,45,45,255);} QScrollBar:vertical {width: 1px; height: 1px;"
            "background-color: rgba(45,45,45,255);}")

        # textbox for confidence level
        cLevel = QtWidgets.QTextEdit(self)
        cLevel.setPlaceholderText("Confidence Level:")
        cLevel.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(0,0,0,100); color: rgba(0,90,255,255);"
            "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        cLevel.setFont(font)
        cLevel.resize(350, 100)
        cLevel.move(50, 50)

        # textbox for meanorprop
        meanorprop = QtWidgets.QComboBox(self)
        meanorprop.addItems(["mean", "proportion"])
        meanorprop.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(0,0,0,100); color: rgba(0,90,255,255);"
            "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        meanorprop.setFont(font)
        meanorprop.resize(350, 100)
        meanorprop.move(50, 250)


import sys
app = QApplication(sys.argv)
desktop = QtWidgets.QApplication.desktop()
resolution = desktop.availableGeometry()
window = MainWindow()
window.setWindowOpacity(1)
window.show()
window.move(resolution.center() - window.rect().center())
sys.exit(app.exec_())