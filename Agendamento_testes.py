from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from reportlab.pdfgen import canvas
from datetime import datetime, timezone

banco = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "petshop")


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
                #agendamentospets = petagendamento.tabelaAgendamento.clear()
                agendamentospets = petagendamento.tabelaAgendamento.reset()
                ListarAgendamento() 
            except:
                QMessageBox.about(janelainserir, "OK!", "Erro a cadastrar Pet.")

def ListarAgendamento():        

        agendamentospets = petagendamento.tabelaAgendamento.reset()       
        cursor = banco.cursor()                       
        comando_SQL = "SELECT  nomepet, especie, porte, peso, datas, horario, valorservico, nomeprofissional, procedimento, realizado FROM agendamento"
        cursor.execute(comando_SQL)        
        listapetsporcliente = cursor.fetchall()        

        petagendamento.tabelaAgendamento.setRowCount(len(listapetsporcliente))
        petagendamento.tabelaAgendamento.setColumnCount(10)

        for linhas in range(0, len(listapetsporcliente)):
            for colunas in range(0, 10):
                petagendamento.tabelaAgendamento.setItem(linhas, colunas,QtWidgets.QTableWidgetItem(str(listapetsporcliente[linhas][colunas])))
                

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
        #petagendamento.tabelaAgendamento.clear()
        petagendamento.tabelaAgendamento.reset()
        ListarAgendamento() 
    
    elif (pergunta == QMessageBox.No):
        ListarAgendamento()
        
    else:   
        QMessageBox.about(janelainserir, "OK!", "Selecione um registro para\nEXCLUIR") 

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
    #pdf.drawString(10, 750, "ID")
    pdf.drawString(10, 750, "NOMEPET")
    pdf.drawString(80, 750, "ESPECIE")
    #pdf.drawString(140, 750, "PORTE")
    pdf.drawString(140, 750, "PESO")
    pdf.drawString(180, 750, "DATAS")
    pdf.drawString(250, 750, "HORARIO")
    pdf.drawString(310, 750, "VALOR")
    pdf.drawString(370, 750, "PROFISSIONAL")
    pdf.drawString(480, 750, "PROCEDIMENTO")
    #pdf.drawString(370, 750, "REALIZADO")


    for i in range(0, len(agendamento_lidos)):
        y = y + 20
        #pdf.drawString(10, 750 - y, str(agendamento_lidos[i][0]))
        pdf.drawString(10, 750 - y, str(agendamento_lidos[i][1]))
        pdf.drawString(80, 750 - y, str(agendamento_lidos[i][2]))
        #pdf.drawString(140, 750 - y, str(agendamento_lidos[i][3]))
        pdf.drawString(140, 750 - y, str(agendamento_lidos[i][4]))
        pdf.drawString(180, 750 - y, str(agendamento_lidos[i][5]))
        pdf.drawString(250, 750 - y, str(agendamento_lidos[i][6]))
        pdf.drawString(310, 750 - y, str(agendamento_lidos[i][7]))
        pdf.drawString(370, 750 - y, str(agendamento_lidos[i][8]))
        pdf.drawString(480, 750 - y, str(agendamento_lidos[i][9]))
        #pdf.drawString(1010, 750 - y, str(agendamento_lidos[i][10]))


    pdf.save()
    QMessageBox.about(janelainserir, "OK!", "PDF gerado com sucesso.")


 
petshopcliente = QtWidgets.QApplication([])
petagendamento = uic.loadUi("AgendamentoLista.ui")
petagendamento.btnListarAgendamento.clicked.connect(ListarAgendamento)
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



petagendamento.show()
petshopcliente.exec()
