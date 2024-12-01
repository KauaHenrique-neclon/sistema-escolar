import tkinter
import customtkinter
import psycopg2
from PIL import ImageTk,Image
import datetime
from time import sleep

class parte_finanças():
    ######################
    ###### codigo de interface do financeiro
    def __init__(self):
        self.janela_fina = tkinter.Tk()
        self.janela_fina.attributes('-fullscreen', True)
        self.janela_fina.configure(background='white')
        self.janela_fina.title('Financeiro')
        
        ###################
        ###### bloco do cabeçario da janela
        frame_de_busca = customtkinter.CTkFrame(master=self.janela_fina,fg_color='#c77dff',width=1100,height=50,bg_color='transparent')
        frame_de_busca.place(relx=0.088, rely=0.04)
        button_menu = customtkinter.CTkButton(master=frame_de_busca,width=100,height=30,fg_color='transparent',bg_color='transparent',text='Menu',text_color='white',hover_color='#6b3fa0',font=('Arial bold',17),command=self.voltando_menu)
        button_menu.place(relx=0.06,rely=0.2)
        hora = datetime.datetime.now().strftime('%H:%M')
        hora_label = customtkinter.CTkLabel(master=frame_de_busca,width=100,height=30,fg_color='transparent',bg_color='transparent',text=f'{hora}',text_color='white',font=('Arial bold',17))
        hora_label.place(relx=0.9,rely=0.2)
       
        ###############################
        ###### bloco da frase da matricula entre o cabeçario e o bloco do aluno
        frame_incio = customtkinter.CTkFrame(master=self.janela_fina,width=1100,height=50,fg_color='transparent',bg_color='transparent')
        frame_incio.place(relx=0.088,rely=0.12)
        label_aviso_matricula = customtkinter.CTkLabel(master=frame_incio,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Financeiro da matrícula do aluno',text_color='black',font=('Arial bold',17))
        label_aviso_matricula.place(relx=0.35,rely=0.2)
        
        ###########################################
        ############# bloco de consultar o aluno pelo CPF, embaixo da frase financeiro
        self.frame_de_busca_aluno = customtkinter.CTkFrame(master=self.janela_fina,width=400,height=500,bg_color='transparent',fg_color='#c77dff')
        self.frame_de_busca_aluno.place(relx=0.088,rely=0.2)
        label_inicial = customtkinter.CTkLabel(master=self.frame_de_busca_aluno,width=300,height=50,fg_color='transparent',bg_color='transparent',text='Consultar a ficha de pagamento',text_color='white',font=('Arial bold',17))
        label_inicial.place(relx=0.15,rely=0.1)
        label_colocar_cpf = customtkinter.CTkLabel(master=self.frame_de_busca_aluno,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Insira o CPF do aluno',text_color='white',font=('Arial bold',17))
        label_colocar_cpf.place(relx=0.15,rely=0.3)
        self.input_cpf = customtkinter.CTkEntry(master=self.frame_de_busca_aluno,width=300,height=30,fg_color='white',bg_color='transparent')
        self.input_cpf.place(relx=0.15,rely=0.45)
        button_submit = customtkinter.CTkButton(master=self.frame_de_busca_aluno,width=300,height=30,fg_color='white',bg_color='transparent',text='Consultar',text_color='black',hover_color='#6b3fa0',command=self.validar_cpf)
        button_submit.place(relx=0.15,rely=0.6)
    
    #################################
    ####### função de mostrar um bloco dizendo que o CPF é invalido 
    def cpf_invalido_busca_aluno(self):
        self.frame_aviso_cpf_busca_aluno = customtkinter.CTkFrame(master=self.frame_de_busca_aluno,width=400,height=200,fg_color='#d3d3d3',bg_color='transparent')
        self.frame_aviso_cpf_busca_aluno.place(relx=0,rely=0.75)
        label_titulo = customtkinter.CTkLabel(master=self.frame_aviso_cpf_busca_aluno,width=400,height=30,fg_color='transparent',bg_color='transparent',text='CPF invalido',text_color='black',font=('Arial bold',17))
        label_titulo.place(relx=0,rely=0.05)
        label_aviso = customtkinter.CTkLabel(master=self.frame_aviso_cpf_busca_aluno,width=400,height=30,fg_color='transparent',bg_color='transparent',text='Entre com um CPF valido')
        label_aviso.place(relx=0,rely=0.5)
        sleep(5)
        self.frame_aviso_cpf_busca_aluno.destroy()

    ######################################
    ############## função que mostra um bloco dizendo q CPF não existe no banco de dados do aluno
    def cpf_nao_existe(self):
        self.frame_aviso_cpf = customtkinter.CTkFrame(master=self.frame_de_busca_aluno,width=400,height=200,fg_color='#d3d3d3',bg_color='transparent')
        self.frame_aviso_cpf.place(relx=0,rely=0.75)
        label_titulo = customtkinter.CTkLabel(master=self.frame_aviso_cpf,width=400,height=30,fg_color='transparent',bg_color='transparent',text='CPF invalido',text_color='black',font=('Arial bold',17))
        label_titulo.place(relx=0,rely=0.05)
        label_aviso_cpf = customtkinter.CTkLabel(master=self.frame_aviso_cpf,width=400,height=30,fg_color='transparent',bg_color='transparent',text='CPF não existe no banco do aluno')
        label_aviso_cpf.place(relx=0,rely=0.5)
        sleep(5)
        self.frame_aviso_cpf.destroy()
    
    #########################################
    ########## função que mostra um bloco dizendo que o servidor caiu
    def erro_no_serve_busca_aluno(self):
        self.frame_serve_caiu = customtkinter.CTkFrame(master=self.frame_de_busca_aluno,width=400,height=200,fg_color='#d3d3d3',bg_color='transparent')
        self.frame_serve_caiu.place(relx=0,rely=0.75)
        label_titulo = customtkinter.CTkLabel(master=self.frame_serve_caiu,width=400,height=30,fg_color='transparent',bg_color='transparent',text='Erro no serve',text_color='black',font=('Arial bold',17))
        label_titulo.place(relx=0,rely=0.05)
        label_aviso_serve = customtkinter.CTkLabel(master=self.frame_serve_caiu,width=400,height=30,fg_color='transparent',bg_color='transparent',text='Servidor indisponivel no momento')
        label_aviso_serve.place(relx=0,rely=0.5)
        sleep(5)
        self.frame_serve_caiu.destroy()
    
    ###################################################
    ########### beckend do consltar aluno #############
    ###################################################
    
    ###################################
    ###### função que valida a entrada do CPF
    def validar_cpf(self):
        cpf = self.input_cpf.get()
        if len(cpf) == 11 and cpf.isdigit():
            self.verificar_cpf_existe_info_aluno()
        else:
            self.cpf_invalido_busca_aluno()

    ##################################
    ########### função que verifica se o CPF existe no banco de dados da informação do aluno
    def verificar_cpf_existe_info_aluno(self):
        try:
            cpf_aluno = self.input_cpf.get()
            self.banco_de_dados()
            cursor = self.conexao_sistema.cursor()
            sql_query = "SELECT cpf FROM aluno_info WHERE cpf = %s"
            cursor.execute(sql_query, (str(cpf_aluno),))
            self.resultado_verificar = cursor.fetchone()
            if self.resultado_verificar is not None:
                self.pegar_nome()
                self.reesultado_info_cpf()
            else:
                self.cpf_nao_existe()
        except:
            self.erro_no_serve_busca_aluno()
    
    #################################################
    ######### função com a conexão ao banco de dados
    def banco_de_dados(self):
        self.conexao_sistema = psycopg2.connect(database = "sistema", host= "localhost", user = "postgres",password="5115",port="5432")
    

    ############################
    ############ função que volta para a inserir e consultar novamente 
    def button_voltar_resultado(self):
        self.input_cpf.delete(0,100)
        self.frame_resultado_consulta.destroy()
    
    ##################################
    ####### função que pega o nome e sobrenome dos alunos atraves do CPF
    def pegar_nome(self):
        try:
            cpf = self.input_cpf.get()
            self.banco_de_dados()
            sql_query = "SELECT nome FROM aluno_info WHERE cpf = %s"
            cursor = self.conexao_sistema.cursor()
            cursor.execute(sql_query, (str(cpf),))
            self.nome = cursor.fetchone()

            sql_query_2 = "SELECT sobrenome FROM aluno_info WHERE cpf = %s"
            cursor.execute(sql_query_2,(str(cpf),))
            self.sobrenome = cursor.fetchone()
        except:
            pass

    ############################################################################
    ###################### interface da segunda parte ##########################
    ############################################################################


    
    #####################################
    ########## função que mostra um bloco da infomação do aluno consultado
    def reesultado_info_cpf(self):
        self.frame_resultado_consulta = customtkinter.CTkFrame(master=self.janela_fina,width=500,height=200,bg_color='transparent',fg_color='#c77dff')
        self.frame_resultado_consulta.place(relx=0.5,rely=0.2)
        label_inicial_consulta = customtkinter.CTkLabel(master=self.frame_resultado_consulta,width=300,height=30,bg_color='transparent',fg_color='transparent',text='Um rapido resumo',text_color='black',font=('Arial bold',17))
        label_inicial_consulta.place(relx=0.2,rely=0.1)
        label_nome_aluno = customtkinter.CTkLabel(master=self.frame_resultado_consulta,width=300,height=30,fg_color='transparent',bg_color='transparent',text=f'Nome do aluno: {str(self.nome[0])}',text_color='black',font=('Arial bold',17))
        label_nome_aluno.place(relx=0.2,rely=0.3)
        label_sobrenome_aluno = customtkinter.CTkLabel(master=self.frame_resultado_consulta,width=300,height=30,fg_color='transparent',bg_color='transparent',text=f'Sobrenome do aluno: {str(self.sobrenome[0])}',text_color='black',font=('Arial bold',17))
        label_sobrenome_aluno.place(relx=0.2,rely=0.5)
        button_continuar = customtkinter.CTkButton(master=self.frame_resultado_consulta,width=150,height=30,bg_color='transparent',text='continuar',text_color='white',font=('Arial bold',17),command=self.parcela)
        button_continuar.place(relx=0.15,rely=0.8)
        button_voltar = customtkinter.CTkButton(master=self.frame_resultado_consulta,width=150,height=30,bg_color='transparent',text='voltar',text_color='white',font=('Arial bold',17),command=self.button_voltar_resultado)
        button_voltar.place(relx=0.55,rely=0.8)



    ############################################
    ############ função mais importante do arquivo
    ############ função que mostra um bloco para ser inserido os dados para salvar os dados
    def parcela(self):
        self.frame_resultado_consulta.destroy()
        self.frame_de_busca_aluno.destroy()
        self.frame_primeira_parcela = customtkinter.CTkFrame(master=self.janela_fina,width=500, height=500, fg_color='#c77dff',bg_color='transparent')
        self.frame_primeira_parcela.place(relx=0.3,rely=0.2)
        label_incial = customtkinter.CTkLabel(master=self.frame_primeira_parcela,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Preencha o requisito',text_color='black',font=('Arial bold',18))
        label_incial.place(relx=0.2,rely=0.05)
        label_data = customtkinter.CTkLabel(master=self.frame_primeira_parcela,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Data:',text_color='black')
        label_data.place(relx=0.05,rely=0.13)
        self.input_data = customtkinter.CTkEntry(master=self.frame_primeira_parcela,width=200,height=30,placeholder_text="dd/mm/aaaa",fg_color='#d3d3d3',bg_color='transparent')
        self.input_data.place(relx=0.5,rely=0.13)
        label_valor = customtkinter.CTkLabel(master=self.frame_primeira_parcela,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Valor',text_color='black')
        label_valor.place(relx=0.05,rely=0.25)
        self.input_valor = customtkinter.CTkEntry(master=self.frame_primeira_parcela,width=200,height=30,fg_color='#d3d3d3',bg_color='transparent')
        self.input_valor.place(relx=0.5,rely=0.25)
        label_forma_pagamento = customtkinter.CTkLabel(master=self.frame_primeira_parcela,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Forma de pagamento',text_color='black')
        label_forma_pagamento.place(relx=0.05,rely=0.37)
        self.input_pagamento = customtkinter.CTkEntry(master=self.frame_primeira_parcela,width=200,height=30,fg_color='#d3d3d3',bg_color='transparent')
        self.input_pagamento.place(relx=0.5,rely=0.37)
        label_mes = customtkinter.CTkLabel(master=self.frame_primeira_parcela,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Mes da parcela',text_color='black')
        label_mes.place(relx=0.05,rely=0.49)
        self.input_mes = customtkinter.CTkEntry(master=self.frame_primeira_parcela,width=200,height=30,fg_color='#d3d3d3',bg_color='transparent')
        self.input_mes.place(relx=0.5,rely=0.49)
        label_status = customtkinter.CTkLabel(master=self.frame_primeira_parcela,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Status:',text_color='black')
        label_status.place(relx=0.05,rely=0.61)
        self.input_status = customtkinter.CTkEntry(master=self.frame_primeira_parcela,width=200,height=30,fg_color='#d3d3d3',bg_color='transparent',placeholder_text="PG ou NP")
        self.input_status.place(relx=0.5,rely=0.61)
        label_codigo_barra = customtkinter.CTkLabel(master=self.frame_primeira_parcela,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Codigo:',text_color='black')
        label_codigo_barra.place(relx=0.05,rely=0.73)
        self.input_codigo = customtkinter.CTkEntry(master=self.frame_primeira_parcela,width=200,height=30,fg_color='#d3d3d3',bg_color='transparent',placeholder_text="codigo de barra")
        self.input_codigo.place(relx=0.5,rely=0.73)
        button_submit = customtkinter.CTkButton(master=self.frame_primeira_parcela,width=200,height=30,text='Salvar',bg_color='transparent',text_color='white',command=self.validar_data)
        button_submit.place(relx=0.3,rely=0.85)




    #############################################
    ######## função que mostra um bloco dizendo que data é invalida
    def data_invalida(self):
        self.frame_data_invalido = customtkinter.CTkFrame(master=self.janela_fina,width=500,height=70,fg_color='#87cefa',bg_color='transparent')
        self.frame_data_invalido.place(relx=0.3,rely=0.81)
        label_titulo = customtkinter.CTkLabel(master=self.frame_data_invalido,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Data invalida',text_color='black',font=('Arial bold',18))
        label_titulo.place(relx=0.2,rely=0.06)
        label_data_errada = customtkinter.CTkLabel(master=self.frame_data_invalido,width=500,height=30,fg_color='transparent',bg_color='transparent',text='Insira a data de maneira correta',text_color='black',font=('Arial bold',16))
        label_data_errada.place(relx=0,rely=0.45)
        self.delete_input()
        sleep(5)
        self.frame_data_invalido.destroy()
    
    #####################################
    ####### função que mostra um bloco dizendo que o codigo de barra é invalido
    def erro_codigo_barra(self):
        self.frame_codigo_invalido = customtkinter.CTkFrame(master=self.janela_fina,width=500,height=70,fg_color='#87cefa',bg_color='transparent')
        self.frame_codigo_invalido.place(relx=0.3,rely=0.81)
        label_titulo = customtkinter.CTkLabel(master=self.frame_data_invalido,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Codigo de barra invalida',text_color='black',font=('Arial bold',18))
        label_titulo.place(relx=0.2,rely=0.06)
        label_codigo_errada = customtkinter.CTkLabel(master=self.frame_data_invalido,width=500,height=30,fg_color='transparent',bg_color='transparent',text='Insira o codigo com 13 numeros',text_color='black',font=('Arial bold',16))
        label_codigo_errada.place(relx=0,rely=0.45)
        self.delete_input()
        sleep(5)
        self.frame_codigo_invalido.destroy()
    
    #####################################
    ############ função que mostra um bloco dizendo que o servidor caiu
    def erro_serve(self):
        self.frame_erro_serve = customtkinter.CTkFrame(master=self.janela_fina,width=500,height=70,fg_color='#87cefa',bg_color='transparent')
        self.frame_erro_serve.place(relx=0.3,rely=0.81)
        label_titulo = customtkinter.CTkLabel(master=self.frame_erro_serve,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Erro servidor',text_color='black',font=('Arial bold',18))
        label_titulo.place(relx=0.2,rely=0.06)
        label_serve_caiu = customtkinter.CTkLabel(master=self.frame_erro_serve,width=500,height=30,fg_color='transparent',bg_color='transparent',text='Sem acesso ao servidor',text_color='black',font=('Arial bold',16))
        label_serve_caiu.place(relx=0,rely=0.45)
        self.delete_input()
        sleep(5)
        self.frame_erro_serve.destroy()
    
    #####################################
    ####### função que mostra que os dados foram salvos
    def dados_salvo(self):
        self.frame_dados_salvo = customtkinter.CTkFrame(master=self.janela_fina,width=500,height=70,fg_color='#87cefa',bg_color='transparent')
        self.frame_dados_salvo.place(relx=0.3,rely=0.81)
        label_titulo = customtkinter.CTkLabel(master=self.frame_dados_salvo,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Dados Salvo',text_color='black',font=('Arial bold',18))
        label_titulo.place(relx=0.2,rely=0.06)
        label_data_errada = customtkinter.CTkLabel(master=self.frame_dados_salvo,width=500,height=30,fg_color='transparent',bg_color='transparent',text='Dados foram salvos',text_color='black',font=('Arial bold',16))
        label_data_errada.place(relx=0,rely=0.45)
        self.delete_input()
        sleep(5)
        self.frame_dados_salvo.destroy()
        self.frame_primeira_parcela.destroy()
        self.frame_de_busca_aluno


    ####################################################################
    ################# beckeend Salvando os dados #######################
    ####################################################################

    #############################
    ####### função para validar a entrada de dados
    def validar_data(self):
        data = self.input_data.get()
        if len(data) == 10 and data[2] == "/" and data[5] == "/":
            self.validar_codigo_barra()
        else:
            self.data_invalida()
    
    ##################################
    ####### função para validar entrada do codigo de barra
    def validar_codigo_barra(self):
        codigo = self.input_codigo.get()
        if len(codigo) == 13 and codigo.isdigit():
            self.salvando_pagamento()
        else:
            self.erro_codigo_barra()
    
    #################################
    #####33 função para salvar os dados inseridos
    def salvando_pagamento(self):
        try:
            self.banco_de_dados()
            cpf = self.input_cpf.get()
            data_dia = self.input_data.get()
            valor = self.input_valor.get()
            pagamento = self.input_pagamento.get()
            mes = self.input_mes.get()
            status = self.input_status.get()
            codigo = self.input_codigo.get()
            sql_query = "INSERT INTO pagamentos(cpf,datapagamento,valor,formapagamento,nomeparcela,statuspagamento,codigo_barra) VALUES(%s, %s,%s, %s, %s, %s, %s)"
            cursor = self.conexao_sistema.cursor()
            cursor.execute(sql_query, (cpf,data_dia,valor,pagamento, mes, status, codigo))
            self.conexao_sistema.commit()
            self.conexao_sistema.close()
            cursor.close()
            self.dados_salvo()
        except:
            self.erro_serve()
    
    ########################
    ##### função que limpa todos os inputs
    def delete_input(self):
        self.input_cpf.delete(0,100)
        self.input_data.delete(0,100)
        self.input_mes.delete(0,100)
        self.input_pagamento.delete(0,100)
        self.input_status.delete(0,100)
        self.input_valor.delete(0,100)
    
    ##############################
    ###### função para voltar ao menu principal
    def voltando_menu(self):
        self.janela_fina.destroy()
        from menu_pincipal import menu_chamar
        menu_chamar()


def chamando_financeiro():
    app = parte_finanças()
    app.janela_fina.mainloop()

    '''
    comentario, eu fi eu codigo em 01/12/2024, e fiz quando tava terminando meu 2° periodo
    da faculdade, cursando CDC, está muito bagunçado, mas fiz alguns comentario para entender
    um pouco pois nem eu mesmo entendo esse codigo agora
    '''