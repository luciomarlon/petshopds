from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(host = "localhost", user = "root",password = "",database = "petshop")

def Cadastrar():
    listadeservicos = cadastracategoria.tabelaCategorias.reset()

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
            listadeservicos = cadastracategoria.tabelaCategorias.reset()
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
        listadeservicos = cadastracategoria.tabelaCategorias.reset()
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
        #cadastracategoria.tabelaCategorias.clear()
        cadastracategoria.tabelaCategorias.reset()
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
            #cadastracategoria.tabelaCategorias.clear()
            cadastracategoria.tabelaCategorias.reset()
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
            # cadastracategoria.tabelaCategorias.clear()
            cadastracategoria.tabelaCategorias.reset()
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


petshopcliente = QtWidgets.QApplication([])
cadastracategoria = uic.loadUi("Categoria.ui")

cadastracategoria.btnCadastrar.clicked.connect(Cadastrar)
cadastracategoria.btnListarCategoria.clicked.connect(Listar)
cadastracategoria.btnExcluir.clicked.connect(Excluir)
cadastracategoria.btnAlteracoes.clicked.connect(Alterar)

janelainserir = uic.loadUi("Petmensageminsere.ui")

cadastracategoria.show()
petshopcliente.exec()