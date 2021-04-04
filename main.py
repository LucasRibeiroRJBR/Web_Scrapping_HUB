from PyQt5 import uic, QtWidgets, QtGui
from bs4 import BeautifulSoup
import requests


def foo():
    url = tela.lineEdit.text()
    print(url)
    sopa = BeautifulSoup(requests.get(url).text.encode('utf8'), 'html.parser')




app = QtWidgets.QApplication([])

tela = uic.loadUi('UI/main_window.ui')

tela.pushButton.clicked.connect(foo)

tela.show()
app.exec_()
