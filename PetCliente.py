from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "petshop"
)

def CadatraPetcliente():

    campoCpf = cadastrameupet.txtCpf.text()
    campoNomepet = cadastrameupet.txtNomepet.text().upper()
    campoIdade   = cadastrameupet.txtIdade.text().upper().replace(",",".")
    campoEspecie = cadastrameupet.ComboEspecie.currentText()
    campoPorte   = cadastrameupet.ComboPorte.currentText()
    campoRaca    = cadastrameupet.ComboRaca.currentText()    
    campoPeso    = cadastrameupet.txtPeso.text().replace(",",".")
    if (campoCpf == ''):
            QMessageBox.about(janelainserir, "OK!", "Preencha o CPF do Responsável")

    elif (campoNomepet == ''):
            QMessageBox.about(janelainserir, "OK!", "Preencha o Nome do Pet")
            
    elif(campoNomepet!= '' and campoCpf != ''):
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO pet (nomepet, idade, especie, porte, raca, peso, cpfcliente) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        dadospet = (str(campoNomepet), str(campoIdade), str(campoEspecie), str(campoPorte), str(campoRaca), str(campoPeso), str(campoCpf))
        try:
            cursor.execute(comando_SQL, dadospet)
        
        
            banco.commit()        
            campoNomepet = cadastrameupet.txtNomepet.setText("")
            campoIdade   = cadastrameupet.txtIdade.setText("")        
            campoPeso    = cadastrameupet.txtPeso.setText("")
            QMessageBox.about(janelainserir, "OK!", "Pet cadastrado com sucesso.")
            linhapets = cadastrameupet.tabelaPetGeralporCliente.reset()
            ListarBuscarPet()
        except:
            QMessageBox.about(janelainserir, "OK!", "Erro a cadastrar Pet.")  


def BuscarNomeAgendamento():  
    cadastrameupet.ComboRaca.load()     

    cursor = banco.cursor()
    comando_SQL = "SELECT racagato FROM categoriagato"   
    cursor.execute(comando_SQL)
    listacategoria = cursor.fetchall()
    

    for categorias in listacategoria:
            cadastrameupet.ComboRaca.addItem(categorias[0])


petshopcliente = QtWidgets.QApplication([])
cadastrameupet = uic.loadUi("PetCliente.ui")
cadastrameupet.btnCadastrarpet.clicked.connect(CadatraPetcliente)
cadastrameupet.ComboEspecie.addItems(["G","C"])
cadastrameupet.ComboPorte.addItems(["P","M","G"])
cadastrameupet.ComboRaca.addItems([""])

janelainserir = uic.loadUi("Petmensageminsere.ui")


cadastrameupet.show()
petshopcliente.exec()
