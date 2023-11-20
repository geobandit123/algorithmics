#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget
 
#declaring constants
win_width, win_height = 800, 300
win_x, win_y = 200, 200
txt_title = "Sending text"
txt_line = "Entry field"
 
class MainWindow(QWidget):
    value = 0
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        # creating and customizing the graphical elements:
        self.initUI()
        #connects the elements
        self.connects()
 
        #determines how the window will look (text, size, location)
        self.set_appear()
 
        # start:
        self.show()
 
    def initUI(self):
        ''' creates graphical elements '''
        self.my_list = QListWidget()
        self.lable_intrebare = QLabel("Intrebare")
        self.lable_raspunsC = QLabel('Raspuns correct')
        self.lable_raspunsG1 = QLabel('Raspuns gresit 1')
        self.lable_raspunsG2 = QLabel('Raspuns gresit 2')
        self.lable_raspunsG3 = QLabel('Raspuns gresit 3')
 
        self.line_intrebare = QLineEdit()
        self.line_intrebareC = QLineEdit()
        self.line_intrebareG1 = QLineEdit()
        self.line_intrebareG2 = QLineEdit()
        self.line_intrebareG3 = QLineEdit()
 
        self.btn_question = QPushButton("New Question", self)
        self.btn_delet = QPushButton("Delete Question", self)
        self.btn_begin = QPushButton("Begin practice", self)
        self.layout_main = QVBoxLayout()
 
 
 
 
 
        layoutHB = QHBoxLayout()
        layoutHB.addWidget(self.btn_delet, alignment = Qt.AlignCenter) 
        layoutHB.addWidget(self.btn_begin, alignment = Qt.AlignCenter)  
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()
        my_elements = [self.lable_intrebare, self.lable_raspunsC, self.lable_raspunsG1, self.lable_raspunsG2, self.lable_raspunsG3]
        for elemet in my_elements:
            layoutV1.addWidget(elemet, alignment = Qt.AlignCenter)
 
        layoutV2.addWidget(self.line_intrebare, alignment = Qt.AlignCenter)
        layoutV2.addWidget(self.line_intrebareC, alignment = Qt.AlignCenter)
        layoutV2.addWidget(self.line_intrebareG1, alignment = Qt.AlignCenter)
        layoutV2.addWidget(self.line_intrebareG2, alignment = Qt.AlignCenter)
        layoutV2.addWidget(self.line_intrebareG3, alignment = Qt.AlignCenter)
        layoutHB2 = QHBoxLayout()
        layoutHB2.addLayout(layoutV1)
        layoutHB2.addLayout(layoutV2)
 
        layoutHBB = QHBoxLayout() 
        layoutHBB.addWidget(self.my_list)     
        layoutHBB.addLayout(layoutHB2)
 
        self.layout_main.addLayout(layoutHBB)
        self.layout_main.addLayout(layoutHB)
        self.layout_main.addWidget(self.btn_question, alignment = Qt.AlignCenter)
 
        self.setLayout(self.layout_main)
 
    def addNewQuestion(self):
        question = self.line_intrebare.text()
        answer = self.line_intrebareC.text()
        answerg1 = self.line_intrebareG1.text()
        answerg2 = self.line_intrebareG2.text() 
        answerg3 = self.line_intrebareG3.text() 
 
 
    def connects(self):
        self.btn_question.clicked.connect(self.addNewQuestion)
 
 
    ''' determines how the window will look (text, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
 
def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()
 
main()
