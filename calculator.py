#import area
from PyQt6.QtWidgets import QLabel, QGridLayout, QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget ,QLineEdit, QComboBox



#ceo = ClassName()
app = QApplication([])

#ceo = ClassName()
btn1 = QPushButton('1')
btn2 = QPushButton('2') 
btnplus = QPushButton('+')
btnequal = QPushButton('=')

num1 = QLineEdit()
num2 = QLineEdit()

result = QLabel("hey") #global variable


#ceo = ClassName()
operator = QComboBox() # +, -, /, *
#ceo.member(actarg1,actarg2)
operator.addItems(["+",'-',"*",'/'])

window = QWidget()
layout = QGridLayout()
#ceo.method()
layout.addWidget(num1,0,0)
layout.addWidget(operator,0,1)
layout.addWidget(num2,0,3)
layout.addWidget(btnequal,1,0)
layout.addWidget(result,1,1)
window.setLayout(layout)

def aashish():
    print(num1.text())
    print(operator.currentText())
    print(num2.text())
    n1 = float(num1.text())
    op = operator.currentText()
    n2 = float(num2.text())

    print(n1)
    if op == '-':
       rst = n1-n2
       print(f'{n1} {op} {n2} = {rst}')
       result.setText(str(rst))
    pass
#widgwt.signal.connect(slot_function)
btnequal.clicked.connect(aashish)

window.show()
app.exec()