from PIL import Image
import sys, os
from PyQt5.QtWidgets import (QWidget, QMessageBox, QApplication, QPushButton, QListWidget, QFileDialog, QLineEdit,QLabel)
from PyQt5.QtGui import QIcon
from packagues.dialog_app import Dialogs

class ConvertImages2Pdf(QWidget):
        def __init__(self):
                super().__init__()
                self.output = 'output'
                self.data_path = []

                #self.setStyleSheet('background:white;')

                self.initUI()
                
                self.setWindowTitle('IMGS TO PDF')
                self.resize(420,220)

                self.show()

        def initUI(self):
                self.files = QPushButton(QIcon('images\\file.png'),'Files',self)
                self.files.setGeometry(5, 5, 50, 50)
                self.files.setStyleSheet('font: 10pt "Arial";')
                
                self.button = QPushButton('Run', self)
                self.button.setStyleSheet('font: 10pt "Arial";')
                self.button.setGeometry(70, 5, 50, 50)

                self.clear_button = QPushButton('Clean', self)
                self.clear_button.setStyleSheet('font: 10pt "Arial";')
                self.clear_button.setGeometry(135, 5, 50, 50)

                self.label = QLabel('Name pdf: ',self)
                self.label.setStyleSheet('font: 12pt "Arial";')
                self.label.setGeometry(200,5,200,20)
                
                self.entry = QLineEdit(self)
                self.entry.setStyleSheet('font: 12pt "Arial";')
                self.entry.setText(self.output)
                self.entry.setGeometry(200, 30, 200, 20)
                
                self.data = QListWidget(self)
                self.data.setStyleSheet('font: 12pt "Arial";')
                self.data.setGeometry(5, 60, 410, 150)

                # functions:

                self.button.clicked.connect(self.run_convert)
                self.files.clicked.connect(self.openfile)
                self.clear_button.clicked.connect(self.clear)
                
        def clear(self):
                self.data.clear()
                self.data_path.clear()

        def convert(self,labels):
                folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
                path = os.path.join(folder,self.output + '.pdf')
                imgs = []

                for l in labels[1:]:
                        img = Image.open(l).convert('RGB')
                        imgs.append(img)
                        
                img = Image.open(labels[0]).convert('RGB')
                img.save(path,save_all=True, append_images=imgs)
                img.close()
                
        def run_convert(self):
                try:
                        self.output = self.entry.text()
                        self.convert(self.data_path)
                        Dialogs.dialog(title='SUCCESSFULL',text=f'* The process was successfull.\n* {self.output}.pdf',icon=False)
                        
                except Exception as e:
                        Dialogs.dialog(text='There was a mistake with the path or the file.')
                        print(e)

        def openfile(self):
                options = QFileDialog.Options()
                filenames, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Images jpg (*.jpg);;Images PNG (*.png)", options=options)
                print(filenames)
                if filenames:
                        for filename in filenames:
                                self.data_path.append(filename)
                                self.data.addItem(str(os.path.basename(filename)))
                    

if __name__=='__main__':
        app = QApplication(sys.argv)
        exe = ConvertImages2Pdf()
        sys.exit(app.exec_())

