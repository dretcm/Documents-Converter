import sys, os
from PyPDF2 import PdfFileMerger
from PyQt5.QtWidgets import (QWidget, QMessageBox, QApplication, QPushButton, QListWidget, QFileDialog, QLineEdit,QLabel)
from packagues.dialog_app import Dialogs
from PyQt5.QtGui import QIcon

class MergePdf(QWidget):
        def __init__(self):
                super().__init__()
                self.output = 'output_pdf'
                self.data_path = {}

                self.initUI()
                
                self.setWindowTitle('PDF Merge')
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
                self.data.setDragDropMode(self.data.InternalMove)

                # functions:

                self.button.clicked.connect(self.run_merge)
                self.files.clicked.connect(self.openfile)
                self.clear_button.clicked.connect(self.clear)
                
        def clear(self):
                self.data.clear()
                self.data_path.clear()

        def merge(self):
                folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
                outpath = os.path.join(folder,self.output + '.pdf')

                merger = PdfFileMerger()

                for i in range(self.data.count()):
                        merger.append(self.data_path[self.data.item(i).text()])
                        
                merger.write(outpath)
                merger.close()
                
        def run_merge(self):
                try:
                        self.output = self.entry.text()
                        self.merge()
                        Dialogs.dialog(title='SUCCESSFULL',text=f'* The process was successfull.\n* {self.output}.pdf',icon=False)
                        
                except Exception as e:
                        Dialogs.dialog(text='There was a mistake with the path or the file.')
                        print(e)

        def openfile(self):
                options = QFileDialog.Options()
                filenames, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;PDF's (*.pdf)", options=options)
                if filenames:
                        for filename in filenames:
                                file_name = str(os.path.basename(filename))
                                self.data_path[file_name] = filename
                                self.data.addItem(file_name)
                    

if __name__=='__main__':
        app = QApplication(sys.argv)
        exe = MergePdf()
        sys.exit(app.exec_())

