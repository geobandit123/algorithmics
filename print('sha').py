#importing modules and widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QPushButton, QLabel, QLineEdit
 
#declaring constants
win_width, win_height = 200, 300
win_x, win_y = 200, 200
txt_title = "List of questions"
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
        self.btn_add = QPushButton("New question", self)
        self.lable_finish = QLabel()
        self.layout_main = QVBoxLayout()
        self.layout_main.addWidget(self.btn_begin, alignment = Qt.AlignCenter)


        self.layout_H1 = QHBoxLayout
        self.layout_H1.addWidget(self.btn_scad == QPushButton("Delete question", self))
        self.layout_H1.addWidget(self.btn_begin == QPushButton("Begin practice", self))
        self.layout_main.addWidget(self.btn_scad, alignment = Qt.AlignCenter)
        self.layout_main.addLayout(layout_H1)

 
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.btn_begin, alignment = Qt.AlignCenter)
        
        layoutH.addWidget(self.btn_scad, alignment = Qt.AlignCenter)

        my_Widget = QWidget()
        my_Widget.setLayout(layoutH)
        self.layout_main.addWidget(my_Widget)
 
        self.lable_finish.setText("Calculator Mockup")       
        self.setLayout(self.layout_main)
 
 
    def connects(self):
        # Nu need for the buttons to do something in this exercise/nothing to add here 
        pass
 
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