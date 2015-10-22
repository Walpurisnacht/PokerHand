import sys
import os
import numpy as np
import sklearn
from PyQt4.QtGui import *
from PyQt4 import QtCore

from sklearn import svm

#Set up ML and scikit-learn
clf = svm.SVC(gamma=0.01, C=100)

class MainActivity(QWidget):

    #constructor
    def __init__(self):
        super(MainActivity, self).__init__()

        self.initUI()

    #init windows
    def initUI(self):

        #main panel
        self.center()
        self.resize(600, 400)

        self.setWindowTitle('Poker Hand')
        self.setWindowIcon(QIcon('d.png'))

        #selection layout
            #label
        self.lbl1 = QLabel('Card #1')
        self.lbl2 = QLabel('Card #2')
        self.lbl3 = QLabel('Card #3')
        self.lbl4 = QLabel('Card #4')
        self.lbl5 = QLabel('Card #5')

        boxLabel = []
        boxLabel.append(self.lbl1)
        boxLabel.append(self.lbl2)
        boxLabel.append(self.lbl3)
        boxLabel.append(self.lbl4)
        boxLabel.append(self.lbl5)
        
            #card name
        self.cbName1 = QComboBox()
        self.cbName2 = QComboBox()
        self.cbName3 = QComboBox()
        self.cbName4 = QComboBox()
        self.cbName5 = QComboBox()

        self.boxName = []
        self.boxName.append(self.cbName1)
        self.boxName.append(self.cbName2)
        self.boxName.append(self.cbName3)
        self.boxName.append(self.cbName4)
        self.boxName.append(self.cbName5)
        
            #card type
        self.cbType1 = QComboBox()
        self.cbType2 = QComboBox()
        self.cbType3 = QComboBox()
        self.cbType4 = QComboBox()
        self.cbType5 = QComboBox()

        self.boxType = []
        self.boxType.append(self.cbType1)
        self.boxType.append(self.cbType2)
        self.boxType.append(self.cbType3)
        self.boxType.append(self.cbType4)
        self.boxType.append(self.cbType5)
        
        for x in range(5):
            self.boxName[x].addItem('A')
            self.boxName[x].addItem('2')
            self.boxName[x].addItem('3')
            self.boxName[x].addItem('4')
            self.boxName[x].addItem('5')
            self.boxName[x].addItem('6')
            self.boxName[x].addItem('7')
            self.boxName[x].addItem('8')
            self.boxName[x].addItem('9')
            self.boxName[x].addItem('J')
            self.boxName[x].addItem('Q')
            self.boxName[x].addItem('K') 
            self.boxType[x].addItem('♥')
            self.boxType[x].addItem('♠')
            self.boxType[x].addItem('♦')
            self.boxType[x].addItem('♣')

            #layout
        grid = QGridLayout()

        for x in range(5):
            grid.addWidget(boxLabel[x],1,x)
            grid.addWidget(self.boxName[x],2,x)
            grid.addWidget(self.boxType[x],3,x)

            #predict value
        self.lblVal = QLabel("Prediction info")
        grid.addWidget(self.lblVal,4,3)
        self.boxPredict = QComboBox()
        self.boxPredict.addItem("Nothing | 0")
        self.boxPredict.addItem("One pair | 1")
        self.boxPredict.addItem("Two pairs | 2")
        self.boxPredict.addItem("Three of a kind | 3")
        self.boxPredict.addItem("Straight | 4")
        self.boxPredict.addItem("Flush | 5")
        self.boxPredict.addItem("Full house | 6")
        self.boxPredict.addItem("Four of a kind | 7")
        self.boxPredict.addItem("Straight flush | 8")
        self.boxPredict.addItem("Royal flush | 9")
        grid.addWidget(self.boxPredict,5,3)

        #debug
        #QMessageBox.about(self,"Info",self.boxPredict.itemText(0))
        #QMessageBox.about(self,"Info",str(self.boxPredict.currentIndex()))

        grid.setContentsMargins(60,20,50,30)

        #feature
            #single input button
        self.btnSolve = QPushButton('Single input')
        self.btnSolve.resize(self.btnSolve.sizeHint())
        self.btnSolve.clicked.connect(self.solveClick)

        grid.addWidget(self.btnSolve,4,0)

            #training button
        self.btnTrain = QPushButton('Training')
        self.btnTrain.resize(self.btnTrain.sizeHint())
        self.btnTrain.clicked.connect(self.trainClick)

        grid.addWidget(self.btnTrain,5,0)
        
            #single input result
        self.inp = QLabel('')
        self.inp.move(150,95)

        grid.addWidget(self.inp,4,1,1,4)

            #multiple input button
        self.btnMult = QPushButton('Multiple input')
        self.btnMult.resize(self.btnMult.sizeHint())
        self.btnMult.clicked.connect(self.multClick)

        grid.addWidget(self.btnMult,5,1)

            #multiple input result
        self.teMult = QTextEdit()
        self.teMult.setReadOnly(True)
        self.teMult.setLineWrapMode(QTextEdit.NoWrap)
        self.teMult.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

        sb = self.teMult.verticalScrollBar()
        sb.setValue(sb.maximum())

        grid.addWidget(self.teMult,6,0,30,5)

        

            #status bar
        #self.statusBar().showMessage('Ready')
        
        self.setLayout(grid)
        self.show()

    #set window at center
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #Multiple input event handler
    def multClick(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')

        self.setWindowTitle(fname)

        #parse file
        lines = open(fname).read().split("\n")

        ldata = []
        lres = []

        for line in lines[0:]:
            text = ""
            line = line.split(",")
            for data in line[:-1]:
                text += data
                text += ","
            ldata.append(text[:-1])
            lres.append(line[-1])

        QMessageBox.about(self, "Info", "%s \n %s" % (ldata, lres))
        
        result = ""
        try:
            for test in ldata[0:]:
                tres = clf.predict(np.array(np.fromstring(test, sep=",")))
                result += str(tres[0])
                if test != ldata[-1]:
                    result += "\n"
        except:
            pass

        outp = result.split("\n")
        result = ""
        for x in range(len(outp)):
            result += outp[x]
            result += " | "
            result += lres[x]
            result += " | "
            if outp[x] == lres[x]:
                result += "True"
            else:
                result += "False"
            result += "\n"

        self.teMult.setPlainText(result)
        

    #Train event handler
    def trainClick(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')

        self.setWindowTitle(fname)

        lines = open(fname).read().split("\n")

        ldata = []
        lres = []

        for line in lines[0:]:
            text = ""
            line = line.split(",")
            for data in line[:-1]:
                text += data
                text += ","
            ldata.append(text[:-1])
            lres.append(line[-1])

        """
        QMessageBox.about(self, "Info", "Data = %s/%s\nRes = %s/%s" % (
            ldata[0], len(ldata), lres[0], len(lres)))
        """

        #Init numpy arrays
        digit = np.array(np.fromstring(ldata[0], sep=","))

        #Parse digit
        for line in ldata[0:]:
            try:
                sample = np.fromstring(line, sep=",")
                digit = np.vstack((digit,sample))
            except:
                pass

        #Parse target
        t = np.array(lres)

        #Train
        x,y = digit,t
        clf.fit(x,y)
        QMessageBox.about(self, "Info", "Training completed!")

    #Solve event handler
    def solveClick(self):
        
        #DATA CONVERTER
        conv = ""
        for x in range(5):
            if x != 4:
                conv += self.boxType[x].currentText()
                conv += ","
                conv += self.boxName[x].currentText()
                conv += ","
            else:
                conv += self.boxType[x].currentText()
                conv += ","
                conv += self.boxName[x].currentText()
                
        conv = conv.replace("A","1")
        conv = conv.replace("J","11")
        conv = conv.replace("Q","12")
        conv = conv.replace("K","13")

        #TODO re-evaluate
        conv = conv.replace("♥","1")
        conv = conv.replace("♠","2")
        conv = conv.replace("♦","3")
        conv = conv.replace("♣","4")

        try:
            result = clf.predict(np.array(np.fromstring(conv, sep=",")))

            QMessageBox.about(self,"Info","%s | %s" %
                              (str(result),str(self.boxPredict.currentIndex())))
            
            if str(result[0]) == str(self.boxPredict.currentIndex()):
                self.inp.setText("True")
            else:
                self.inp.setText("False")
        except:
            pass
        
    #Close event handler
    def closeEvent(self, event):

        rep = QMessageBox.question(self, 'Confirmation',
            "Do you really want to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if rep == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():

    app = QApplication(sys.argv)
    pk = MainActivity()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
