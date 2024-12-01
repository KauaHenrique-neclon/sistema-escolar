import tkinter
import customtkinter
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from menu_pincipal import menu_chamar
import psycopg2

class aplicativo():
    def __init__(self):
        self.janela_login = tkinter.Tk()
        #self.janela_login.attributes('-fullscreen', True) 
        self.janela_login.geometry('500x400')
        self.janela_login.title('Login')
        self.janela_login.resizable(width=False,height=False)
        #self.janela_login.iconbitmap("")
        self.janela_login.configure(background="white")
        label_titulo = customtkinter.CTkLabel(master=self.janela_login,width=500,height=60,text='S.E.C',bg_color='transparent',fg_color="#20b2aa")
        label_titulo.place(relx=0,rely=0)
        frame_tudo = customtkinter.CTkFrame(master=self.janela_login,width=400,height=340,bg_color="#0097b2",fg_color="#0097b2")
        frame_tudo.place(relx=0.1,rely=0.12)
        label_nome = customtkinter.CTkLabel(master=frame_tudo,width=200,height=30,bg_color='transparent',text="Email",text_color='#ffffff')
        label_nome.place(relx=0.24,rely=0.08)
        self.receber_usuario = customtkinter.CTkEntry(master=frame_tudo,width=200,height=30,fg_color="#ffffff",corner_radius=10,bg_color='transparent')
        self.receber_usuario.place(relx=0.24,rely=0.16)
        label_senha = customtkinter.CTkLabel(master=frame_tudo,width=200,height=30,bg_color='transparent',text="Sua Senha",text_color='#ffffff')
        label_senha.place(relx=0.24,rely=0.26)
        self.receber_senha = customtkinter.CTkEntry(master=frame_tudo,width=200,height=30,fg_color="#ffffff",corner_radius=10,bg_color='transparent',show="*")
        self.receber_senha.place(relx=0.24,rely=0.34)
        button_verificar = customtkinter.CTkButton(master=frame_tudo,width=150,height=30,hover_color="#00a8ff",fg_color="#20b2aa",text="Entrar",corner_radius=10,bg_color='transparent',command=self.verificar_senha)
        button_verificar.place(relx=0.3,rely=0.47)
        add_adm = customtkinter.CTkFrame(master=frame_tudo,width=320,height=80,bg_color="#20b2aa",fg_color="#20b2aa",corner_radius=20)
        add_adm.place(relx=0.1,rely=0.66)
        label_add_adm = customtkinter.CTkLabel(master=add_adm,width=50,height=20,bg_color='transparent',text='ADICIONAR ADMINISTRADOR',text_color='#ffffff',font=("Arial bold",17))
        label_add_adm.place(relx=0.15,rely=0.1)
        button_add_adm = customtkinter.CTkButton(master=add_adm,width=150,height=30,hover_color="#00a8ff",fg_color="#0097b2",text="Cadastrar",corner_radius=10,bg_color='transparent')
        button_add_adm.place(relx=0.27,rely=0.50)
        
    def verificar_senha(self):
        try:
            usuario = self.receber_usuario.get()
            senha = self.receber_senha.get()
            conexao = psycopg2.connect(database = "sistema", host= "localhost", user = "postgres",password="5115",port="5432")
            cursor = conexao.cursor()
            sql_consulta = 'SELECT email,senha FROM os_admin WHERE email = %s AND senha = %s'
            cursor.execute(sql_consulta, (usuario, senha))
            resultado = cursor.fetchone()
            if resultado:
                self.janela_login.destroy()
                cursor.close()
                conexao.close()
                menu_chamar()
            else:
                messagebox.showinfo('Acesso negado', 'Usuário ou senha incorretos')
                cursor.close()
                conexao.close()
        except:
            print('Erro ao tentar acessar')


def chamando():
    app = aplicativo()
    app.janela_login.mainloop()

chamando()