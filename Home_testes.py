from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
import mysql.connector
from reportlab.pdfgen import canvas
from datetime import datetime, timezone

banco = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "petshop")

def Cliente():
    cliente.show()    
    
def TelaBuscarCliente():
    listarbuscarcliente.show()


def Pet():
    cadastrameupet.show()

def Funcionarios():
    funcionario.show()    

def BuscarAddExcluirPets():
    buscaraddexcluirpets.show()

def listarBuscarFuncionario():
    listarfuncionario.show()

def CadastrarCategorias():
    cadastracategoria.show()

def AcessarAgendamentos():
    petagendamento.show()

def LogarFuncionario():
    loginfuncionario.show() 

#----------------------------------------------------------------------------------------------------------------------------------------------
def FuncaoLogar():
    
    Usuario = login.lineUsuario.text()
    Senha = login.lineSenha.text()
    cursor = banco.cursor()        
    logarSistema =  ("SELECT senha FROM login WHERE usuario = '{}'".format(Usuario))
    cursor.execute(logarSistema)
    usuariosenha = cursor.fetchall()   

    
    if (Usuario == '' and Senha == ''):
        QMessageBox.about(janelainserir, "OK!", "Usuário e senha em branco")        

    elif(Usuario == '' ):
        QMessageBox.about(janelainserir, "OK!", "Usuário em branco")

    elif(Senha == '' ):
        QMessageBox.about(janelainserir, "OK!", "Senha em branco")

    elif(Senha != usuariosenha[0][0]):
        QMessageBox.about(janelainserir, "OK!", "Senha invalida")

    elif(Senha == usuariosenha[0][0]):
        QMessageBox.about(janelainserir, "OK!", "Bem vindo MEU AMIGÃO!")
        home.show()
        login.close()
    elif(Usuario != usuariosenha[0]):
        QMessageBox.about(janelainserir, "OK!", "Usuário e senha invalidos")
     
#----------------------------------------------------------------------------------------------------------------------------------------------

def FuncionarioLogin(): 
    
    Usuario = loginfuncionario.lineUsuario.text()
    Senha = loginfuncionario.lineSenha.text()
    cursor = banco.cursor()        
    logarSistema =  ("SELECT senha FROM loginfuncionario WHERE usuario = '{}'".format(Usuario))
    cursor.execute(logarSistema)
    usuariosenha = cursor.fetchall()   

    
    if (Usuario == '' and Senha == ''):
        QMessageBox.about(janelainserir, "OK!", "Usuário e senha em branco")        

    elif(Usuario == '' ):
        QMessageBox.about(janelainserir, "OK!", "Usuário em branco")

    elif(Senha == '' ):
        QMessageBox.about(janelainserir, "OK!", "Senha em branco")

    elif(Senha != usuariosenha[0][0]):
        QMessageBox.about(janelainserir, "OK!", "Senha invalida")

    elif(Senha == usuariosenha[0][0]):
        QMessageBox.about(janelainserir, "OK!", "Bem vindo "+ Usuario +  ", módulo FUNCIONÁRIOS!")
        funcionario.show()
        loginfuncionario.close()
   
        
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
           
 

    
     
def BuscarCliente():
   
        campoNome = listarbuscarcliente.txtBuscarCliente.text()
      
        cursor = banco.cursor()
        comando_SQL = "SELECT nome, rg, cpf, celular, telefone, logradouro, cep, bairro, cidade FROM cliente WHERE nome like '%"+str(campoNome)+"%'"  
                
        cursor.execute(comando_SQL)
        listarClienteGeral = cursor.fetchall()        

        listarbuscarcliente.tabelaListarClienteGeral.setRowCount(len(listarClienteGeral))
        listarbuscarcliente.tabelaListarClienteGeral.setColumnCount(9)

        for linhas in range(0, len(listarClienteGeral)):
            for colunas in range(0, 9):
                listarbuscarcliente.tabelaListarClienteGeral.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listarClienteGeral[linhas][colunas])))

         
def ExcluirCliente():

    linhacliente = - 1
    
    linhacliente = listarbuscarcliente.tabelaListarClienteGeral.currentRow()

    pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir?', QMessageBox.Yes | QMessageBox.No)
    
    if(linhacliente < 0):
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

    elif (pergunta == QMessageBox.Yes):
        
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
        
        #listarbuscarcliente.tabelaListarClienteGeral.clear()
        BuscarListarCliente()        
    
    elif (pergunta == QMessageBox.No):
        BuscarListarCliente()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR") 


def AlterarCliente():
    
    cursor = banco.cursor()
    comando_SQL = "SELECT id_cliente FROM cliente"
    cursor.execute(comando_SQL)
    listarClienteGeral = cursor.fetchall()
    for linhas in range(0, len(listarClienteGeral)):
        valorId             = listarClienteGeral[linhas][0]
        campoNome           = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 0).text().upper()
        campoRg             = listarbuscarcliente.tabelaListarClienteGeral.item(linhas, 1).text().upper()
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


#----------------------------------------------------------------------------------------------------------------------------------------------
def CadatraPetcliente():

    listarbuscarcliente.tabelaListarClienteGeral.reset()
    
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

  
    

def ListarBuscarPet():    
    #linhapets = buscaraddexcluirpets.tabelaPetGeralporCliente.clear()

    cursor = banco.cursor()
    comando_SQL = "SELECT nomepet, idade, especie, porte, raca, peso, cliente FROM pet"
    
    cursor.execute(comando_SQL)
    listapetsporcliente = cursor.fetchall()
 
    buscaraddexcluirpets.tabelaPetGeralporCliente.setRowCount(len(listapetsporcliente))
    buscaraddexcluirpets.tabelaPetGeralporCliente.setColumnCount(7)

    for linhas in range(0, len(listapetsporcliente)):
        for colunas in range(0, 7):
            buscaraddexcluirpets.tabelaPetGeralporCliente.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listapetsporcliente[linhas][colunas])))

def BuscarPet():
   
        campoNomepet = buscaraddexcluirpets.txtNomepet.text()
      
        cursor = banco.cursor()
        comando_SQL = "SELECT nomepet, idade, especie, porte, raca, peso, cliente FROM pet WHERE nomepet like '%"+str(campoNomepet)+"%'"  
                
        cursor.execute(comando_SQL)
        listapetsporcliente = cursor.fetchall()        

        buscaraddexcluirpets.tabelaPetGeralporCliente.setRowCount(len(listapetsporcliente))
        buscaraddexcluirpets.tabelaPetGeralporCliente.setColumnCount(7)

        for linhas in range(0, len(listapetsporcliente)):
            for colunas in range(0, 7):
                buscaraddexcluirpets.tabelaPetGeralporCliente.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listapetsporcliente[linhas][colunas])))
            
def ExcluirPets():

    linhapets = - 1
    
    linhapets = buscaraddexcluirpets.tabelaPetGeralporCliente.currentRow()

    pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir?', QMessageBox.Yes | QMessageBox.No)
    
    if(linhapets < 0):
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

    elif (pergunta == QMessageBox.Yes):
        
         linhapets = buscaraddexcluirpets.tabelaPetGeralporCliente.currentRow()
         buscaraddexcluirpets.tabelaPetGeralporCliente.removeRow(linhapets)  

         cursor = banco.cursor()
         comando_SQL = "SELECT * FROM pet"
         cursor.execute(comando_SQL)
         listapetsporcliente = cursor.fetchall()
         valorId = listapetsporcliente[linhapets][0]
         cursor.execute("DELETE FROM pet WHERE id_pet = " + str(valorId))
         banco.commit()
         QMessageBox.about(janelainserir, "OK!", "Pet deletado com sucesso.") 
        
         linhapets = buscaraddexcluirpets.tabelaPetGeralporCliente.clear()
         ListarBuscarPet()        
    
    elif (pergunta == QMessageBox.No):
        ListarBuscarPet()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR")


def AlterarPet():

    cursor = banco.cursor()
    comando_SQL = "SELECT id_pet FROM pet"
    cursor.execute(comando_SQL)
    listarPetGeral = cursor.fetchall()
    for linhas in range(0, len(listarPetGeral)):
        valorId      = listarPetGeral[linhas][0]        
        campoNomepet = buscaraddexcluirpets.tabelaPetGeralporCliente.item(linhas, 0).text().upper()
        campoIdade   = buscaraddexcluirpets.tabelaPetGeralporCliente.item(linhas, 1).text()
        campoEspecie = buscaraddexcluirpets.tabelaPetGeralporCliente.item(linhas, 2).text().upper()
        campoPorte   = buscaraddexcluirpets.tabelaPetGeralporCliente.item(linhas, 3).text().upper()
        campoRaca    = buscaraddexcluirpets.tabelaPetGeralporCliente.item(linhas, 4).text().upper()
        campoPeso    = buscaraddexcluirpets.tabelaPetGeralporCliente.item(linhas, 5).text()
        campoCliente = buscaraddexcluirpets.tabelaPetGeralporCliente.item(linhas, 6).text().upper()
        cursor.execute("UPDATE pet SET "
                        "nomepet = '" + str(campoNomepet) + "', "
                        "idade = '" + str(campoIdade) + "', "
                        "especie = '" + str(campoEspecie) + "', "
                        "porte = '" + str(campoPorte) + "', "
                        "raca = '" + str(campoRaca) + "', "                        
                        "peso = '" + str(campoPeso)+"', "
                        "cliente = '" + str(campoCliente)+"' WHERE id_pet = " + str(valorId))                       
        
        banco.commit()
#----------------------------------------------------------------------------------------------------------------------------------------------

def Cadastrarfuncionario():
    
    campoNome           = funcionario.txtNome.text().upper()
    campoCargo          = funcionario.txtCargo.text().upper()
    campoRg             = funcionario.txtRg.text()
    campoCpf            = funcionario.txtCpf.text()
    campoDataNascimento = funcionario.txtDataNascimento.text()
    campoTelefone       = funcionario.txtTelefone.text()
    campoCelular        = funcionario.txtCelular.text()
    campoLogradouro     = funcionario.txtLogradouro.text().upper()
    campoCidade         = funcionario.txtCidade.text().upper()
    campoCep            = funcionario.txtCep.text()
    campoCampoSalario   = funcionario.txtSalario.text().replace(",",".")
    campoHoraentrada    = funcionario.txtEntrada.text()
    campoHorasaida      = funcionario.txtSaida.text()   
    
    try:
        cursor = banco.cursor()
        comando_SQL ="INSERT INTO funcionario (nome, cargo, rg, cpf, datadeNascimento, telefone, celular, logradouro, cidade, cep, salario, horaentrar, horasaida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dadosfuncionario = (str(campoNome), str(campoCargo), str(campoRg), str(campoCpf), str(campoDataNascimento),
                            str(campoTelefone), str(campoCelular), str(campoLogradouro), str(campoCidade), str(campoCep),
                            str(campoCampoSalario),str(campoHoraentrada), str(campoHorasaida))
        cursor.execute(comando_SQL, dadosfuncionario)                
        banco.commit()
        QMessageBox.about(janelainserir, "OK!", "Funcionario cadastrado com sucesso.")
        
        campoNome           = funcionario.txtNome.setText("")
        campoCargo          = funcionario.txtCargo.setText("")
        campoRg             = funcionario.txtRg.setText("")
        campoCpf            = funcionario.txtCpf.setText("")
        campoDataNascimento = funcionario.txtDataNascimento.setText("")
        campoTelefone       = funcionario.txtTelefone.setText("")
        campoCelular        = funcionario.txtCelular.setText("")
        campoLogradouro     = funcionario.txtLogradouro.setText("")
        campoCidade         = funcionario.txtCidade.setText("")
        campoCep            = funcionario.txtCep.setText("")
        campoCampoSalario   = funcionario.txtSalario.setText("")
        campoHoraentrada    = funcionario.txtEntrada.setText("")
        campoHorasaida      = funcionario.txtSaida.setText("")
        linhafuncionario = listarfuncionario.tabelaFuncionarios.clear()
        Listarfuncionario()
    except:
        QMessageBox.about(janelainserir, "OK!", "Erro ao cadastrar funcionário.")
        
def Listarfuncionario():
    
    #linhafuncionario = listarfuncionario.tabelaFuncionarios.clear()
    cursor = banco.cursor()
    comando_SQL = "SELECT nome, cargo, rg, cpf, datadeNascimento, telefone, celular, logradouro, cidade, cep, salario, horaentrar, horasaida FROM funcionario"
    cursor.execute(comando_SQL)
    funcionarioLido = cursor.fetchall()

    listarfuncionario.tabelaFuncionarios.setRowCount(len(funcionarioLido))
    listarfuncionario.tabelaFuncionarios.setColumnCount(13)

    for linhas in range(0, len(funcionarioLido)): 
        for colunas in range(0,13):
            listarfuncionario.tabelaFuncionarios.setItem(linhas,colunas, QtWidgets.QTableWidgetItem(str(funcionarioLido[linhas][colunas])))

def Excluirfuncionario():

    linhafuncionario = - 1
    
    linhafuncionario = listarfuncionario.tabelaFuncionarios.currentRow()

    pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir?', QMessageBox.Yes | QMessageBox.No)
    
    if(linhafuncionario < 0):
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

    elif (pergunta == QMessageBox.Yes):
        
        linhafuncionario = listarfuncionario.tabelaFuncionarios.currentRow()
        listarfuncionario.tabelaFuncionarios.removeRow(linhafuncionario)  

        cursor = banco.cursor()
        comando_SQL = "SELECT id_funcionario FROM funcionario"
        cursor.execute(comando_SQL)
        funcionariosLido = cursor.fetchall()
        valorId = funcionariosLido[linhafuncionario][0]
        cursor.execute("DELETE FROM funcionario WHERE id_funcionario = " + str(valorId))
        banco.commit()
        listarfuncionario.tabelaFuncionarios.clear()
        Listarfuncionario()
        
    elif (pergunta == QMessageBox.No):
        Listarfuncionario()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR")    

def AlterarFuncionario():

    cursor = banco.cursor()
    comando_SQL = "SELECT id_funcionario From funcionario"
    cursor.execute(comando_SQL)
    funcionario_lidos = cursor.fetchall()

    for lista in range(0, len(funcionario_lidos)):
        valorId          = funcionario_lidos[lista][0]
        nome             = listarfuncionario.tabelaFuncionarios.item(lista, 0).text().upper()
        cargo            = listarfuncionario.tabelaFuncionarios.item(lista, 1).text().upper()
        rg               = listarfuncionario.tabelaFuncionarios.item(lista, 2).text().upper()
        cpf              = listarfuncionario.tabelaFuncionarios.item(lista, 3).text()
        datadeNascimento = listarfuncionario.tabelaFuncionarios.item(lista, 4).text()
        telefone         = listarfuncionario.tabelaFuncionarios.item(lista, 5).text()
        celular          = listarfuncionario.tabelaFuncionarios.item(lista, 6).text()
        logradouro       = listarfuncionario.tabelaFuncionarios.item(lista, 7).text().upper()
        cidade           = listarfuncionario.tabelaFuncionarios.item(lista, 8).text().upper()
        cep              = listarfuncionario.tabelaFuncionarios.item(lista, 9).text().upper()
        salario          = listarfuncionario.tabelaFuncionarios.item(lista, 10).text()
        horaentrar       = listarfuncionario.tabelaFuncionarios.item(lista, 11).text()
        horasaida        = listarfuncionario.tabelaFuncionarios.item(lista, 12).text()

        cursor.execute("UPDATE funcionario SET "
                       "nome = '"+ str(nome) + "', "
                       "cargo = '"+ str(cargo) + "', "
                       "rg = '"+ str(rg) + "', "
                       "cpf = '"+ str(cpf) + "', "
                       "datadeNascimento = '"+ str(datadeNascimento) + "', "
                       "telefone = '"+ str(telefone) + "', "
                       "celular = '"+ str(celular ) + "', "
                       "logradouro = '"+ str(logradouro) + "', "
                       "cidade = '"+ str(cidade) + "', "
                       "cep = '" +str(cep) + "', "
                       "salario = '"+ str(salario) + "', "
                       "horaentrar = '"+ str(horaentrar) + "', "
                       "horasaida = '"+ str(horasaida) + "' WHERE id_funcionario = " + str(valorId))
        banco.commit()

def Cadastrar():

    campoCadastra = cadastracategoria.txtCadastrar.text().upper()   
    campoValor = cadastracategoria.txtValorCategoria.text().replace(",",".")
    cursor = banco.cursor()

    if (cadastracategoria.rbServico.isChecked()):        
        
        comando_SQL = "INSERT INTO servicos (nomeservico, valorservico) values (%s, %s)"
        dadosServico = (str(campoCadastra), str(campoValor))
        
        try:
            cursor.execute(comando_SQL, dadosServico)
            banco.commit()
            campoCadastra = cadastracategoria.txtCadastrar.setText("")
            campoValor = cadastracategoria.txtValorCategoria.setText("")
            QMessageBox.about(janelainserir, "OK!", "Serviço cadastrado com sucesso.")
            #listadeservicos = cadastracategoria.tabelaCategorias.clear()
            Listar()
        except:
            QMessageBox.about(janelainserir, "OK!", "Erro ao cadastrar Serviço")


    elif(cadastracategoria.rbGato.isChecked()):
        
        comando_SQL = "INSERT INTO categoriagato (racagato, valorunitario) values (%s, %s)"
        dadosRacaGato = (str(campoCadastra), str(campoValor))

        try:
            cursor.execute(comando_SQL, dadosRacaGato)
            banco.commit()
            campoCadastra = cadastracategoria.txtCadastrar.setText("")
            campoValor = cadastracategoria.txtValorCategoria.setText("")
            QMessageBox.about(janelainserir, "OK!", "Raça de gato cadastrada com sucesso.")
            #listaderacas = cadastracategoria.tabelaCategorias.clear()
            Listar() 
        except:
            QMessageBox.about(janelainserir, "OK!", "Erro ao cadastrar Gato")

    elif(cadastracategoria.rbCachorro.isChecked()):
        
        comando_SQL = "INSERT INTO categoriacachorro (racacachorro, valorunitario) values (%s, %s)"
        dadosRacaCachorro = (str(campoCadastra), str(campoValor))

        try:
            cursor.execute(comando_SQL, dadosRacaCachorro)
            banco.commit()
            campoCadastra = cadastracategoria.txtCadastrar.setText("")
            campoValor = cadastracategoria.txtValorCategoria.setText("")
            QMessageBox.about(janelainserir, "OK!", "Raça de cachorro cadastrada com sucesso.")
            #listaderacas = cadastracategoria.tabelaCategorias.clear()
            Listar()
        except:
            QMessageBox.about(janelainserir, "OK!", "Erro ao cadastrar Cachorro")
 
def Listar():
        #listadeservicos = cadastracategoria.tabelaCategorias.clear()
        if(cadastracategoria.rbServico.isChecked()):
            cursor = banco.cursor()
            comando_SQL = "SELECT nomeservico, valorservico FROM servicos "
            cursor.execute(comando_SQL)
            listarCategorias = cursor.fetchall()        

            cadastracategoria.tabelaCategorias.setRowCount(len(listarCategorias))
            cadastracategoria.tabelaCategorias.setColumnCount(2)

            for linhas in range(0, len(listarCategorias)):
                for colunas in range(0, 2):
                    cadastracategoria.tabelaCategorias.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listarCategorias[linhas][colunas])))

        elif(cadastracategoria.rbGato.isChecked()):
            cursor = banco.cursor()
            comando_SQL = "SELECT racagato, valorunitario from categoriagato"
            cursor.execute(comando_SQL)
            listarCategorias = cursor.fetchall()        

            cadastracategoria.tabelaCategorias.setRowCount(len(listarCategorias))
            cadastracategoria.tabelaCategorias.setColumnCount(2)

            for linhas in range(0, len(listarCategorias)):
                for colunas in range(0, 2):
                    cadastracategoria.tabelaCategorias.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listarCategorias[linhas][colunas])))


        elif(cadastracategoria.rbCachorro.isChecked()):
            cursor = banco.cursor()
            comando_SQL = "SELECT racacachorro, valorunitario from categoriacachorro"
            cursor.execute(comando_SQL)
            listarCategorias = cursor.fetchall()        

            cadastracategoria.tabelaCategorias.setRowCount(len(listarCategorias))
            cadastracategoria.tabelaCategorias.setColumnCount(2)

            for linhas in range(0, len(listarCategorias)):
                for colunas in range(0, 2):
                    cadastracategoria.tabelaCategorias.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listarCategorias[linhas][colunas])))       


def Excluir():    
    listadeservicos = - 1
    listaderacas = - 1

    if (cadastracategoria.rbServico.isChecked()):
        listadeservicos = cadastracategoria.tabelaCategorias.currentRow()

        pergunta = QMessageBox.question(janelainserir, 'Confirmação', 'Deseja excluir SERVIÇO?',
                                        QMessageBox.Yes | QMessageBox.No)

    if (listadeservicos < 0):
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")

    elif (pergunta == QMessageBox.Yes):
        listadeservicos = cadastracategoria.tabelaCategorias.currentRow()
        cadastracategoria.tabelaCategorias.removeRow(listadeservicos)

        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM servicos"
        cursor.execute(comando_SQL)
        servicosemgeral = cursor.fetchall()
        valorId = servicosemgeral[listadeservicos][0]
        cursor.execute("DELETE FROM servicos WHERE id_servicos =" + str(valorId))
        banco.commit()
        QMessageBox.about(janelainserir, "OK!", "Registro de SERVIÇO EXCLUÍDO com sucesso.")
        cadastracategoria.tabelaCategorias.clear()
        Listar()

    elif (pergunta == QMessageBox.No):
        Listar()

    else:
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR")

    if (cadastracategoria.rbGato.isChecked()):
        listaderacas = cadastracategoria.tabelaCategorias.currentRow()

        pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir raça de GATO?', QMessageBox.Yes | QMessageBox.No)
        
        if(listaderacas < 0):
            QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

        elif (pergunta == QMessageBox.Yes):        
        
            listaderacas = cadastracategoria.tabelaCategorias.currentRow()
            cadastracategoria.tabelaCategorias.removeRow(listaderacas)  
   
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM categoriagato"
            cursor.execute(comando_SQL)
            racasemgeral = cursor.fetchall()
            valorId = racasemgeral[listaderacas][0]
            cursor.execute("DELETE FROM categoriagato WHERE id_gato ="+ str(valorId))
            banco.commit()
            QMessageBox.about(janelainserir, "OK!", "Raça de GATO excluída com sucesso.")
            cadastracategoria.tabelaCategorias.clear()
            Listar()
        
        elif (pergunta == QMessageBox.No):
            Listar()
        
        else:   
            QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR")

    if (cadastracategoria.rbCachorro.isChecked()):
        listaderacas = cadastracategoria.tabelaCategorias.currentRow()

        pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir raça de CACHORRO?', QMessageBox.Yes | QMessageBox.No)
        
        if(listaderacas < 0):
            QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

        elif (pergunta == QMessageBox.Yes):        
        
            listaderacas = cadastracategoria.tabelaCategorias.currentRow()
            cadastracategoria.tabelaCategorias.removeRow(listaderacas)  
   
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM categoriacachorro"
            cursor.execute(comando_SQL)
            racasemgeral = cursor.fetchall()
            valorId = racasemgeral[listaderacas][0]
            cursor.execute("DELETE FROM categoriacachorro WHERE id_cachorro ="+ str(valorId))
            banco.commit()
            QMessageBox.about(janelainserir, "OK!", "Raça de CACHORRO excluída com sucesso.")
            cadastracategoria.tabelaCategorias.clear()
            Listar()
        
        elif (pergunta == QMessageBox.No):
            Listar()
        
        else:   
            QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR") 



def Alterar():
   

    
    if (cadastracategoria.rbServico.isChecked()):
        cursor = banco.cursor()
        comando_SQL = "SELECT id_servicos FROM servicos"
        cursor.execute(comando_SQL)
        listaServicos = cursor.fetchall()
        for linhas in range(0, len(listaServicos)):
            valorId = listaServicos[linhas][0]
            campoCadastra   = cadastracategoria.tabelaCategorias.item(linhas, 0).text().upper()    
            campoValor      = cadastracategoria.tabelaCategorias.item(linhas, 1).text().replace(",",".")
            cursor.execute("UPDATE servicos SET "
                            "nomeservico = '" + str(campoCadastra) + "', "
                            "valorservico = '" + str(campoValor)+"' WHERE id_servicos = " + str(valorId))
            banco.commit()

    if (cadastracategoria.rbGato.isChecked()):
        cursor = banco.cursor()
        comando_SQL = "SELECT id_gato FROM categoriagato"
        cursor.execute(comando_SQL)
        racasemgeral = cursor.fetchall()
        for linhas in range(0, len(racasemgeral)):
            valorId = racasemgeral[linhas][0]
            campoCadastra   = cadastracategoria.tabelaCategorias.item(linhas, 0).text().upper()    
            campoValor      = cadastracategoria.tabelaCategorias.item(linhas, 1).text().replace(",",".")        
            cursor.execute("UPDATE categoriagato SET "
                            "racagato = '" + str(campoCadastra) + "', "
                            "valorunitario = '" + str(campoValor)+"' WHERE id_gato = " + str(valorId))
            banco.commit()

    if (cadastracategoria.rbCachorro.isChecked()):
        cursor = banco.cursor()
        comando_SQL = "SELECT id_cachorro FROM categoriacachorro"
        cursor.execute(comando_SQL)
        racasemgeral = cursor.fetchall()
        for linhas in range(0, len(racasemgeral)):
            valorId = racasemgeral[linhas][0]
            campoCadastra   = cadastracategoria.tabelaCategorias.item(linhas, 0).text().upper()    
            campoValor      = cadastracategoria.tabelaCategorias.item(linhas, 1).text().replace(",",".")        
            cursor.execute("UPDATE categoriacachorro SET "
                            "racacachorro = '" + str(campoCadastra) + "', "
                            "valorunitario = '" + str(campoValor)+"' WHERE id_cachorro = " + str(valorId))


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


'''    
def BuscarRacaPetCliente():       

    cursor = banco.cursor()
    comando_SQL = "SELECT raca FROM categoriapet ORDER BY raca"   
    cursor.execute(comando_SQL)
    listacategoria = cursor.fetchall()
    

    for categorias in listacategoria:
            cadastrameupet.ComboRaca.addItem(categorias[0])


def CadastraRaca():
    
    campoRacaPet = cadastracategoria.txtRacacategoria.text().upper()
    campoLixo = cadastracategoria.txtServicoCategoria.text().upper()
    cursor = banco.cursor()
    
    comando_SQL = "INSERT INTO categoriapet (raca_cachorro, raca_gato) values (%s, %s)"
    dadosRacaPet = (str(campoRacaPet),str(campoLixo))    
    
    try:
        cursor.execute(comando_SQL, dadosRacaPet)
        banco.commit()
        campoRacaPet = cadastracategoria.txtRacacategoria.setText("")
        QMessageBox.about(janelainserir, "OK!", "Raça cadastrada com sucesso.")
        #listaderacas = cadastracategoria.tabelaCategoriaRaca.clear()
        ListarRacas() 
    except:
        QMessageBox.about(janelainserir, "OK!", "Erro ao cadastrar Raça")
        
def ListarRacas():

        listaderacas = cadastracategoria.tabelaCategoriaRaca.clear()
        
        cursor = banco.cursor()
        comando_SQL = "SELECT raca_cachorro from categoriapet"
        cursor.execute(comando_SQL)
        ListarRacas = cursor.fetchall()        

        cadastracategoria.tabelaCategoriaRaca.setRowCount(len(ListarRacas))
        cadastracategoria.tabelaCategoriaRaca.setColumnCount(1)

        for linhas in range(0, len(ListarRacas)):
            for colunas in range(0, 1):
                cadastracategoria.tabelaCategoriaRaca.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(ListarRacas[linhas][colunas])))

def ExcluirRaca():

    listaderacas = - 1
    
    listaderacas = cadastracategoria.tabelaCategoriaRaca.currentRow()

    pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir?', QMessageBox.Yes | QMessageBox.No)
    
    if(listaderacas < 0):
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

    elif (pergunta == QMessageBox.Yes):
                
        listaderacas = cadastracategoria.tabelaCategoriaRaca.currentRow()
        cadastracategoria.tabelaCategoriaRaca.removeRow(listaderacas)  
   
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM categoriapet"
        cursor.execute(comando_SQL)
        racasemgeral = cursor.fetchall()
        valorId = racasemgeral[listaderacas][0]
        cursor.execute("DELETE FROM categoriapet WHERE id_categoriapet ="+ str(valorId))
        banco.commit()
        QMessageBox.about(janelainserir, "OK!", "Raça deletada com sucesso.")
        cadastracategoria.tabelaCategoriaRaca.clear()
        ListarRacas()
        
    elif (pergunta == QMessageBox.No):
        ListarRacas()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR") 


def CadastraServico():
    
    campoServico = cadastracategoria.txtServicoCategoria.text().upper()
    campoLixo = cadastracategoria.txtRacacategoria.text().upper()
    cursor = banco.cursor()
    
    comando_SQL = "INSERT INTO servicos (nomeservico, valorservico) values (%s, %s)"
    dadosRacaPet = (str(campoServico), str(campoLixo))    
    
    try:
        cursor.execute(comando_SQL, dadosRacaPet)
        banco.commit()
        campoServico = cadastracategoria.txtServicoCategoria.setText("")
        QMessageBox.about(janelainserir, "OK!", "Serviço cadastrado com sucesso.")
        #listadeservicos = cadastracategoria.tabelaServicos.clear()
        ListarServicos()
    except:
        QMessageBox.about(janelainserir, "OK!", "Erro ao cadastrar Serviço")


  
def ListarServicos():

        #listadeservicos = cadastracategoria.tabelaServicos.clear()
     
        cursor = banco.cursor()
        comando_SQL = "SELECT nomeservico from servicos"
        cursor.execute(comando_SQL)
        listaServicos = cursor.fetchall()        

        cadastracategoria.tabelaServicos.setRowCount(len(listaServicos))
        cadastracategoria.tabelaServicos.setColumnCount(1)

        for linhas in range(0, len(listaServicos)):
            for colunas in range(0, 1):
                cadastracategoria.tabelaServicos.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listaServicos[linhas][colunas])))

def ExcluirServico():

    listadeservicos = - 1
    
    listadeservicos = cadastracategoria.tabelaServicos.currentRow()

    pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir?', QMessageBox.Yes | QMessageBox.No)
    
    if(listadeservicos < 0):
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

    elif (pergunta == QMessageBox.Yes):
        
        listadeservicos = cadastracategoria.tabelaServicos.currentRow()
        cadastracategoria.tabelaServicos.removeRow(listadeservicos)  
   
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM servicos"
        cursor.execute(comando_SQL)
        servicosemgeral = cursor.fetchall()
        valorId = servicosemgeral[listadeservicos][0]
        cursor.execute("DELETE FROM servicos WHERE id_servicos ="+ str(valorId))
        banco.commit()
        QMessageBox.about(janelainserir, "OK!", "Serviço deletado com sucesso.")      
        
        #cadastracategoria.tabelaServicos.clear()
        ListarServicos()
        
    elif (pergunta == QMessageBox.No):
        ListarServicos()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR") 


def AlteraRaca():

    cursor = banco.cursor()
    comando_SQL = "SELECT id_categoriapet FROM categoriapet"
    cursor.execute(comando_SQL)
    racasemgeral = cursor.fetchall()
    for linhas in range(0, len(racasemgeral)):
        valorId = racasemgeral[linhas][0]
        campoRacaPet = cadastracategoria.tabelaCategoriaRaca.item(linhas, 0).text().upper()        
        cursor.execute("UPDATE categoriapet SET "
                        "raca_cachorro = '" + str(campoRacaPet)+"' WHERE id_categoriapet = " + str(valorId))
        banco.commit()


def AlteraServicos():

    cursor = banco.cursor()
    comando_SQL = "SELECT id_servicos FROM servicos"
    cursor.execute(comando_SQL)
    listaServicos = cursor.fetchall()
    for linhas in range(0, len(listaServicos)):
        valorId = listaServicos[linhas][0]
        campoServico = cadastracategoria.tabelaServicos.item(linhas, 0).text().upper()         
        cursor.execute("UPDATE servicos SET "
                        "nomeservico = '" + str(campoServico)+"' WHERE id_servicos = " + str(valorId))
        banco.commit()

'''        
def Agendamento():        
    agendamento.show()

def CadastrarAgendamento():
       
        campoNomepet = agendamento.txtNomepet.text().upper()
        campoEspecie = agendamento.comboEspecie.currentText()
        campoPorte = agendamento.comboPorte.currentText()
        campoPeso = agendamento.txtPeso.text().replace(",",".")
        Data = agendamento.txtDataAgendamento.text()
        campoData = datetime.strptime(Data, '%d/%m/%Y').date()        
        campoHorario = agendamento.txtHorario.text()
        campoValor = agendamento.txtValor.text().replace(",",".")
        campoProfissional = agendamento.ComboProfissional.currentText()        
        campoProcedimento = agendamento.ComboServico.currentText().upper()
        campoRealizado = agendamento.ComboRealizado.currentText()
        if (campoNomepet == ''):
            QMessageBox.about(janelainserir, "OK!", "Preencha um nome")
            
        else:
            cursor = banco.cursor()
            comando_SQL = "INSERT INTO agendamento (nomepet, especie, porte, peso, datas, horario, valorservico, nomeprofissional, procedimento, realizado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            dadosagendamento = (str(campoNomepet), str(campoEspecie), str(campoPorte), str(campoPeso), str(campoData),
                                str(campoHorario), str(campoValor), str(campoProfissional), str(campoProcedimento),
                                str(campoRealizado))
            try:
                cursor.execute(comando_SQL, dadosagendamento)
                banco.commit()
                
                campoNomepet = agendamento.txtNomepet.setText("")                
                campoPeso = agendamento.txtPeso.setText("")
                campoValor   = agendamento.txtValor.setText("")               
                QMessageBox.about(janelainserir, "OK!", "Agendamento realizado com sucesso.")
                
                agendamentospets = petagendamento.tabelaAgendamento.reset()
                ListarAgendamento() 
            except:
                QMessageBox.about(janelainserir, "OK!", "Erro a cadastrar Pet.")
                
def ListarAgendamento():

#        agendamentospets = petagendamento.tabelaAgendamento.clear()
       
        cursor = banco.cursor()                       
        comando_SQL = "SELECT  nomepet, especie, porte, peso, datas, horario, valorservico, nomeprofissional, procedimento, realizado FROM agendamento"
        cursor.execute(comando_SQL)        
        listapetsporcliente = cursor.fetchall()        

        petagendamento.tabelaAgendamento.setRowCount(len(listapetsporcliente))
        petagendamento.tabelaAgendamento.setColumnCount(10)

        for linhas in range(0, len(listapetsporcliente)):
            for colunas in range(0, 10):
                petagendamento.tabelaAgendamento.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listapetsporcliente[linhas][colunas])))

def BuscarAgendamento():
   
        campoNomepet = petagendamento.txtBuscarAgendamento.text()
      
        cursor = banco.cursor()
        comando_SQL = "SELECT nomepet, especie, porte, peso, datas, horario, valorservico, nomeprofissional, procedimento, realizado FROM agendamento WHERE nomepet like '%"+str(campoNomepet)+"%'"  
                
        cursor.execute(comando_SQL)
        listarAgendamento = cursor.fetchall()        

        petagendamento.tabelaAgendamento.setRowCount(len(listarAgendamento))
        petagendamento.tabelaAgendamento.setColumnCount(10)

        for linhas in range(0, len(listarAgendamento)):
            for colunas in range(0, 10):
                petagendamento.tabelaAgendamento.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listarAgendamento[linhas][colunas])))


def ExcluirAgendamento():

    agendamentospets = - 1
    
    agendamentospets = petagendamento.tabelaAgendamento.currentRow()

    pergunta = QMessageBox.question(janelainserir, 'Confirmação','Deseja excluir?', QMessageBox.Yes | QMessageBox.No)
    
    if(agendamentospets < 0):
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para EXCLUIR")        

    elif (pergunta == QMessageBox.Yes):
        
        
        agendamentospets = petagendamento.tabelaAgendamento.currentRow()
        petagendamento.tabelaAgendamento.removeRow(agendamentospets) 

        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM agendamento"
        cursor.execute(comando_SQL)
        listagendamentos = cursor.fetchall()
        valorId = listagendamentos[agendamentospets][0]
        cursor.execute("DELETE FROM agendamento WHERE id_agendamento ="+ str(valorId))
        banco.commit()
        QMessageBox.about(janelainserir, "OK!", "Agendamento deletado com sucesso.")
        petagendamento.tabelaAgendamento.reset()
        ListarAgendamento() 
    
    elif (pergunta == QMessageBox.No):
        ListarAgendamento()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR") 


def AlterarAgendamento():

    cursor = banco.cursor()
    comando_SQL = "SELECT id_agendamento FROM agendamento"
    cursor.execute(comando_SQL)
    listarAgendamento = cursor.fetchall()
    for linhas in range(0, len(listarAgendamento)):
        valorId = listarAgendamento[linhas][0]
        campoNomepet        = petagendamento.tabelaAgendamento.item(linhas, 0).text().upper()
        campoEspecie        = petagendamento.tabelaAgendamento.item(linhas, 1).text().upper()
        campoPorte          = petagendamento.tabelaAgendamento.item(linhas, 2).text().upper()
        campoPeso           = petagendamento.tabelaAgendamento.item(linhas, 3).text()
        campoData           = petagendamento.tabelaAgendamento.item(linhas, 4).text()
        campoHorario        = petagendamento.tabelaAgendamento.item(linhas, 5).text()
        campoValor          = petagendamento.tabelaAgendamento.item(linhas, 6).text()
        campoProfissional   = petagendamento.tabelaAgendamento.item(linhas, 7).text().upper()
        campoProcedimento   = petagendamento.tabelaAgendamento.item(linhas, 8).text().upper()
        campoRealizado      = petagendamento.tabelaAgendamento.item(linhas, 9).text().upper()
        
        
        cursor.execute("UPDATE agendamento SET "
                        "nomepet = '" + str(campoNomepet)  + "', "
                        "especie = '" + str(campoEspecie)  + "', "
                        "porte = '" + str(campoPorte)  + "', "
                        "peso = '" + str(campoPeso)  + "', "
                        "datas = '" + str(campoData) + "', "
                        "horario = '" + str(campoHorario)  + "', "
                        "valorservico = '" + str(campoValor)  + "', "
                        "nomeprofissional = '" + str(campoProfissional)  + "', "
                        "procedimento = '" + str(campoProcedimento) + "', "                      
                        "realizado = '" + str(campoRealizado)+"' WHERE id_agendamento = " + str(valorId))        
                        
        banco.commit()

  
def BuscarNomeFuncionario():       

    cursor = banco.cursor()
    comando_SQL = "SELECT nome FROM funcionario ORDER by nome"   
    cursor.execute(comando_SQL)
    listarprofissional = cursor.fetchall()    

    for funcionario in listarprofissional:
            agendamento.ComboProfissional.addItem(funcionario[0])


def BuscarServicos():       

    cursor = banco.cursor()
    comando_SQL = "SELECT nomeservico FROM servicos ORDER by nomeservico"   
    cursor.execute(comando_SQL)
    listarservicos = cursor.fetchall()
    

    for funcionario in listarservicos:
            agendamento.ComboServico.addItem(funcionario[0])


def gerarPDFAgendamento():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM agendamento ORDER BY datas"
    cursor.execute(comando_SQL)
    agendamento_lidos = cursor.fetchall()

    y = 0
    pdf = canvas.Canvas("lista_agendamento.pdf")
    pdf.setFont("Times-Bold", 10)
    pdf.drawString(200, 800, "Lista de Agendamento")

    pdf.setFont("Times-Bold", 10)
    
    pdf.drawString(10, 750, "NOMEPET")
    pdf.drawString(80, 750, "ESPECIE")    
    pdf.drawString(140, 750, "PESO")
    pdf.drawString(180, 750, "DATAS")
    pdf.drawString(250, 750, "HORARIO")
    pdf.drawString(310, 750, "VALOR")
    pdf.drawString(370, 750, "PROFISSIONAL")
    pdf.drawString(480, 750, "PROCEDIMENTO")
    


    for i in range(0, len(agendamento_lidos)):
        y = y + 20
        
        pdf.drawString(10, 750 - y, str(agendamento_lidos[i][1]))
        pdf.drawString(80, 750 - y, str(agendamento_lidos[i][2]))        
        pdf.drawString(140, 750 - y, str(agendamento_lidos[i][4]))
        pdf.drawString(180, 750 - y, str(agendamento_lidos[i][5]))
        pdf.drawString(250, 750 - y, str(agendamento_lidos[i][6]))
        pdf.drawString(310, 750 - y, str(agendamento_lidos[i][7]))
        pdf.drawString(370, 750 - y, str(agendamento_lidos[i][8]))
        pdf.drawString(480, 750 - y, str(agendamento_lidos[i][9]))

    pdf.save()
    QMessageBox.about(janelainserir, "OK!", "PDF gerado com sucesso.")

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

    pdf.drawString(10, 750, "NOMEPET")
    pdf.drawString(110, 750, "IDADE")
    pdf.drawString(210, 750, "ESPECIE")
    pdf.drawString(310, 750, "PORTE")
    pdf.drawString(410, 750, "RACA")
    pdf.drawString(510, 750, "PESO")


    for i in range(0, len(pet_lidos)):
        y = y + 20
        pdf.drawString(10, 750 - y, str(pet_lidos[i][1]))
        pdf.drawString(110, 750 - y, str(pet_lidos[i][2]))
        pdf.drawString(210, 750 - y, str(pet_lidos[i][3]))
        pdf.drawString(310, 750 - y, str(pet_lidos[i][4]))
        pdf.drawString(410, 750 - y, str(pet_lidos[i][5]))
        pdf.drawString(510, 750 - y, str(pet_lidos[i][6]))


    pdf.save()
    QMessageBox.about(janelainserir, "OK!", "PDF gerado com sucesso.")

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
    
    pdf.drawString(20, 750, "NOME")
    pdf.drawString(210, 750, "CEP")    
    pdf.drawString(300, 750, "CELULAR")
    pdf.drawString(400, 750, "TELEFONE")  
    pdf.drawString(500, 750, "CIDADE")


    for i in range(0, len(cliente_lidos)):
        y = y + 20
        
        pdf.drawString(20, 750 - y, str(cliente_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(cliente_lidos[i][3]))
        pdf.drawString(300, 750 - y, str(cliente_lidos[i][4]))
        pdf.drawString(400, 750 - y, str(cliente_lidos[i][7])) 
        pdf.drawString(500, 750 - y, str(cliente_lidos[i][9]))


    pdf.save()                
    QMessageBox.about(janelainserir, "OK!", "PDF gerado com sucesso.")

def gerarPDFFuncionario():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM funcionario ORDER by nome"
    cursor.execute(comando_SQL)
    funcionario_lidos = cursor.fetchall()

    y = 0
    pdf = canvas.Canvas("lista_funcionario.pdf")
    pdf.setFont("Times-Bold", 10)
    pdf.drawString(200, 800, "Lista de Funcionario")

    pdf.setFont("Times-Bold", 10)
 
    pdf.drawString(50, 750, "NOME")
    pdf.drawString(220, 750, "CARGO")
    pdf.drawString(350, 750, "RG")
    pdf.drawString(450, 750, "CPF")
    pdf.drawString(530, 750, "SALARIO")


    for i in range(0, len(funcionario_lidos)):
        y = y + 20

        pdf.drawString(50, 750 - y, str(funcionario_lidos[i][1]))
        pdf.drawString(220, 750 - y, str(funcionario_lidos[i][2]))
        pdf.drawString(350, 750 - y, str(funcionario_lidos[i][3]))
        pdf.drawString(450, 750 - y, str(funcionario_lidos[i][4]))
       
        pdf.drawString(530, 750 - y, str(funcionario_lidos[i][11]))


    pdf.save()
    QMessageBox.about(janelainserir, "OK!", "PDF gerado com sucesso.")


homeprogramapetshop = QtWidgets.QApplication([])
login = uic.loadUi("login.ui") 
login.btnEntrar.clicked.connect(FuncaoLogar)

loginfuncionario = uic.loadUi("Loginfuncionario.ui")
loginfuncionario.btnEntrarFuncionario.clicked.connect(FuncionarioLogin)


home = uic.loadUi("Home.ui")
home.btnCliente.clicked.connect(Cliente)
home.btnPet.clicked.connect(BuscarAddExcluirPets)
home.btnServicos.clicked.connect(CadastrarCategorias)
home.btnAgendamento.clicked.connect(AcessarAgendamentos)
#home.btnFuncionario.clicked.connect(Funcionarios)
home.btnFuncionario.clicked.connect(LogarFuncionario)

#home.btnPet.clicked.connect(ListarBuscarPet)
#---------------------------------------------------------------------
cliente = uic.loadUi("Cliente.ui")
#cliente.btnPetcliente.clicked.connect(BuscarRacaPetCliente)
cliente.btnCadastrar.clicked.connect(Cadastrarcliente)
cliente.btnPetcliente.clicked.connect(Pet)

cliente.btnBuscarCliente.clicked.connect(TelaBuscarCliente)
cliente.btnBuscarCliente.clicked.connect(BuscarListarCliente)
cliente.btnPetcliente.clicked.connect(BuscarRaca)


listarbuscarcliente = uic.loadUi("BuscarCliente.ui")
listarbuscarcliente.btnListarCliente.clicked.connect(BuscarListarCliente)
listarbuscarcliente.btnExcluir.clicked.connect(ExcluirCliente)
listarbuscarcliente.btnAlterar.clicked.connect(AlterarCliente)
listarbuscarcliente.btnPdfCliente.clicked.connect(gerarPDFClientes)
listarbuscarcliente.btnBuscarClientes.clicked.connect(BuscarCliente)

#---------------------------------------------------------------------

buscaraddexcluirpets = uic.loadUi("BuscaPet.ui")
buscaraddexcluirpets.btnAddPet.clicked.connect(Pet)
#buscaraddexcluirpets.btnAddPet.clicked.connect(BuscarRacaPetCliente)
buscaraddexcluirpets.btnListarPets.clicked.connect(ListarBuscarPet)
buscaraddexcluirpets.btnExcluirpet.clicked.connect(ExcluirPets)
buscaraddexcluirpets.btnAlterarPet.clicked.connect(AlterarPet)
buscaraddexcluirpets.btnPdfPet.clicked.connect(gerarPDFBuscaPet)
buscaraddexcluirpets.btnBuscar.clicked.connect(BuscarPet)

cadastrameupet = uic.loadUi("ClienteAddPet.ui")
cadastrameupet.btnCadastrarpet.clicked.connect(CadatraPetcliente)
#cadastrameupet.ComboEspecie.addItems(["G","C"])
cadastrameupet.ComboPorte.addItems(["P","M","G"])
cadastrameupet.ComboRaca.addItems([""])

#---------------------------------------------------------------------

funcionario = uic.loadUi("Funcionario.ui")
funcionario.btnCadastrarfuncionario.clicked.connect(Cadastrarfuncionario)
funcionario.btnListarfuncionarios.clicked.connect(listarBuscarFuncionario)


listarfuncionario = uic.loadUi("listafuncionario.ui")
listarfuncionario.btnListarFuncionario.clicked.connect(Listarfuncionario)
listarfuncionario.btnExcluirFuncionario.clicked.connect(Excluirfuncionario)
listarfuncionario.btnAlterar.clicked.connect(AlterarFuncionario)
listarfuncionario.btnGerarPdf.clicked.connect(gerarPDFFuncionario)

#listarfuncionario.btnBuscarFuncionario.clicked.connect(BuscarFuncionario)

#---------------------------------------------------------------------

cadastracategoria = uic.loadUi("Categoria.ui")
cadastracategoria.btnCadastrar.clicked.connect(Cadastrar)
cadastracategoria.btnListarCategoria.clicked.connect(Listar)
cadastracategoria.btnExcluir.clicked.connect(Excluir)
cadastracategoria.btnAlteracoes.clicked.connect(Alterar)
#cadastracategoria.btnCadastra.clicked.connect(CadastraRaca)
#cadastracategoria.btnCadastrarServico.clicked.connect(CadastraServico)
#cadastracategoria.btnExcluirRaca.clicked.connect(ExcluirRaca)
#cadastracategoria.btnExcluirServico.clicked.connect(ExcluirServico)
#cadastracategoria.btnListarCategoria.clicked.connect(ListarRacas)
#cadastracategoria.btnListarCategoria.clicked.connect(ListarServicos)
#cadastracategoria.btnAlteraraca.clicked.connect(AlteraRaca)
#cadastracategoria.btnAlterarServico.clicked.connect(AlteraServicos)

petagendamento = uic.loadUi("AgendamentoLista.ui")
petagendamento.btnListarAgendamento.clicked.connect(ListarAgendamento)
petagendamento.btnConsultar.clicked.connect(BuscarAgendamento)

petagendamento.btnAgendar.clicked.connect(Agendamento)

petagendamento.btnExcluirAgendamento.clicked.connect(ExcluirAgendamento)
petagendamento.btnAlterarAgendamento.clicked.connect(AlterarAgendamento)

petagendamento.btnAgendar.clicked.connect(BuscarNomeFuncionario)
petagendamento.btnAgendar.clicked.connect(BuscarServicos)

petagendamento.btnGerarPdfAgendamento.clicked.connect(gerarPDFAgendamento)

agendamento = uic.loadUi("Agendamento.ui")
agendamento.btnAgendarProcedimento.clicked.connect(CadastrarAgendamento)
agendamento.comboEspecie.addItems(["GATO","CACHORRO"])
agendamento.comboPorte.addItems(["P","M","G"])
agendamento.ComboServico.addItems([""])
agendamento.ComboRealizado.addItems(["SIM","NAO","REMARCADO"])
agendamento.ComboProfissional.addItems([""])


janelainserir = uic.loadUi("Petmensageminsere.ui")

login.show()
#home.show()
homeprogramapetshop.exec()
#EXCLUIR PETS COM CHAVE ESTRANGEIRA TRAZ PROBLEMAS NO ORDENAMENTO. INSERIR CASCADE
