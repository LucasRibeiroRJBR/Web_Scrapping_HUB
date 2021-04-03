from PyQt5 import uic, QtWidget, QtGui

app = QtWidget.QApplication([])

tela = uic.loadUi('UI/main_window.ui')

tela.show()
app.exec_()
