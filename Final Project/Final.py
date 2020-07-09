import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime
import pyowm
import pytz
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
import numpy as np
from min_max_temp import find_min_max
from line_forecast
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


    
class Ui_MainWindow(object):
    #def UI(self,days,min_t,max_t):
        #canvas=Canvas(parent=None,width=7, height=5,dpi=100,days=self.days,min_t=self.min_t,max_t=self.max_t)
        #canvas.move(80,210)
    def pressed(self):
        self.place=self.lineEdit.text() 
        self.unit_t=None
        print(self.place)
        if self.checkBox.isChecked()==True and self.checkBox_2.isChecked()==True:
            print("Select any 1")            
        elif self.checkBox.isChecked()==True and self.checkBox_2.isChecked()==False:
            self.unit_t=self.checkBox.text()
            find_min_max(self.place,self.unit_t)
        elif self.checkBox_2.isChecked()==True and self.checkBox.isChecked()==False:
            self.unit_t=self.checkBox_2.text()
            find_min_max(self.place,self.unit_t)           
        #self.UI(self.days,self.min_t,self.max_t)
                
           
  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 872)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 130, 131, 41))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(80, 50, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 50, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(330, 140, 141, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(530, 140, 111, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 250, 951, 541))
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setPixmap(QtGui.QPixmap("../../Final Project/white.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 26))
        self.menubar.setObjectName("menubar")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuUser.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.pressed) 
        self.pushButton_2.clicked.connect(self.show_bar)
        self.pushButton_3.clicked.connect(self.show_line)
        #self.label_3.setPixmap(QtGui.QPixmap("figure.png"))
        #print("Done")          
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "Location:"))
        self.label_2.setText(_translate("MainWindow", "Temperature Unit -"))
        self.checkBox.setText(_translate("MainWindow", "Celcius"))
        self.checkBox_2.setText(_translate("MainWindow", "Fahrenheit"))
        self.pushButton_2.setText(_translate("MainWindow", "BAR GRAPH"))
        self.pushButton_3.setText(_translate("MainWindow", "LINE GRAPH"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        
    def show_bar(self):
        self.label_3.setPixmap(QtGui.QPixmap("figure.png"))
        print("Done")  
    def show_line(self):
        self.label_3.setPixmap(QtGui.QPixmap("figure_line.png"))
        print("Done")       
        

if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())