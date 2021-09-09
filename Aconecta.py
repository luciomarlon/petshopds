from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "petshop")

cursor = banco.cursor()
comando_SQL = "SELECT nome FROM funcionario ORDER by nome"   
cursor.execute(comando_SQL)
listarprofissional = cursor.fetchall()
    

for funcionario in listarprofissional:
    print(funcionario)
    #ComboProfissional.addItem(funcionario[0])
