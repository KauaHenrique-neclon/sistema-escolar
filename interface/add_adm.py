import tkinter
import customtkinter
import psycopg2
import datetime
from time import sleep
import re

class adicionar_adm():
    def __init__(self):
        self.janela_add_adm = tkinter.Tk()
        self.janela_add_adm.configure(background='white')
        self.janela_add_adm.geometry('700x600')
        self.janela_add_adm.title('Adicionar adm')
        self.janela_add_adm.resizable(width=False,height=False)

        ####################################
        ########## frame ou cabeçario de busca da janela add adm
        frame_de_busca = customtkinter.CTkFrame(master=self.janela_add_adm,fg_color='#0097b2',width=600,height=50,bg_color='transparent')
        frame_de_busca.place(relx=0.088, rely=0.04)
        button_menu = customtkinter.CTkButton(master=frame_de_busca,width=100,height=30,fg_color='transparent',bg_color='transparent',text='Menu',text_color='white',hover_color='#054f77',font=('Arial bold',17))
        button_menu.place(relx=0.3,rely=0.2)
        hora = datetime.datetime.now().strftime('%H:%M')
        hora_label = customtkinter.CTkLabel(master=frame_de_busca,width=100,height=30,fg_color='transparent',bg_color='transparent',text=f'{hora}',text_color='white',font=('Arial bold',17))
        hora_label.place(relx=0.7,rely=0.2)
        
        #####################################
        ############# aviso de preencher dados
        label_aviso = customtkinter.CTkLabel(master=self.janela_add_adm,width=300,height=30,text='Preenchar os dados',text_color='black',font=('Arial Bold',17),fg_color='transparent',bg_color='transparent')
        label_aviso.place(relx=0.3,rely=0.15)

        ######################################
        ############ frame para receber os dados do cadastro do adm
        self.frame_dados_adm = customtkinter.CTkFrame(master=self.janela_add_adm,width=500,height=400,fg_color='#d3d3d3',bg_color='transparent')
        self.frame_dados_adm.place(relx=0.15,rely=0.2)
        label_nome = customtkinter.CTkLabel(master=self.frame_dados_adm,width=150,height=30,text='Nome:',text_color='black',font=('Arial bold',16),fg_color='transparent',bg_color='transparent')
        label_nome.place(relx=0.15,rely=0.05)
        self.input_nome = customtkinter.CTkEntry(master=self.frame_dados_adm,width=150,height=30,bg_color='transparent',fg_color='#d3d3d3')
        self.input_nome.place(relx=0.5,rely=0.05)
        label_email = customtkinter.CTkLabel(master=self.frame_dados_adm,width=150,height=30,text='Email:',text_color='black',font=('Arial bold',16),fg_color='transparent',bg_color='transparent')
        label_email.place(relx=0.15,rely=0.2)
        self.input_email = customtkinter.CTkEntry(master=self.frame_dados_adm,width=150,height=30,bg_color='transparent',fg_color='#d3d3d3')
        self.input_email.place(relx=0.5,rely=0.2)
        label_senha = customtkinter.CTkLabel(master=self.frame_dados_adm,width=150,height=30,text='Senha:',text_color='black',font=('Arial bold',16),fg_color='transparent',bg_color='transparent')
        label_senha.place(relx=0.15,rely=0.35)
        self.input_senha = customtkinter.CTkEntry(master=self.frame_dados_adm,width=150,height=30,bg_color='transparent',fg_color='#d3d3d3')
        self.input_senha.place(relx=0.5,rely=0.35)
        ### button de sunmit
        button_submit = customtkinter.CTkButton(master=self.frame_dados_adm,width=200,height=30,fg_color='#0097b2',bg_color='transparent',text='Adicionar adm',text_color='black',font=('Arial bold',16),command=self.verificar_email)
        button_submit.place(relx=0.3,rely=0.50)


    #####################################
    ####### função de verificar email se é válido
    def verificar_email(self):
        email = self.input_email.get()
        padrão = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|gov|org)$"
        if re.match(padrão, email, re.IGNORECASE):
            self.verificar_senha()
        else:
            self.aviso_email_invalido()
    
    ##################################
    ###### verificar senha se é válida
    def verificar_senha(self):
        senha = self.input_senha.get()
        if len(senha) >= 8 and senha.isdigit():
            self.cadastro_autorizado()
        else:
            self.senha_invalida()

    ##################################
    ###### função de salvar dados no banco de dados
    def cadastro_autorizado(self):
        try:
            nome = self.input_nome.get()
            email = self.input_email.get()
            senha = self.input_senha.get()
            conect = psycopg2.connect(database = "sistema", host= "localhost", user = "postgres",password="5115",port="5432")
            sql_query = "INSERT INTO os_admin(nome,email,senha) VALUES( %s, %s, %s)"
            cursor = conect.cursor()
            cursor.execute(sql_query, (nome, email, senha))
            conect.commit()
            cursor.close()
            conect.close()
        except psycopg2.Error:
            self.aviso_erro_serve()
            
    #############################
    ##### função aviso email inválido
    def aviso_email_invalido(self):
        frame_email_invalido = customtkinter.CTkFrame(master=self.frame_dados_adm,width=400,height=120,fg_color='#0097b2',bg_color='transparent')
        frame_email_invalido.place(relx=0.1,rely=0.62)
        label_aviso_email_invalido = customtkinter.CTkLabel(master=frame_email_invalido,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Email invalido',text_color='black',font=('Arial bold',18))
        label_aviso_email_invalido.place(relx=0.13,rely=0.15)
        label_aviso_novamente = customtkinter.CTkLabel(master=frame_email_invalido,width=300,height=40,fg_color='transparent',bg_color='transparent',text='Insere um email válido',text_color='black',font=('Arial bold',17))
        label_aviso_novamente.place(relx=0.13,rely=0.5)
        sleep(5)
        self.limpar_inputs()
        frame_email_invalido.destroy()
    
    ############################
    ##### função de senha inválida
    def senha_invalida(self):
        frame_senha_invalido = customtkinter.CTkFrame(master=self.frame_dados_adm,width=400,height=120,fg_color='#0097b2',bg_color='transparent')
        frame_senha_invalido.place(relx=0.1,rely=0.62)
        label_aviso_senha_invalido = customtkinter.CTkLabel(master=frame_senha_invalido,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Senha invalida',text_color='black',font=('Arial bold',18))
        label_aviso_senha_invalido.place(relx=0.13,rely=0.15)
        label_aviso_novamente = customtkinter.CTkLabel(master=frame_senha_invalido,width=300,height=40,fg_color='transparent',bg_color='transparent',text='Crie uma senha válida',text_color='black',font=('Arial bold',17))
        label_aviso_novamente.place(relx=0.13,rely=0.5)
        sleep(5)
        self.limpar_inputs()
        frame_senha_invalido.destroy()
    
    ############################
    #### função de erro no servidor
    def aviso_erro_serve(self):
        frame_erro_serve = customtkinter.CTkFrame(master=self.frame_dados_adm,width=400,height=120,fg_color='#0097b2',bg_color='transparent')
        frame_erro_serve.place(relx=0.1,rely=0.62)
        label_aviso_erro_serve = customtkinter.CTkLabel(master=frame_erro_serve,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Erro no servidor',text_color='black',font=('Arial bold',18))
        label_aviso_erro_serve.place(relx=0.13,rely=0.15)
        label_aviso_novamente = customtkinter.CTkLabel(master=frame_erro_serve,width=300,height=40,fg_color='transparent',bg_color='transparent',text='Falha em conectar ao servidor',text_color='black',font=('Arial bold',17))
        label_aviso_novamente.place(relx=0.13,rely=0.5)
        sleep(5)
        self.limpar_inputs()
        frame_erro_serve.destroy()
    

    #######################
    #### função de limpar os inputs
    def limpar_inputs(self):
        self.input_email.delete(0,100)
        self.input_nome.delete(0,100)
        self.input_senha.delete(0,100)


def chamando_adicionar_adm():
    app = adicionar_adm()
    app.janela_add_adm.mainloop()