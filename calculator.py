import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Attach widgets to window here
class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('My Calculator')
		screen_width = 320
		screen_height = 320
		self.setFixedSize(screen_width,screen_height) # find a more elegant solution

		self.btn_font = QFont("Arial", 12)
		self.result_font = QFont("Arial", 16)

		self.setLayout(qtw.QVBoxLayout())
		self.keypad()
		self.temp_nums = []
		self.fin_nums = []

		self.show()

	def keypad(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		# Buttons
		self.result_field = qtw.QLineEdit()
		self.result_field.setReadOnly(True) # prevents the user from typing in the text field
		self.result_field.setFont(self.result_font)

		btn_result = qtw.QPushButton('=', clicked = self.func_result)
		btn_clear = qtw.QPushButton('Clear', clicked = self.clear_calc)
		btn_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
		btn_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
		btn_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
		btn_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
		btn_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
		btn_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
		btn_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
		btn_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
		btn_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
		btn_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
		btn_period = qtw.QPushButton('.', clicked = lambda:self.num_press('.'))
		btn_plus = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
		btn_mins = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
		btn_mult = qtw.QPushButton('x', clicked = lambda:self.func_press('*'))
		btn_divd = qtw.QPushButton('÷', clicked = lambda:self.func_press('/'))

		# Setting the Button Font
		btn_result.setFont(self.btn_font)
		btn_clear.setFont(self.btn_font)
		btn_9.setFont(self.btn_font)
		btn_8.setFont(self.btn_font)
		btn_7.setFont(self.btn_font)
		btn_6.setFont(self.btn_font)
		btn_5.setFont(self.btn_font)
		btn_4.setFont(self.btn_font)
		btn_3.setFont(self.btn_font)
		btn_2.setFont(self.btn_font)
		btn_1.setFont(self.btn_font)
		btn_0.setFont(self.btn_font)
		btn_period.setFont(self.btn_font)
		btn_plus.setFont(self.btn_font)
		btn_mins.setFont(self.btn_font)
		btn_mult.setFont(self.btn_font)
		btn_divd.setFont(self.btn_font)

		# Adding the buttons to the layout
		container.layout().addWidget(self.result_field,0,0,1,4)
		container.layout().addWidget(btn_clear,1,0,1,3)
		container.layout().addWidget(btn_divd,1,3)
		container.layout().addWidget(btn_7,2,0)
		container.layout().addWidget(btn_8,2,1)
		container.layout().addWidget(btn_9,2,2)
		container.layout().addWidget(btn_mult,2,3)
		container.layout().addWidget(btn_4,3,0)
		container.layout().addWidget(btn_5,3,1)
		container.layout().addWidget(btn_6,3,2)
		container.layout().addWidget(btn_mins,3,3)
		container.layout().addWidget(btn_3,4,0)
		container.layout().addWidget(btn_2,4,1)
		container.layout().addWidget(btn_1,4,2)
		container.layout().addWidget(btn_plus,4,3)
		container.layout().addWidget(btn_0,5,0,1,2)
		container.layout().addWidget(btn_period,5,2)
		container.layout().addWidget(btn_result,5,3,1,1)
		self.layout().addWidget(container)

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
			self.func_result()
		# if event.key() == Qt.Key_Backspace: # doesn't work properly, deleted text comes back
		# 	text = self.result_field.text()
		# 	self.result_field.setText(text[:-1])
		if event.key() == Qt.Key_Delete:
			self.clear_calc()
		if event.key() == Qt.Key_9:
			self.num_press('9')
		if event.key() == Qt.Key_8:
			self.num_press('8')
		if event.key() == Qt.Key_7:
			self.num_press('7')
		if event.key() == Qt.Key_6:
			self.num_press('6')
		if event.key() == Qt.Key_5:
			self.num_press('5')
		if event.key() == Qt.Key_4:
			self.num_press('4')
		if event.key() == Qt.Key_3:
			self.num_press('3')
		if event.key() == Qt.Key_2:
			self.num_press('2')
		if event.key() == Qt.Key_1:
			self.num_press('1')
		if event.key() == Qt.Key_0:
			self.num_press('0')
		if event.key() == Qt.Key_Period:
			self.num_press('.')
		if event.key() == Qt.Key_Plus:
			self.func_press('+')
		if event.key() == Qt.Key_Minus:
			self.func_press('-')
		if event.key() == Qt.Key_Asterisk:
			self.func_press('*')
		if event.key() == Qt.Key_Slash:
			self.func_press('/')

	def num_press(self,key_number):
		self.temp_nums.append(key_number)
		temp_string = ''.join(self.temp_nums)
		if self.fin_nums:
			self.result_field.setText(''.join(self.fin_nums) + temp_string)
		else:
			self.result_field.setText(temp_string)

	def func_press(self,operator):
		temp_string = ''.join(self.temp_nums)
		self.fin_nums.append(temp_string)
		self.fin_nums.append(operator)
		self.temp_nums = []
		self.result_field.setText(''.join(self.fin_nums))

	def func_result(self):
		# Check to make sure the expression ends with a number first
		expression = self.result_field.text()
		if expression:
			last_char = expression[-1]
			if last_char in ['+', '-', '*', '/']:
				# show error message to the user
				QMessageBox.warning(self, "Error", "Expression cannot end with an operator.")
				return
			try:
				result = eval(expression)
				self.result_field.setText(str(result))
			except:
				QMessageBox.warning(self, "Error", "Invalid expression.")
			else: # This part evaluates the expression when it's safe to do so.
				fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
				result_string = eval(fin_string)
				fin_string += ' = '
				fin_string += str(result_string)
				self.result_field.setText(fin_string)

	def clear_calc(self):
		self.result_field.clear()
		self.temp_nums = []
		self.fin_nums = []

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_() # The underscore prevents naming conflicts with python