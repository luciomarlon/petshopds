from PyQt5 import uic,  QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "petshop")



def CadastraPetcliente():

   
    campoNomepet = cadastrameupet.txtNomepet.text().upper()
   
    

    cursor = banco.cursor()
    #comando_SQL = "INSERT INTO teste (raca) VALUES ('teste')"
    dadospet = (str(campoNomepet))
    
    
    try:
        cursor.execute("INSERT INTO teste (raca) VALUES ('s')", dadospet)
        banco.commit()        
        campoNomepet = cadastrameupet.txtNomepet.setText("")
      
        QMessageBox.about(janelainserir, "OK!", "Pet cadastrado com sucesso.")
    except:
        QMessageBox.about(janelainserir, "OK!", "Erro a cadastrar Pet.")  
 
 




petshopcliente = QtWidgets.QApplication([])
cadastrameupet = uic.loadUi("teste.ui")

cadastrameupet.btnAddPet.clicked.connect(CadastraPetcliente)




janelainserir = uic.loadUi("Petmensageminsere.ui")


cadastrameupet.show()
petshopcliente.exec()
