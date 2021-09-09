from PyQt5 import uic,  QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "petshop")


def Cadastrarfuncionario():
    
    campoNome           = funcionario.txtNome.text().upper()
    campoSobrenome      = funcionario.txtSobrenome.text().upper()
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

    if (campoNome == '' and campoSobrenome  == '' and campoCpf == ''):
        QMessageBox.about(janelainserir, "OK!", "Preencha um NOME SOBRENOME e CPF")

    elif (campoNome != '' and campoSobrenome != '' and campoCpf != ''): 
  
        try:
            cursor = banco.cursor()
            comando_SQL ="INSERT INTO funcionario (nome, sobrenome, cargo, rg, cpf, datadeNascimento, telefone, celular, logradouro, cidade, cep, salario, horaentrar, horasaida) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            dadosfuncionario = (str(campoNome),str(campoSobrenome), str(campoCargo), str(campoRg), str(campoCpf), str(campoDataNascimento),
                                str(campoTelefone), str(campoCelular), str(campoLogradouro), str(campoCidade), str(campoCep),
                                str(campoCampoSalario),str(campoHoraentrada), str(campoHorasaida))
            cursor.execute(comando_SQL, dadosfuncionario)                
            banco.commit()
            QMessageBox.about(janelainserir, "OK!", "Funcionario cadastrado com sucesso.")
            linhafuncionario = listarfuncionario.tabelaFuncionarios.reset()
            
            campoNome           = funcionario.txtNome.setText("")
            campoSobrenome      = funcionario.txtSobrenome.setText("")
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
            #linhafuncionario = listarfuncionario.tabelaFuncionarios.clear()
            linhafuncionario = listarfuncionario.tabelaFuncionarios.reset()
            Listarfuncionario()
        except:
            QMessageBox.about(janelainserir, "OK!", "Erro ao cadastrar funcionário.")
        
def ListarBuscar():
        listarfuncionario.show()


def Listarfuncionario():
    #linhafuncionario = listarfuncionario.tabelaFuncionarios.clear()
    linhafuncionario = listarfuncionario.tabelaFuncionarios.reset()

    cursor = banco.cursor()
    comando_SQL = "SELECT nome, sobrenome, cargo, rg, cpf, datadeNascimento, telefone, celular, logradouro, cidade, cep, salario, horaentrar, horasaida FROM funcionario"
    cursor.execute(comando_SQL)
    funcionarioLido = cursor.fetchall()

    listarfuncionario.tabelaFuncionarios.setRowCount(len(funcionarioLido))
    listarfuncionario.tabelaFuncionarios.setColumnCount(14)

    for linhas in range(0, len(funcionarioLido)): 
        for colunas in range(0,14):
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
        # listarfuncionario.tabelaFuncionarios.clear()
        listarfuncionario.tabelaFuncionarios.reset()                
        Listarfuncionario()
        
    elif (pergunta == QMessageBox.No):        
        Listarfuncionario()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR") 

'''
def Excluirfuncionario(): 
    
    linhafuncionario = listarfuncionario.tabelaFuncionarios.currentRow()
    listarfuncionario.tabelaFuncionarios.removeRow(linhafuncionario)  

    cursor = banco.cursor()
    comando_SQL = "SELECT id_funcionario FROM funcionario"
    cursor.execute(comando_SQL)
    funcionariosLido = cursor.fetchall()
    valorId = funcionariosLido[linhafuncionario][0]
    cursor.execute("DELETE FROM funcionario WHERE id_funcionario = " + str(valorId))
    banco.commit()
'''

def AlterarFuncionario():

    cursor = banco.cursor()
    comando_SQL = "SELECT id_funcionario From funcionario"
    cursor.execute(comando_SQL)
    funcionario_lidos = cursor.fetchall()

    for linha in range(0, len(funcionario_lidos)):
        valorId          = funcionario_lidos[linha][0]
        nome             = listarfuncionario.tabelaFuncionarios.item(linha, 0).text().upper()
        sobrenome        = listarfuncionario.tabelaFuncionarios.item(linha, 1).text().upper()
        cargo            = listarfuncionario.tabelaFuncionarios.item(linha, 2).text().upper()
        rg               = listarfuncionario.tabelaFuncionarios.item(linha, 3).text().upper()
        cpf              = listarfuncionario.tabelaFuncionarios.item(linha, 4).text()
        datadeNascimento = listarfuncionario.tabelaFuncionarios.item(linha, 5).text()
        telefone         = listarfuncionario.tabelaFuncionarios.item(linha, 6).text()
        celular          = listarfuncionario.tabelaFuncionarios.item(linha, 7).text()
        logradouro       = listarfuncionario.tabelaFuncionarios.item(linha, 8).text().upper()
        cidade           = listarfuncionario.tabelaFuncionarios.item(linha, 9).text().upper()
        cep              = listarfuncionario.tabelaFuncionarios.item(linha, 10).text().upper()
        salario          = listarfuncionario.tabelaFuncionarios.item(linha, 11).text().replace(",",".")
        horaentrar       = listarfuncionario.tabelaFuncionarios.item(linha, 12).text()
        horasaida        = listarfuncionario.tabelaFuncionarios.item(linha, 13).text()

        cursor.execute("UPDATE funcionario SET "
                       "nome = '"+ str(nome) + "', "
                       "sobrenome = '"+ str(sobrenome) + "', "
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
        

def gerarPDFFuncionario():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM funcionario"
    cursor.execute(comando_SQL)
    funcionario_lidos = cursor.fetchall()

    y = 0
    pdf = canvas.Canvas("lista_funcionario.pdf")
    pdf.setFont("Times-Bold", 10)
    pdf.drawString(200, 800, "Lista de Funcionario")

    pdf.setFont("Times-Bold", 10)
    #pdf.drawString(10, 750, "ID")
    pdf.drawString(50, 750, "NOME")
    pdf.drawString(220, 750, "CARGO")
    pdf.drawString(350, 750, "RG")
    pdf.drawString(450, 750, "CPF")
    pdf.drawString(530, 750, "SALARIO")
    #pdf.drawString(510, 750, "DATANASCIMENTO")
    #pdf.drawString(610, 750, "TELEFONE")
    #pdf.drawString(710, 750, "CELULAR")
    #pdf.drawString(810, 750, "LOGRADOURO")
    #pdf.drawString(910, 750, "CIDADE")
    #pdf.drawString(1010, 750, "CEP")
    #pdf.drawString(1110, 750, "SALARIO")
    #pdf.drawString(1210, 750, "HORAENTRADA")
    #pdf.drawString(1310, 750, "HORAENTRADA")

    for i in range(0, len(funcionario_lidos)):
        y = y + 20
        #pdf.drawString(10, 750 - y, str(funcionario_lidos[i][0]))
        pdf.drawString(50, 750 - y, str(funcionario_lidos[i][1]))
        pdf.drawString(220, 750 - y, str(funcionario_lidos[i][2]))
        pdf.drawString(350, 750 - y, str(funcionario_lidos[i][3]))
        pdf.drawString(450, 750 - y, str(funcionario_lidos[i][4]))
        #pdf.drawString(510, 750 - y, str(funcionario_lidos[i][5]))
        #pdf.drawString(610, 750 - y, str(funcionario_lidos[i][6]))
        #pdf.drawString(710, 750 - y, str(funcionario_lidos[i][7]))
        #pdf.drawString(810, 750 - y, str(funcionario_lidos[i][8]))
        #pdf.drawString(910, 750 - y, str(funcionario_lidos[i][9]))
        #pdf.drawString(1010, 750 - y, str(funcionario_lidos[i][10]))
        pdf.drawString(530, 750 - y, str(funcionario_lidos[i][11]))
        #pdf.drawString(1210, 750 - y, str(funcionario_lidos[i][12]))
        #pdf.drawString(1310, 750 - y, str(funcionario_lidos[i][13]))

    pdf.save()
    QMessageBox.about(janelainserir, "OK!", "PDF gerado com sucesso.")





programapetshop=QtWidgets.QApplication([])
funcionario= uic.loadUi("Funcionario.ui")
funcionario.btnCadastrarfuncionario.clicked.connect(Cadastrarfuncionario)
funcionario.btnListarfuncionarios.clicked.connect(ListarBuscar)
#listarfuncionario = uic.loadUi("listafuncionario.ui")
#funcionario.btnListarBuscarfuncionarios.clicked.connect(Listarfuncionario)

listarfuncionario = uic.loadUi("listafuncionario.ui")
listarfuncionario.btnListarFuncionario.clicked.connect(Listarfuncionario)
listarfuncionario.btnExcluirFuncionario.clicked.connect(Excluirfuncionario)
listarfuncionario.btnAlterar.clicked.connect(AlterarFuncionario)
listarfuncionario.btnGerarPdf.clicked.connect(gerarPDFFuncionario)



janelainserir = uic.loadUi("Petmensageminsere.ui")


funcionario.show()
programapetshop.exec()

