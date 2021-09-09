from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="petshop"
)


def FuncaoLogar():
    
    campoUsuario = login.lineUsuario.text()
    campoSenha = login.lineSenha.text()

    if ((campoUsuario == "vanessa" and campoSenha == "etec") or (campoUsuario == "lucio" and campoSenha == "etec")):
        home.show()
        login.close()
    else:
        QMessageBox.about(janelainserir, "OK!", "Senha ou usuário incorretos.")

def abreTelacadastrar():
    cadastrarUsuario.show()

programapetshop=QtWidgets.QApplication([]) 
login = uic.loadUi("login.ui") 
login.btnEntrar.clicked.connect(FuncaoLogar) 

home = uic.loadUi("Home.ui")


janelainserir = uic.loadUi("Petmensageminsere.ui")


login.show()
programapetshop.exec()
