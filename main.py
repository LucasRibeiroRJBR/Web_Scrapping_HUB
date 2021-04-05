from PyQt5 import uic, QtWidgets, QtGui
from bs4 import BeautifulSoup
import requests, lxml


def foo():
    tela.cb_tag.clear()

    url = tela.lineEdit.text()
    sopa = BeautifulSoup(requests.get(url).text.encode('utf8'), 'lxml')

    tags = []

    for i in sopa.find_all(True):
        tags.append(i.name)

    tag_names = set(tags)

    for tag in tag_names:
        tela.cb_tag.addItem(tag)


app = QtWidgets.QApplication([])

tela = uic.loadUi('UI/main_window.ui')

tela.pushButton.clicked.connect(foo)

tela.show()
app.exec()
