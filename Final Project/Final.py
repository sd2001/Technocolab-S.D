import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime
import pyowm
import pytz
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from five_day_forecast import find_min_max
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


    
class Ui_MainWindow(object):
    def UI(self,days,min_t,max_t):
        canvas = Canvas(parent=None,width=7, height=5,dpi=100,days=self.days,min_t=self.min_t,max_t=self.max_t)
        #canvas.move(80,210)
    def pressed(self):
        self.place=self.lineEdit.text() 
        self.unit_t=None
        print(self.place)
        if self.checkBox.isChecked()==True and self.checkBox_2.isChecked()==True:
            print("Select any 1")            
        elif self.checkBox.isChecked()==True and self.checkBox_2.isChecked()==False:
            self.unit_t=self.checkBox.text()
            self.days,self.min_t,self.max_t=find_min_max(self.place,self.unit_t)
        elif self.checkBox_2.isChecked()==True and self.checkBox.isChecked()==False:
            self.unit_t=self.checkBox_2.text()
            self.days,self.min_t,self.max_t=find_min_max(self.place,self.unit_t)           
        self.UI(self.days,self.min_t,self.max_t)
                
           
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 801)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(840, 120, 131, 41))
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
        self.checkBox_2.setGeometry(QtCore.QRect(560, 140, 111, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 250, 891, 471))
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setPixmap(QtGui.QPixmap("white.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 26))
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
        self.pushButton_2.clicked.connect(self.show_photo)
        #self.label_3.setPixmap(QtGui.QPixmap("figure.png"))
        #print("Done")          
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather App-SD"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "Location:"))
        self.label_2.setText(_translate("MainWindow", "Temperature Unit -"))
        self.checkBox.setText(_translate("MainWindow", "Celcius"))
        self.checkBox_2.setText(_translate("MainWindow", "Fahrenheit"))
        self.pushButton_2.setText(_translate("MainWindow", "GRAPH"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        
    def show_photo(self):
        self.label_3.setPixmap(QtGui.QPixmap("figure.png"))
        print("Done")  

class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 7, height = 5, dpi = 100, days=1,min_t=None,max_t=None):
        fig = Figure(figsize=(width, height), dpi=dpi)        
        
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)        
        self.plot_bars(days,min_t,max_t)
 
 
    def plot_bars(self,days,min_t,max_t):        
        days=dates.date2num(days)
        bar_min=plt.bar(days-0.2, min_t, width=0.4, color='r')
        bar_max=plt.bar(days+0.2, max_t, width=0.4, color='b')        
        plt.xticks(days)
        x_y_axis=plt.gca()
        xaxis_format = dates.DateFormatter('%m/%d')
        x_y_axis.xaxis.set_major_formatter(xaxis_format)
        plt.savefig('figure.png')
        
        #self.photo.setPixmap(QtGui.QPixmap("figure.png"))
        
        

if __name__ =="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
