import sys,os
from packagues.converts import ConvertPW
from PyQt5.QtWidgets import (QWidget, QApplication,QLineEdit, QLabel,QPushButton, QComboBox, QFileDialog)
from PyQt5.QtGui import QIcon
from packagues.dialog_app import Dialogs

class WordPdfConvert(QWidget):
        def __init__(self):
                super().__init__()
                self.path_file = ''
                #self.setStyleSheet('background:white;')
                self.initUI()
                
                self.setWindowTitle('Convert(pdf,word)')
                self.resize(400,105)

                self.show()

        def initUI(self):

                self.menu = QPushButton(QIcon('images\\file.png'),'Files',self)
                self.menu.setGeometry(5, 5, 50, 25)
                
                self.entry = QLineEdit(self)
                self.entry.setStyleSheet('font: 12pt "Arial";')
                self.entry.setReadOnly(True)
                self.entry.setGeometry(5, 35, 250, 20)
                
                self.button = QPushButton('Convert', self)
                self.button.setStyleSheet('font: 10pt "Arial";')
                self.button.setGeometry(270, 35, 100, 50)
                
                self.option = QComboBox(self)
                self.option.setStyleSheet('font: 12pt "Arial";')
                self.option.setGeometry(5, 65, 250, 25)

                options = ['pdf to word', 'word to pdf']
                for op in options:
                        self.option.addItem(op)

                # functions:

                self.button.clicked.connect(self.run_convert)
                self.menu.clicked.connect(self.openfile)

                
        def run_convert(self):
                try:
                        option = str(self.option.currentText())
                        path = self.path_file
                        
                        cv = ConvertPW(path, option)
                        cv.go()

                        self.entry.clear()
                        
                        Dialogs.dialog(title='SUCCESSFULL',text='* The convertion was succesfull.',icon=False)
                        
                except Exception as e:
                        Dialogs.dialog(text='There was a mistake with the path or the file.')
                        print(e)

        def openfile(self):
                options = QFileDialog.Options()
                filename, aux = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Pdf Files (*.pdf);;Word Files (*.docx)", options=options)

                if filename:
                    self.path_file = filename
                    self.entry.setText(str(os.path.basename(filename)))

if __name__ == '__main__':
        app = QApplication(sys.argv)
        exe = WordPdfConvert()
        sys.exit(app.exec_())

