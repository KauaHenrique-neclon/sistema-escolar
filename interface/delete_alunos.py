import tkinter
import customtkinter
import psycopg2

class deletar_alunos():
    def __init__(self):
        self.janela_deletar = tkinter.Tk()
        self.janela_deletar.title('Deletar Aluno')
        self.janela_deletar.configure(background='#d6dee2')
        self.janela_deletar.attributes('-fullscreen', True)

        ############
        ####### construção do frame para consultar
        label_indicando = customtkinter.CTkLabel(master=self.janela_deletar,width=900,height=40,fg_color='transparent',bg_color='transparent',text='Deseja deletar aluno',text_color='black',font=("Arial bold",18))
        label_indicando.place(relx=0.18,rely=0.05)
        self.frame_insirir = customtkinter.CTkFrame(master=self.janela_deletar,width=450,height=400,fg_color='white',bg_color='transparent')
        self.frame_insirir.place(relx=0.06,rely=0.14)
        label_insirir = customtkinter.CTkLabel(master=self.frame_insirir,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Insere os dados',text_color='black',font=("Arial bold",16))
        label_insirir.place(relx=0.18,rely=0.05)
        label_cpf = customtkinter.CTkLabel(master=self.frame_insirir,width=200,height=40,fg_color='transparent',bg_color='transparent',text='CPF do aluno',text_color='black')
        label_cpf.place(relx=0.03,rely=0.13)
        self.input_cpf = customtkinter.CTkEntry(master=self.frame_insirir,width=200,height=40,bg_color='transparent',fg_color='#d6dee2')
        self.input_cpf.place(relx=0.4,rely=0.13)
        button_consultar = customtkinter.CTkButton(master=self.frame_insirir,width=300,height=30,fg_color="#0097b2",bg_color='transparent',text='Deletar Aluno',text_color='white',command=self.validar_entrada_cpf_delete)
        button_consultar.place(relx=0.17,rely=0.3)
    

    #############
    ####### função para validar os 11 digitos do CPF
    def validar_entrada_cpf_delete(self):
        cpf = self.input_cpf.get()
        if len(cpf) == 11 and cpf.isdigit():
            self.buscando_dados()
            self.mostrando_resultado_aluno()
        else:
            self.aviso_insira_11_digito_cpf()
    

    ##################
    ###### função para buscar os dados do aluno para informar
    def buscando_dados(self):
        try:
            cpf = self.input_cpf.get()
            connec = psycopg2.connect(database = "sistema", host= "localhost", user = "postgres",password="5115",port="5432")
            sql_buscar_nome = "SELECT nome FROM aluno_info WHERE cpf = %s"
            sql_sobrenome = "SELECT sobrenome FROM aluno_info WHERE cpf = %s"
            sql_idade = "SELECT idade FROM aluno_info WHERE cpf = %s"
            sql_id = "SELECT id FROM notas WHERE cpf = %s"
            cursor = connec.cursor()
            cursor.execute(sql_buscar_nome, (str(cpf),))
            self.cpf_aluno_result = cursor.fetchone()

            cursor.execute(sql_sobrenome, (str(cpf),))
            self.sobrenome = cursor.fetchone()

            cursor.execute(sql_idade, (str(cpf),))
            self.idade = cursor.fetchone()

            cursor.execute(sql_id, (str(cpf),))
            self.id = cursor.fetchone()

            cursor.close()
            connec.close()
        except psycopg2.Error:
            self.aviso_erro_serve()
        

    ##################
    ######## função para mostrar o resultado da buscas dos dados
    def mostrando_resultado_aluno(self):
        self.frame_info_aluno = customtkinter.CTkFrame(master=self.janela_deletar,width=600,height=350,fg_color='white',bg_color='transparent')
        self.frame_info_aluno.place(relx=0.5,rely=0.3)
        label_info = customtkinter.CTkLabel(master=self.frame_info_aluno,width=400,height=30,fg_color='transparent',bg_color='transparent',text='Informações do aluno a ser deletado',text_color='black',font=("Arial bold",18))
        label_info.place(relx=0.2,rely=0.07)
        label_nome_aluno = customtkinter.CTkLabel(master=self.frame_info_aluno,width=400,height=30,fg_color='transparent',bg_color='transparent',text=f'Quer apagar o {str(self.cpf_aluno_result[0])} do sistema',text_color='black',font=("Arial bold",16))
        label_nome_aluno.place(relx=0.11,rely=0.2)
        label_sobrenome = customtkinter.CTkLabel(master=self.frame_info_aluno,width=400,height=30,fg_color='transparent',bg_color='transparent',text=f'Sobrenome do aluno: {str(round(self.sobrenome))}',text_color='black',font=("Arial bold",16))
        label_sobrenome.place(relx=0.11,rely=0.35)
        label_idade = customtkinter.CTkLabel(master=self.frame_info_aluno,width=400,height=30,fg_color='transparent',bg_color='transparent',text=f'Ano de nascimento: {str(round(self.idade))}',text_color='black',font=("Arial bold",16))
        label_idade.place(relx=0.11,rely=0.55)
        label_id = customtkinter.CTkLabel(master=self.frame_info_aluno,width=400,height=30,fg_color='transparent',bg_color='transparent',text=f'Id do aluno: {str(round(self.id[0]))}',text_color='black',font=("Arial bold",16))
        label_id.place(relx=0.11,rely=0.75)
        button_apagar = customtkinter.CTkButton(master=self.frame_info_aluno,width=200,height=30,fg_color="#0097b2",bg_color='transparent',text='Deletar',text_color='white',command=self.deletando_aluno)
        button_apagar.place(relx=0.3,rely=0.87)
    

    ###############################
    ############ função para deletar o aluno do banco de dados
    def deletando_aluno(self):
        try:
            cpf = self.input_cpf.get()
            connec = psycopg2.connect(database = "sistema", host= "localhost", user = "postgres",password="5115",port="5432")
            cursor = connec.cursor()
            sql_delete = "DELETE FROM aluno_info,aulas_alunos,financeiro,notas WHERE cpf = %s"
            cursor.execute(sql_delete, (str(cpf),))
            cursor.close()
            connec.close()
            self.aviso_delete_sucesso()
        except psycopg2.Error:
            self.aviso_erro_serve()
    

    ##############################
    ########## função para mostra um aviso de deletado com sucesso
    def aviso_delete_sucesso(self):
        self.frame_aviso_sucesso = customtkinter.CTkFrame(master=self.frame_insirir,width=400,height=120,fg_color="#0097b2",bg_color='transparent')
        self.frame_aviso_sucesso.place(relx=0.06,rely=0.6)
        label_aviso_sucesso = customtkinter.CTkLabel(master=self.frame_aviso_sucesso,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Deletado com sucesso',text_color='white',font=('Arial bold',18))
        label_aviso_sucesso.place(relx=0.25,rely=0.2)
        label_aviso_sucesso_2 = customtkinter.CTkLabel(master=self.frame_aviso_sucesso,width=200,height=30,fg_color='transparent',bg_color='transparent',text='O Aluno foi deletado com suceesso',text_color='white',font=('Arial bold',17))
        label_aviso_sucesso_2.place(relx=0.2,rely=0.5)
    

    ##########################
    ########### função que mostra um aviso de erro no servidor
    def aviso_erro_serve(self):
        self.frame_erro_serve = customtkinter.CTkFrame(master=self.frame_insirir,width=400,height=120,fg_color="#0097b2",bg_color='transparent')
        self.frame_erro_serve.place(relx=0.06,rely=0.6)
        label_aviso_erro = customtkinter.CTkLabel(master=self.frame_erro_serve,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Erro serve',text_color='white',font=('Arial bold',18))
        label_aviso_erro.place(relx=0.25,rely=0.2)
        label_aviso_erro_2 = customtkinter.CTkLabel(master=self.frame_erro_serve,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Parece que o server caiu',text_color='white',font=('Arial bold',17))
        label_aviso_erro_2.place(relx=0.25,rely=0.5)
    

    ################################
    ############ função para mostrar um aviso de erro ao insirir o cpf
    def aviso_insira_11_digito_cpf(self):
        self.frame_erro_cpf = customtkinter.CTkFrame(master=self.frame_insirir,width=400,height=120,fg_color="#0097b2",bg_color='transparent')
        self.frame_erro_cpf.place(relx=0.06,rely=0.6)
        label_erro_cpf = customtkinter.CTkLabel(master=self.frame_erro_cpf,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Insira certo',text_color='white',font=('Arial bold',18))
        label_erro_cpf.place(relx=0.25,rely=0.2)
        label_aviso_erro_cpf = customtkinter.CTkLabel(master=self.frame_erro_cpf,width=200,height=30,fg_color='transparent',bg_color='transparent',text='Insira os 11 digito do cpf',text_color='white',font=('Arial bold',17))
        label_aviso_erro_cpf.place(relx=0.25,rely=0.5)

def chamando_delete():
    app = deletar_alunos()
    app.janela_deletar.mainloop()