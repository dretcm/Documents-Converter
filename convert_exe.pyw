import sys
from PyQt5.QtWidgets import (QWidget, QMessageBox, QApplication, QPushButton, QListWidget, QFileDialog, QLineEdit,QTabWidget)
from PyQt5.QtGui import QIcon

# converts

from packagues.image2pdf import ConvertImages2Pdf
from packagues.word2pdf_all import WordPdfConvert
                
class Manager(QWidget):
        def __init__(self):
                super().__init__()
                
                #self.setStyleSheet('background:black;')

                self.initUI()
                
                self.setWindowIcon(QIcon('images/yasu.ico'))
                self.setWindowTitle('Manager Yasu')
                self.resize(445,260)

                self.show()

        def initUI(self):
                tab1 = ConvertImages2Pdf()
                tab2 = WordPdfConvert()

                tabs = QTabWidget(self)
                tabs.addTab(tab1,'Images to pdf')
                tabs.addTab(tab2,'Word to pdf')
                tabs.setGeometry(15,10,425,240)
                #tabs.setStyleSheet('background:black;')
                
if __name__=='__main__':
        app = QApplication(sys.argv)
        aux = Manager()
        sys.exit(app.exec_())

