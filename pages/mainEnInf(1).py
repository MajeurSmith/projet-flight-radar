from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QMessageBox, QListWidgetItem
#from PyQt5.QtGui import QPixmap, QIcon #  QPixmap est utile pour les images
from PyQt5.uic import loadUi
import os
#import ctypes

localPath = os.path.dirname(os.path.abspath(__file__))

class mainPage(QMainWindow):
    def __init__(self):
        super(mainPage, self).__init__()
        self.setWindowTitle("mainPage")
        self.windowContent=QMainWindow()
        self.setCentralWidget(self.windowContent)
        loadUi(localPath + "/Carte de France(1).ui",self.windowContent)

"""
        self.windowContent.lineEditNom.setPlaceholderText("Nom")
        self.windowContent.lineEditEmail.setPlaceholderText("Email")
        self.windowContent.textEdit.setPlaceholderText("Commentaire supplémentaire")
        self.windowContent.radioButtonPage1.clicked.connect(self.ouverturePage1)
        self.windowContent.radioButtonPage2.clicked.connect(self.ouverturePage2)

    def ouverturePage1(self):
        self.fermeture()
        self.page=Page1()
        self.page.setFixedSize(450,555)
        self.page.show()

    def ouverturePage2(self):
        self.fermeture()
        self.page=Page2()
        self.page.setFixedSize(450,555)
        self.page.show()

    def fermeture(self):
        self.close()

class Page1(QMainWindow):
    def __init__(self):
        super(Page1, self).__init__()
        self.setWindowTitle("Page1")
        self.windowContent=QWidget()
        self.setCentralWidget(self.windowContent)
        loadUi(localPath + "/page1.ui",self.windowContent)
        
    def fermeture(self):
        self.close()
        
class Page2(QMainWindow):
    def __init__(self):
        super(Page2, self).__init__()
        self.setWindowTitle("Page2")
        self.windowContent=QWidget()
        self.setCentralWidget(self.windowContent)
        loadUi(localPath + "/page2.ui",self.windowContent)

    def fermeture(self):
        self.close()

"""
if __name__=="__main__":  
    os.system("cls")
    app = QApplication([])
    page=mainPage()
    page.setFixedSize(1172,682)
    page.show()
    app.exec_()
    

    