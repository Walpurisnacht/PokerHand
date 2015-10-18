# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore

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
            self.boxType[x].addItem('♦')
            self.boxType[x].addItem('♥')
            self.boxType[x].addItem('♣')
            self.boxType[x].addItem('♠')
            

            #layout
        grid = QGridLayout()

        for x in range(5):
            grid.addWidget(boxLabel[x],1,x)
            grid.addWidget(self.boxName[x],2,x)
            grid.addWidget(self.boxType[x],3,x)

        grid.setContentsMargins(60,20,50,400)

        #feature
            #solve button
        self.btnSolve = QPushButton('Solve',self)
        self.btnSolve.resize(self.btnSolve.sizeHint())
        self.btnSolve.clicked.connect(self.solveClick)

        grid.addWidget(self.btnSolve,4,0)
        
            #input viewer
        self.inp = QLabel('')
        self.inp.move(150,95)

        grid.addWidget(self.inp,4,1,1,4)
        
        self.setLayout(grid)
        self.show()

    #set window at center
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #Solve event handler
    def solveClick(self):
        text = ""
        for x in range(5):
            if x != 4:
                text += self.boxName[x].currentText()
                text += self.boxType[x].currentText()
                text += " | "
            else:
                text += self.boxName[x].currentText()
                text += self.boxType[x].currentText()

        """
        DATA CONVERTER
        text = text.replace("A","1")
        text = text.replace("J","11")
        text = text.replace("Q","12")
        text = text.replace("K","13")

        #TODO re-evaluate
        text = text.replace("♦","1")
        text = text.replace("♥","2")
        text = text.replace("♣","3")
        text = text.replace("♠","4")
        """

        self.inp.setText(text)
        
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