from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "petshop")

def Cadastrarcliente():
    
    campoNome           = cliente.txtNome.text().upper()
    campoRg             = cliente.txtRg.text().upper()
    campoCpf            = cliente.txtCpf.text()
    campoCelular        = cliente.txtCelular.text()
    campoFixo           = cliente.txtFixo.text()
    campoLogradouro     = cliente.txtLogradouro.text().upper()
    campoCep            = cliente.txtCep.text()
    campoBairro         = cliente.txtBairro.text().upper()
    campoCidade         = cliente.txtCidade.text().upper()

    if(campoNome == ''):
        QMessageBox.about(janelainserir, "OK!", "Preencha um Nome")

    elif(campoCpf == ''):
        QMessageBox.about(janelainserir, "OK!", "Preencha um CPF")    
        
    elif (campoNome != '' and campoCpf != ''):
        try:
            cursor = banco.cursor()
            comando_SQL = "INSERT INTO cliente (nome, rg, cpf, celular, telefone, logradouro, cep, bairro, cidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            dadoscliente = (str(campoNome), str(campoRg), str(campoCpf), str(campoCelular),str(campoFixo),str(campoLogradouro),str(campoCep),str(campoBairro), str(campoCidade))
            cursor.execute(comando_SQL, dadoscliente)
            QMessageBox.about(janelainserir, "OK!", "Cliente cadastrado com sucesso")
            banco.commit()
            campoNome           = cliente.txtNome.setText("")
            campoRg             = cliente.txtRg.setText("")
            campoCpf            = cliente.txtCpf.setText("")
            campoCelular        = cliente.txtCelular.setText("")
            campoFixo           = cliente.txtFixo.setText("")
            campoLogradouro     = cliente.txtLogradouro.setText("")
            campoCep            = cliente.txtCep.setText("")
            campoBairro         = cliente.txtBairro.setText("")
            campoCidade         = cliente.txtCidade.setText("")
            BuscarListarCliente()  
            linhacliente = listarbuscarcliente.tabelaListarClienteGeral.reset()       
        except:
            QMessageBox.about(janelainserir, "OK!", "Erro ao cadastrar cliente")

def BuscarListarCliente():

    linhacliente = listarbuscarcliente.tabelaListarClienteGeral.reset()
    cursor = banco.cursor()
        
    comando_SQL =  "SELECT nome, rg, cpf, celular, telefone, logradouro, cep, bairro, cidade FROM cliente"    
    cursor.execute(comando_SQL)
    listarClienteGeral = cursor.fetchall()    

    listarbuscarcliente.tabelaListarClienteGeral.setRowCount(len(listarClienteGeral))
    listarbuscarcliente.tabelaListarClienteGeral.setColumnCount(9)

    for linhas in range(0, len(listarClienteGeral)):
        for colunas in range(0, 9):
            listarbuscarcliente.tabelaListarClienteGeral.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listarClienteGeral[linhas][colunas])))            
 
def Pet():
    cadastrameupet.show()

def CadatraPetcliente():

    campoNome    = cadastrameupet.ComboNome.currentText()        
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
            
            campoNomepet = cadastrameupet.txtNomepet.setText("") 
            campoIdade   = cadastrameupet.txtIdade.setText("")        
            campoPeso    = cadastrameupet.txtPeso.setText("")
            QMessageBox.about(janelainserir, "OK!", "Pet cadastrado com sucesso.")
            
            listarbuscarcliente.tabelaListarClienteGeral.reset()
            BuscarListarCliente()
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
        
    
def TelaBuscarCliente():
    listarbuscarcliente.show()

def ExcluirCliente():

    linhacliente = - 1
    
    linhacliente = listarbuscarcliente.tabelaListarClienteGeral.currentRow()

    pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir?', QMessageBox.Yes | QMessageBox.No)
    
    if(linhacliente < 0):
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

    elif (pergunta == QMessageBox.Yes):
        #ExcluirCliente()
        linhacliente = listarbuscarcliente.tabelaListarClienteGeral.currentRow()
        listarbuscarcliente.tabelaListarClienteGeral.removeRow(linhacliente)  

        cursor = banco.cursor()
        comando_SQL = "SELECT id_cliente FROM cliente"    
        cursor.execute(comando_SQL)
        listaporcliente = cursor.fetchall()
        valorIdCliente = listaporcliente[linhacliente][0]
        cursor.execute("DELETE FROM cliente WHERE id_cliente = " + str(valorIdCliente))
        QMessageBox.about(janelainserir, "OK!", "Cliente excluído com sucesso")
        banco.commit()                     
        # listarbuscarcliente.tabelaListarClienteGeral.clear()
        listarbuscarcliente.tabelaListarClienteGeral.reset()
        BuscarListarCliente()        
    
    elif (pergunta == QMessageBox.No):
        BuscarListarCliente()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR") 

'''

def ExcluirCliente():
    linhacliente = listarbuscarcliente.tabelaListarClienteGeral.currentRow()
    listarbuscarcliente.tabelaListarClienteGeral.removeRow(linhacliente)  

    cursor = banco.cursor()
    comando_SQL = "SELECT id_cliente FROM cliente"    
    cursor.execute(comando_SQL)
    listaporcliente = cursor.fetchall()
    valorIdCliente = listaporcliente[linhacliente][0]
    cursor.execute("DELETE FROM cliente WHERE id_cliente = " + str(valorIdCliente))
    QMessageBox.about(janelainserir, "OK!", "Cliente excluído com sucesso")
    banco.commit()
'''
def AlterarCliente():
    
    cursor = banco.cursor()
    comando_SQL = "SELECT id_cliente FROM cliente"
    cursor.execute(comando_SQL)    
    
    listarClienteGeral = cursor.fetchall()
    for linhas in range(0, len(listarClienteGeral)):
        valorId             = listarClienteGeral[linhas][0]
        campoNome           = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 0).text().upper()
        campoRg             = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 1).text()
        campoCpf            = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 2).text()
        campoCelular        = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 3).text()
        campoFixo           = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 4).text()
        campoLogradouro     = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 5).text().upper()
        campoCep            = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 6).text()
        campoBairro         = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 7).text().upper()
        campoCidade         = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 8).text().upper() 
        cursor.execute("UPDATE cliente SET "
                        "nome = '" + str(campoNome) + "', "
                        "rg = '" + str(campoRg) + "', "
                        "cpf = '" + str(campoCpf) + "', "
                        "celular = '" + str(campoCelular) + "', "
                        "telefone = '" + str(campoFixo) + "', "
                        "logradouro = '" + str(campoLogradouro) + "', "
                        "cep = '" + str(campoCep) + "', "
                        "bairro = '" + str(campoBairro) + "', "
                        "cidade = '" + str(campoCidade)+"' WHERE id_cliente = " + str(valorId))
                        
        banco.commit()

def gerarPDFClientes():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cliente ORDER BY nome"
    cursor.execute(comando_SQL)
    cliente_lidos = cursor.fetchall()

    y = 0
    pdf = canvas.Canvas("lista_cliente.pdf")
    pdf.setFont("Times-Bold", 12)
    pdf.drawString(20, 800, "Lista de Cliente")

    pdf.setFont("Times-Bold", 10)
    #pdf.drawString(10, 750, "ID")
    pdf.drawString(20, 750, "NOME")
    pdf.drawString(210, 750, "CEP")    
    pdf.drawString(300, 750, "CELULAR")
    pdf.drawString(400, 750, "TELEFONE")
    
    #pdf.drawString(710, 750, "LOGRADOURO")
    #pdf.drawString(810, 750, "BAIRRO")
    pdf.drawString(500, 750, "CIDADE")


    for i in range(0, len(cliente_lidos)):
        y = y + 20
        #pdf.drawString(10, 750 - y, str(cliente_lidos[i][1]))
        pdf.drawString(20, 750 - y, str(cliente_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(cliente_lidos[i][3]))
        pdf.drawString(300, 750 - y, str(cliente_lidos[i][4]))
        pdf.drawString(400, 750 - y, str(cliente_lidos[i][7]))        
        #pdf.drawString(610, 750 - y, str(cliente_lidos[i][6]))
        #pdf.drawString(710, 750 - y, str(cliente_lidos[i][7]))
        #pdf.drawString(810, 750 - y, str(cliente_lidos[i][8]))
        pdf.drawString(500, 750 - y, str(cliente_lidos[i][9]))


    pdf.save()
    QMessageBox.about(janelainserir, "OK!", "PDF gerado com sucesso.")
 

clientepetshop = QtWidgets.QApplication([])
cliente = uic.loadUi("Cliente.ui")
cliente.btnCadastrar.clicked.connect(Cadastrarcliente)
cliente.btnPetcliente.clicked.connect(Pet)

cliente.btnBuscarCliente.clicked.connect(TelaBuscarCliente)
cliente.btnPetcliente.clicked.connect(BuscarRaca)

listarbuscarcliente = uic.loadUi("BuscarCliente.ui")
listarbuscarcliente.btnListarCliente.clicked.connect(BuscarListarCliente)
listarbuscarcliente.btnExcluir.clicked.connect(ExcluirCliente)
listarbuscarcliente.btnAlterar.clicked.connect(AlterarCliente)
listarbuscarcliente.btnPdfCliente.clicked.connect(gerarPDFClientes)


cadastrameupet = uic.loadUi("ClienteAddPet.ui")
cadastrameupet.btnCadastrarpet.clicked.connect(CadatraPetcliente)
#cadastrameupet.ComboEspecie.addItems(["GATO","CACHORRO"])
cadastrameupet.ComboPorte.addItems(["P","M","G"])
cadastrameupet.ComboRaca.addItems([""])

janelainserir = uic.loadUi("Petmensageminsere.ui")



cliente.show()
clientepetshop.exec()
