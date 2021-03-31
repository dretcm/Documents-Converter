import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtGui import QIcon

class Dialogs(QWidget):
        def __init__(self):
                super().__init__()

        @staticmethod
        def dialog(title='Error!', text = 'There was a mistake.', icon=QMessageBox.Warning):
                
                msgBox = QMessageBox()
                msgBox.setWindowIcon(QIcon('images\\yasu.ico'))
                if icon:
                        msgBox.setIcon(icon)
                else:
                        msgBox.setIcon(QMessageBox.Information)   
                msgBox.setText(text)
                msgBox.setWindowTitle(title)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                
if __name__=='__main__':
        app = QApplication(sys.argv)
        aux = Dialogs.dialog()
        sys.exit(app.exec_())
        
