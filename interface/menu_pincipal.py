import tkinter
import customtkinter
from customtkinter import *
from tkinter import *
from tkinter import messagebox
import datetime
import psycopg2
from PIL import ImageTk,Image
from medias_alunos_menu import chamando_medias
from cadastrar import chamando_cadastramento
from delete_alunos import chamando_delete
from lancar_notas import chamando_notas
from add_adm import chamando_adicionar_adm
from financeiro import chamando_financeiro


class menu():
    def __init__(self):
        self.menu_janela = tkinter.Tk()
        self.menu_janela.title('Menu')
        self.menu_janela.configure(background='#d6dee2')
        self.menu_janela.attributes('-fullscreen', True)
         
        #############################
        ######## frame de menu de busca
        frame_de_busca = customtkinter.CTkFrame(master=self.menu_janela,fg_color='#c77dff',width=1100,height=50,bg_color='transparent')
        frame_de_busca.place(relx=0.088, rely=0.06)
        button_add_adm = customtkinter.CTkButton(master=frame_de_busca,width=100,height=30,fg_color='transparent',bg_color='transparent',text='add adm',text_color='white',hover_color='#6b3fa0',font=('Arial bold',17),command=self.adicionar_adm)
        button_add_adm.place(relx=0.5,rely=0.2)
        hora = datetime.datetime.now().strftime('%H:%M')
        hora_label = customtkinter.CTkLabel(master=frame_de_busca,width=100,height=30,fg_color='transparent',bg_color='transparent',text=f'{hora}',text_color='white',font=('Arial bold',17))
        hora_label.place(relx=0.9,rely=0.2)

        #################################
        #### frame de cadastro button
        frame_cadastro_aluno = customtkinter.CTkFrame(master=self.menu_janela,width=150,height=150,fg_color='white',bg_color='transparent')
        frame_cadastro_aluno.place(relx=0.3,rely=0.2)
        frame_icone_cadastro = customtkinter.CTkFrame(master=frame_cadastro_aluno,width=150,height=100,fg_color='white',bg_color='transparent')
        frame_icone_cadastro.place(relx=0,rely=0)
        imagem_cadastro = Image.open(r"C:/sistema_2/icones/menu_principal/cadastro_2.ico")
        convertendo_icon_cadastro = ImageTk.PhotoImage(imagem_cadastro)
        icone_cadastro = customtkinter.CTkButton(master=frame_icone_cadastro,image=convertendo_icon_cadastro,width=150,height=100,fg_color='transparent',bg_color='transparent',hover_color=None,hover=None,text=None)
        icone_cadastro.place(relx=0,rely=0)
        button_cadastro = customtkinter.CTkButton(master=frame_cadastro_aluno,width=120,height=30,fg_color='transparent',bg_color='transparent',text='Cadastrar aluno',text_color='black',hover_color='#6b3fa0',command=self.cadastrar_aluno)
        button_cadastro.place(relx=0.1,rely=0.7)

        #################################
        ####### frame de deletar aluno
        frame_deletar_aluno = customtkinter.CTkFrame(master=self.menu_janela,width=150,height=150,fg_color='white',bg_color='transparent')
        frame_deletar_aluno.place(relx=0.43,rely=0.2)
        frame_icone_delete = customtkinter.CTkFrame(master=frame_deletar_aluno,width=150,height=100,fg_color='white',bg_color='transparent')
        frame_icone_delete.place(relx=0,rely=0)
        imagem_delete = Image.open(r"C:/sistema_2/icones/menu_principal/delete_aluno_2.ico")
        convertendo_icon_delete = ImageTk.PhotoImage(imagem_delete)
        icone_delete = customtkinter.CTkButton(master=frame_icone_delete,image=convertendo_icon_delete,width=150,height=100,fg_color='transparent',bg_color='transparent',hover_color=None,hover=None,text=None)
        icone_delete.place(relx=0,rely=0)
        button_delete = customtkinter.CTkButton(master=frame_deletar_aluno,width=120,height=30,fg_color='transparent',bg_color='transparent',text='Deletar info',text_color='black',hover_color='#6b3fa0',command=self.deletar_alunos)
        button_delete.place(relx=0.1,rely=0.7)
        

        ############################
        ######## frame de cadastrar notas
        frame_notas = customtkinter.CTkFrame(master=self.menu_janela,width=150,height=150,fg_color='white',bg_color='transparent')
        frame_notas.place(relx=0.56,rely=0.2)
        frame_icone_notas = customtkinter.CTkFrame(master=frame_notas,width=150,height=100,fg_color='white',bg_color='transparent')
        frame_icone_notas.place(relx=0,rely=0)
        imagem_notas = Image.open(r"C:/sistema_2/icones/menu_principal/nota_2.ico")
        convertendo_icon_notas = ImageTk.PhotoImage(imagem_notas)
        icone_notas = customtkinter.CTkButton(master=frame_icone_notas,image=convertendo_icon_notas,width=150,height=100,fg_color='transparent',bg_color='transparent',hover_color=None,hover=None,text=None)
        icone_notas.place(relx=0,rely=0)
        button_notas = customtkinter.CTkButton(master=frame_notas,width=120,height=30,fg_color='transparent',bg_color='transparent',text='Lançar Notas',text_color='black',hover_color='#6b3fa0',command=self.lancar_notas)
        button_notas.place(relx=0.1,rely=0.7)


        ##################################
        ######### frame de ver media do aluno
        frame_media = customtkinter.CTkFrame(master=self.menu_janela,width=150,height=150,fg_color='white',bg_color='transparent')
        frame_media.place(relx=0.69,rely=0.2)
        frame_icone_media = customtkinter.CTkFrame(master=frame_media,width=150,height=100,fg_color='white',bg_color='transparent')
        frame_icone_media.place(relx=0,rely=0)
        imagem_media = Image.open(r"C:/sistema_2/icones/menu_principal/media_escolar.ico")
        convertendo_icon_media = ImageTk.PhotoImage(imagem_media)
        icone_media = customtkinter.CTkButton(master=frame_icone_media,image=convertendo_icon_media,width=150,height=100,fg_color='transparent',bg_color='transparent',hover_color=None,hover=None,text=None)
        icone_media.place(relx=0,rely=0)
        button_media = customtkinter.CTkButton(master=frame_media,width=120,height=30,fg_color='transparent',bg_color='transparent',text='Ver Media',text_color='black',hover_color='#6b3fa0',command=self.ver_medias)
        button_media.place(relx=0.1,rely=0.7)

        ###################################
        ######## frame financeiro 
        frame_financeiro = customtkinter.CTkFrame(master=self.menu_janela,width=150,height=150,fg_color='white',bg_color='transparent')
        frame_financeiro.place(relx=0.56,rely=0.45)
        frame_icone_financeiro = customtkinter.CTkFrame(master=frame_financeiro,width=150,height=100,fg_color='white',bg_color='transparent')
        frame_icone_financeiro.place(relx=0,rely=0)
        imagem_financeiro= Image.open(r"C:/sistema_2/icones/menu_principal/financeiro.ico")
        convertendo_icon_financeiro = ImageTk.PhotoImage(imagem_financeiro)
        icone_financeiro = customtkinter.CTkButton(master=frame_icone_financeiro,image=convertendo_icon_financeiro,width=150,height=100,fg_color='transparent',bg_color='transparent',hover_color=None,hover=None,text=None)
        icone_financeiro.place(relx=0,rely=0)
        button_financeiro = customtkinter.CTkButton(master=frame_financeiro,width=120,height=30,fg_color='transparent',bg_color='transparent',text='Financeiro',text_color='black',hover_color='#6b3fa0',command=self.financeiro)
        button_financeiro.place(relx=0.1,rely=0.7)

    

    def ver_medias(self):
        self.menu_janela.destroy()
        chamando_medias()
    
    def cadastrar_aluno(self):
        self.menu_janela.destroy()
        chamando_cadastramento()
    
    def deletar_alunos(self):
        self.menu_janela.destroy()
        chamando_delete()
    
    def lancar_notas(self):
        self.menu_janela.destroy()
        chamando_notas()

    def adicionar_adm(self):
        self.menu_janela.destroy()
        chamando_adicionar_adm()
    
    def financeiro(self):
        self.menu_janela.destroy()
        chamando_financeiro()


def menu_chamar():
    menu_app = menu()
    menu_app.menu_janela.mainloop()