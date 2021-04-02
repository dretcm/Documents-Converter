import sys
from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QApplication, QPushButton, QListWidget, QFileDialog, QLineEdit,QTabWidget)
from PyQt5.QtGui import QIcon

# converts

from packagues.image2pdf import ConvertImages2Pdf
from packagues.word2pdf_all import WordPdfConvert
from packagues.pdf_merge import MergePdf
                
class Manager(QMainWindow):
        def __init__(self):
                super().__init__()

                self.initUI()
                
                self.setWindowIcon(QIcon('images/yasu.ico'))
                self.setWindowTitle('Manager Yasu')
                self.resize(445,260)

                self.show()

        def initUI(self):
                tab1 = ConvertImages2Pdf()
                tab2 = WordPdfConvert()
                tab3 = MergePdf()

                tabs = QTabWidget(self)
                tabs.addTab(tab1,'Images to pdf')
                tabs.addTab(tab2,'Word to pdf')
                tabs.addTab(tab3,'Pdf Merge')
                tabs.setGeometry(15,10,425,240)
                
if __name__=='__main__':
        app = QApplication(sys.argv)
        aux = Manager()
        sys.exit(app.exec_())

