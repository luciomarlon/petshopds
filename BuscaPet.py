from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "petshop")


def Cadastrar():
    cadastrameupet.show()    
    #cadastrameupet.ComboRaca.clear() 



def CadatraPetcliente():

    campoNome    = cadastrameupet.ComboNome.currentText().upper()   
    campoNomepet = cadastrameupet.txtNomepet.text().upper()
    campoIdade   = cadastrameupet.txtIdade.text().upper().replace(",",".")
    campoEspecie = cadastrameupet.ComboEspecie.currentText()
    campoPorte   = cadastrameupet.ComboPorte.currentText()
    campoRaca    = cadastrameupet.ComboRaca.currentText().upper()    
    campoPeso    = cadastrameupet.txtPeso.text().replace(",",".")
    
    if (campoNome == ''):
            QMessageBox.about(janelainserir, "OK!", "Preencha o Nome do Responsável")

    elif (campoNomepet == ''):
            QMessageBox.about(janelainserir, "OK!", "Preencha o Nome do Pet")
            
    elif(campoNome!= '' and campoNomepet != ''):
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO pet (nomepet, idade, especie, porte, raca, peso, cliente) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        dadospet = (str(campoNomepet), str(campoIdade), str(campoEspecie), str(campoPorte), str(campoRaca), str(campoPeso), str(campoNome))
        try:
            cursor.execute(comando_SQL, dadospet)        
        
            banco.commit()        
            
            campoIdade   = cadastrameupet.txtIdade.setText("")        
            campoPeso    = cadastrameupet.txtPeso.setText("")
            QMessageBox.about(janelainserir, "OK!", "Pet cadastrado com sucesso.")
            
            linhapets = petgeral.tabelaPetGeralporCliente.reset()
            ListarBuscarPet()
        except:
            QMessageBox.about(janelainserir, "OK!", "Erro a cadastrar Pet.") 

def BuscarRaca():

    campoNome    = cadastrameupet.ComboNome.addItems([""])
    cursor = banco.cursor()
    SQL_CLIENTE = "SELECT nome FROM cliente ORDER by nome"
    cursor.execute(SQL_CLIENTE)   
    listaclientes = cursor.fetchall()
    for clientes in listaclientes:
        cadastrameupet.ComboNome.addItem(clientes[0])
  

    campoEspecie = cadastrameupet.ComboEspecie.addItems([""])
    if(campoEspecie == cadastrameupet.ComboEspecie.addItems(["GATO"])):

        cursor = banco.cursor()      
        comando_SQL = "SELECT racagato FROM categoriagato ORDER by racagato"   
        cursor.execute(comando_SQL)
        listacategoria = cursor.fetchall()

        for categorias in listacategoria:
            cadastrameupet.ComboRaca.addItem(categorias[0])

    if(campoEspecie == cadastrameupet.ComboEspecie.addItems(["CACHORRO"])):
        
        cursor = banco.cursor()
        comando_SQL = "SELECT racacachorro FROM categoriacachorro ORDER by racacachorro"           
        cursor.execute(comando_SQL)
        listacategoria = cursor.fetchall()    

        for categorias in listacategoria:
            cadastrameupet.ComboRaca.addItem(categorias[0])     

def ExcluirPets():

    linhapets = - 1
    
    linhapets = petgeral.tabelaPetGeralporCliente.currentRow()

    pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir?', QMessageBox.Yes | QMessageBox.No)
    
    if(linhapets < 0):
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

    elif (pergunta == QMessageBox.Yes):
        
        linhapets = petgeral.tabelaPetGeralporCliente.currentRow()
        petgeral.tabelaPetGeralporCliente.removeRow(linhapets)  
   
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM pet"
        cursor.execute(comando_SQL)
        listapetsporcliente = cursor.fetchall()
        valorId = listapetsporcliente[linhapets][0]
        cursor.execute("DELETE FROM pet WHERE id_pet ="+ str(valorId))
        banco.commit()
        QMessageBox.about(janelainserir, "OK!", "Pet deletado com sucesso.")
        
        
        linhapets = petgeral.tabelaPetGeralporCliente.reset()
        ListarBuscarPet()        
    
    elif (pergunta == QMessageBox.No):
        ListarBuscarPet()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR") 


def ListarBuscarPet(): 

        
        linhapets = petgeral.tabelaPetGeralporCliente.reset()
       
        cursor = banco.cursor()
        comando_SQL = "SELECT nomepet, idade, especie, porte, raca, peso, cliente FROM pet"
        cursor.execute(comando_SQL)
        listapetsporcliente = cursor.fetchall()        

        petgeral.tabelaPetGeralporCliente.setRowCount(len(listapetsporcliente))
        petgeral.tabelaPetGeralporCliente.setColumnCount(7)

        for linhas in range(0, len(listapetsporcliente)):
            for colunas in range(0, 7):
                petgeral.tabelaPetGeralporCliente.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listapetsporcliente[linhas][colunas])))

        
'''
def BuscarPet():
   
        campoNomepet = petgeral.txtNomepet.text()
      
        cursor = banco.cursor()
        comando_SQL = "SELECT nomepet, idade, especie, porte, raca, peso, cpfcliente FROM pet WHERE nomepet like '%"+str(campoNomepet)+"%'"
        #comando_SQL = "SELECT * FROM pet where nomepet like '%CA%'"
                
        cursor.execute(comando_SQL)
        listapetsporcliente = cursor.fetchall()        

        petgeral.tabelaPetGeralporCliente.setRowCount(len(listapetsporcliente))
        petgeral.tabelaPetGeralporCliente.setColumnCount(7)

        for linhas in range(0, len(listapetsporcliente)):
            for colunas in range(0, 7):
                petgeral.tabelaPetGeralporCliente.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listapetsporcliente[linhas][colunas])))

'''
def AlterarPet():

    cursor = banco.cursor()
    comando_SQL = "SELECT id_pet FROM pet"
    cursor.execute(comando_SQL)
    listarPetGeral = cursor.fetchall()
    for linhas in range(0, len(listarPetGeral)):
        valorId      = listarPetGeral[linhas][0]        
        campoNomepet = petgeral.tabelaPetGeralporCliente.item(linhas, 0).text().upper()
        campoIdade   = petgeral.tabelaPetGeralporCliente.item(linhas, 1).text().replace(",",".")
        campoEspecie = petgeral.tabelaPetGeralporCliente.item(linhas, 2).text().upper()
        campoPorte   = petgeral.tabelaPetGeralporCliente.item(linhas, 3).text().upper()
        campoRaca    = petgeral.tabelaPetGeralporCliente.item(linhas, 4).text().upper()
        campoPeso    = petgeral.tabelaPetGeralporCliente.item(linhas, 5).text().replace(",",".")
        campoCliente = petgeral.tabelaPetGeralporCliente.item(linhas, 6).text().upper()
        
        cursor.execute("UPDATE pet SET "                        
                        "nomepet = '" + str(campoNomepet) + "', "
                        "idade = '" + str(campoIdade) + "', "
                        "especie = '" + str(campoEspecie) + "', "
                        "porte = '" + str(campoPorte) + "', "
                        "raca = '" + str(campoRaca) + "', "                        
                        "peso = '" + str(campoPeso)+"', "
                        "cliente = '" + str(campoCliente)+"' WHERE id_pet = " + str(valorId))
                        
        banco.commit()

def gerarPDFBuscaPet():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM pet ORDER BY nomepet"
    cursor.execute(comando_SQL)
    pet_lidos = cursor.fetchall()

    y = 0
    pdf = canvas.Canvas("lista_pet.pdf")
    pdf.setFont("Times-Bold", 12)
    pdf.drawString(200, 800, "Lista de Pets")

    pdf.setFont("Times-Bold", 10)
    #pdf.drawString(10, 750, "ID")
    pdf.drawString(10, 750, "NOMEPET")
    pdf.drawString(110, 750, "IDADE")
    pdf.drawString(210, 750, "ESPECIE")
    pdf.drawString(310, 750, "PORTE")
    pdf.drawString(410, 750, "RACA")
    pdf.drawString(510, 750, "PESO")
    #pdf.drawString(610, 750, "CPFCLIENTE")
    #pdf.drawString(710, 750, "PET_CLIENTE")

    for i in range(0, len(pet_lidos)):
        y = y + 20
        pdf.drawString(10, 750 - y, str(pet_lidos[i][1]))
        pdf.drawString(110, 750 - y, str(pet_lidos[i][2]))
        pdf.drawString(210, 750 - y, str(pet_lidos[i][3]))
        pdf.drawString(310, 750 - y, str(pet_lidos[i][4]))
        pdf.drawString(410, 750 - y, str(pet_lidos[i][5]))
        pdf.drawString(510, 750 - y, str(pet_lidos[i][6]))
        #pdf.drawString(610, 750 - y, str(pet_lidos[i][7]))
        #pdf.drawString(710, 750 - y, str(pet_lidos[i][8]))
        #pdf.drawString(810, 750 - y, str(pet_lidos[i][9]))

    pdf.save()
    QMessageBox.about(janelainserir, "OK!", "PDF gerado com sucesso.")

petshopcliente = QtWidgets.QApplication([])
petgeral = uic.loadUi("BuscaPet.ui")
petgeral.btnListarPets.clicked.connect(ListarBuscarPet)
petgeral.btnAddPet.clicked.connect(Cadastrar)
petgeral.btnExcluirpet.clicked.connect(ExcluirPets)
petgeral.btnAlterarPet.clicked.connect(AlterarPet)
petgeral.btnAddPet.clicked.connect(BuscarRaca)
petgeral.btnPdfPet.clicked.connect(gerarPDFBuscaPet)
#petgeral.btnBuscar.clicked.connect(BuscarPet)


cadastrameupet = uic.loadUi("ClienteAddPet.ui")
cadastrameupet.btnCadastrarpet.clicked.connect(CadatraPetcliente)
#cadastrameupet.ComboEspecie.addItems(["GATO","CACHORRO"])

cadastrameupet.ComboPorte.addItems(["P","M","G"])
cadastrameupet.ComboRaca.addItems([""])

janelainserir = uic.loadUi("Petmensageminsere.ui")


petgeral.show()
petshopcliente.exec()
