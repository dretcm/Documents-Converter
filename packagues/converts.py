from pdf2docx import Converter
from docx2pdf import convert
import os

class ConvertPW:
        def __init__(self,path,op):
                self.path = path
                self.op = op
                
        def go(self):
                if self.op == "pdf to word":
                        self.pw()
                elif self.op == "word to pdf":
                        self.wp()
                else:
                        pass
                
        def pw(self,begin=0,end=None):

                docx_file = self.path[:-4] + '.docx'

                cv =  Converter(self.path)
                cv.convert(docx_file, start=begin, end=end)
                cv.close()

        def wp(self):
                convert(self.path)

##a = ConvertPW(r'D:\Alexander\UCSP\caratula.docx',"word to pdf")
##a.go()

