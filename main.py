from PyQt5 import uic, QtWidgets, QtGui
from bs4 import BeautifulSoup
import requests, lxml


def show_tags_classes():
    tela.cb_tag.clear()
    tela.cb_classes.clear()

    url = tela.lineEdit.text()
    sopa = BeautifulSoup(requests.get(url).text.encode('utf8'), 'lxml')

    tags = []

    # Pegando o nome das tags
    for i in sopa.find_all(True):
        tags.append(i.name)

    # Gravando apenas uma de cada
    tag_names = sorted(set(tags))

    # Adicionando no combobox
    for tag in tag_names:
        tela.cb_tag.addItem(tag)

    classes = []

    # Pegando o nome das classes
    for element in sopa.find_all(class_=True):
        classes.extend(element["class"])

    # Gravando apenas uma de cada
    class_names = sorted(set(classes))

    for clas in class_names:
        tela.cb_classes.addItem(clas)


def show_data():
    tela.textBrowser.clear()
    url = tela.lineEdit.text()
    sopa = BeautifulSoup(requests.get(url).text.encode('utf8'), 'lxml')

    texto = ''
    t = []
    t.clear()

    exec(f"for i in sopa.find_all('{str(tela.cb_tag.currentText())}', class_='{str(tela.cb_classes.currentText())}'): t.append(i.text.strip())")

    #print(t)

    for tt in t:
        texto += f'{tt}\n'

    tela.textBrowser.append(texto)


app = QtWidgets.QApplication([])

tela = uic.loadUi('UI/main_window.ui')

tela.bt_tags_classes.clicked.connect(show_tags_classes)
tela.bt_data.clicked.connect(show_data)

icone = QtGui.QIcon()
icone.addFile('img/icon.png')
app.setWindowIcon(icone)

tela.show()
app.exec()
