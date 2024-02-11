from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, 
                             QPushButton, QLineEdit, QLabel, QHBoxLayout) 
 
app = QApplication([]) 
window = QWidget() 
line = QLineEdit() 
label = QLabel('Результат:') 
label2 = QLabel('') 
 
tab1 = QWidget() 
button = QPushButton('1') 
button2 = QPushButton('2') 
button3 = QPushButton('3') 
button4 = QPushButton('+') 
button5 = QPushButton('4') 
button6 = QPushButton('5') 
button7 = QPushButton('6') 
button8 = QPushButton('-') 
button9 = QPushButton('7') 
button10 = QPushButton('8') 
button11 = QPushButton('9') 
button12 = QPushButton('*') 
button13 = QPushButton('0') 
button14 = QPushButton('/') 
button15 = QPushButton('clear') 
button16 = QPushButton('result') 
 
h = QHBoxLayout() 
h.addWidget(button) 
h.addWidget(button2) 
h.addWidget(button3) 
h.addWidget(button4) 
 
h1 = QHBoxLayout() 
h1.addWidget(button5) 
h1.addWidget(button6) 
h1.addWidget(button7) 
h1.addWidget(button8) 
 
h2 = QHBoxLayout() 
h2.addWidget(button9) 
h2.addWidget(button10) 
h2.addWidget(button11) 
h2.addWidget(button12) 
 
h3 = QHBoxLayout() 
h3.addWidget(button13) 
h3.addWidget(button14) 
h3.addWidget(button15) 
h3.addWidget(button16) 
 
v = QVBoxLayout() 
v.addWidget(line) 
v.addLayout(h) 
v.addLayout(h1) 
v.addLayout(h2) 
v.addLayout(h3) 
v.addWidget(label) 
v.addWidget(label2)  
 
window.setLayout(v) 
 
def on_button_click(): 
    button = window.sender() 
    text = button.text() 
    line.insert(text) 
 
def calculate_result():
    try:
        result = eval(line.text()) 
        label2.setText(str(result)) 
    except as e:
        label2.setText('Помилка: ' + str(e))

def clear_line():
    line.clear()

window.show() 
app.exec_()

