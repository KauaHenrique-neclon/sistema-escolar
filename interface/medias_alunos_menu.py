import tkinter
import customtkinter
from customtkinter import *
from tkinter import *
import psycopg2
from PIL import ImageTk,Image

class medias_aluno():
    def __init__(self):
        self.media_janela = tkinter.Tk()
        self.media_janela.title('Medias')
        self.media_janela.configure(background='#29849f')
        self.media_janela.attributes('-fullscreen', True)
        label_nome = customtkinter.CTkLabel(master=self.media_janela,width=900,height=60,fg_color='white',bg_color='transparent' ,text='Menu para ver notas', text_color='black',font=("Arial bold",17))
        label_nome.place(relx=0.2,rely=0.08)

        #criando a estrutura do button
        #frame do botão de consultar com CPF
        frame_consultar_cpf = customtkinter.CTkFrame(master=self.media_janela,width=300,height=100,fg_color='white',bg_color='transparent')
        frame_consultar_cpf.place(relx=0.05,rely=0.2)
        imagem_cpf = Image.open(r"C:/sistema_2/icones/cpf_icon_3.ico")
        covertendo_icone_cpf = ImageTk.PhotoImage(imagem_cpf)
        cpf_icone = customtkinter.CTkButton(master=frame_consultar_cpf,image=covertendo_icone_cpf,width=20,height=60,hover_color=None,hover=None,bg_color='transparent',fg_color='transparent',text=None)
        cpf_icone.place(relx=0.07,rely=0.01)
        button_notas_cpf = customtkinter.CTkButton(master=frame_consultar_cpf,width=150,height=40,fg_color='#054f77',bg_color='transparent',text='Ver com CPF',text_color='white',command=self.verificar_cpf_apareceu)
        button_notas_cpf.place(relx=0.45,rely=0.27)
        
        ###frame de consultar com ID do aluno
        #####button para ativar frame
        frame_consultar_id = customtkinter.CTkFrame(master=self.media_janela,width=300,height=100,fg_color='white',bg_color='transparent')
        frame_consultar_id.place(relx=0.05,rely=0.37)
        imagem_id = Image.open(r"C:/sistema_2/icones/icone_id.ico")
        covertendo_icone_id = ImageTk.PhotoImage(imagem_id)
        icone_id = customtkinter.CTkButton(master=frame_consultar_id,image=covertendo_icone_id,width=20,height=60,hover_color=None,hover=None,bg_color='transparent',fg_color='transparent',text=None)
        icone_id.place(relx=0.1,rely=0.01)
        button_notas_id = customtkinter.CTkButton(master=frame_consultar_id,width=150,height=40,fg_color='#054f77',bg_color='transparent',text='Ver com ID',text_color='white',command=self.verificar_id_apareceu)
        button_notas_id.place(relx=0.45,rely=0.27)

        self.frame_do_id = None
        self.frame_do_cpf = None
    
    #primeiro frame
    ##### pertende ao frame cpf
    def verificar_cpf_apareceu(self):
        if self.frame_do_cpf is None:
            self.aluno_id = None
            self.apareceu_frame_cpf()
        else:
            self.ocultar_frame_cpf()
    
    #######
    #### função para o frame aparecer
    ##### pertende ao frame cpf
    def apareceu_frame_cpf(self):
        self.frame_do_cpf = customtkinter.CTkFrame(master=self.media_janela,width=900,height=400,fg_color='white',bg_color='transparent')
        self.frame_do_cpf.place(relx=0.3,rely=0.2)
        label_cpf = customtkinter.CTkLabel(master=self.frame_do_cpf,width=300,height=50,fg_color='transparent',bg_color='transparent',text='Pelo CPF do aluno',text_color='black',font=("Arial bold",15))
        label_cpf.place(relx=0.3,rely=0.05)
        label_coloc_cpf = customtkinter.CTkLabel(master=self.frame_do_cpf,width=250,height=40,fg_color='transparent',bg_color='transparent',text='Entra com CPF do Aluno',text_color='black',font=("Arial bold",15))
        label_coloc_cpf.place(relx=0.1,rely=0.2)
        self.input_cpf = customtkinter.CTkEntry(master=self.frame_do_cpf,width=250,height=40,fg_color='#d3d3d3',bg_color='transparent')
        self.input_cpf.place(relx=0.1,rely=0.4)
        self.ButtonSubmitPesquisaCpf = customtkinter.CTkButton(master=self.frame_do_cpf,width=250, height=35,bg_color='transparent',fg_color='#054f77',text='Consultar',text_color='white',command=self.consulta_media_cpf)
        self.ButtonSubmitPesquisaCpf.place(relx=0.1,rely=0.7) 
    
    ########
    ### função para o frame ser ocultado
    ##### pertende ao frame cpf
    def ocultar_frame_cpf(self):
        if self.frame_do_cpf is not None:
            self.frame_do_cpf.place_forget()
            self.frame_do_cpf = None

    ##################
    ##conexão ao banco, 1 conexão
    def conectar_banco_sistema(self):
        self.conexao_sistema = psycopg2.connect(database = "sistema", host= "localhost", user = "postgres",password="5115",port="5432")

    #consultar media pelo cpf do aluno
    ##### pertende ao frame cpf
    def consulta_media_cpf(self):
            try:
                self.cpf_aluno = self.input_cpf.get()
                self.conectar_banco_sistema()
                sql_query = "SELECT (nota_1 + nota_2 + nota_3) /3 FROM notas WHERE cpf = %s"
                cursor = self.conexao_sistema.cursor()
                cursor.execute(sql_query,(str(self.cpf_aluno),))
                self.soma_nota = cursor.fetchone()
                print(self.soma_nota)
                if self.soma_nota is not None:
                    self.consultar_nome_pelo_cpf()
                    self.resultado_cpf_media_notas()
                    cursor.close()
                    self.conexao_sistema.close()
                else:
                    self.cpf_invalido()
            except ConnectionError:
                self.server_caiu_cpf()

    ##### 2 consulta porque não dar pra fazer essa poha em uma só
    ##### vai se fuder python crlh
    ##### pertende ao frame cpf
    def consultar_nome_pelo_cpf(self):
        try:
            self.conectar_banco_sistema()
            sql_query = "SELECT nome FROM aluno_info WHERE cpf = %s"
            cursor_1 = self.conexao_sistema.cursor()
            cursor_1.execute(sql_query, (str(self.cpf_aluno),))
            self.nome_soma = cursor_1.fetchone()
        except:
            self.nome_soma = 'erro'
    
    
    ###  uma função para mostrar o resultado no app da media de nota
    ##### pertende ao frame cpf
    def resultado_cpf_media_notas(self):
        self.FrameResultadoConsultaCpf = customtkinter.CTkFrame(master=self.frame_do_cpf,width=450,height=250,fg_color='#d3d3d3',bg_color='transparent')
        self.FrameResultadoConsultaCpf.place(relx=0.43,rely=0.2)
        label_media_aluno = customtkinter.CTkLabel(master=self.FrameResultadoConsultaCpf,width=400,height=40,fg_color='transparent',bg_color='transparent',text='Resultado da consulta pelo CPF',text_color='black',font=("Arial bold",15))
        label_media_aluno.place(relx=0.1,rely=0.1)
        label_mostrando_nota = customtkinter.CTkLabel(master=self.FrameResultadoConsultaCpf,width=100,height=40,fg_color='transparent',bg_color='transparent',text=f'A media foi {str(round(self.soma_nota[0]))}' ,text_color='black',font=("Arial bold",17))
        label_mostrando_nota.place(relx=0.4,rely=0.4)
        label_mostrando_nome = customtkinter.CTkLabel(master=self.FrameResultadoConsultaCpf,width=100,height=40,fg_color='transparent',bg_color='transparent',text=f'Media do aluno {str(self.nome_soma[0])}',text_color='black',font=("Arial bold",17))
        label_mostrando_nome.place(relx=0.34,rely=0.6)
        Button_pesquisar_novamente = customtkinter.CTkButton(master=self.FrameResultadoConsultaCpf,width=200,height=30,fg_color='#054f77',bg_color='transparent',text='Consultar novamente',text_color='white',font=("Arial bold",16),command=self.consultar_novamente_pelo_cpf)
        Button_pesquisar_novamente.place(relx=0.3,rely=0.8)
    
    ##### função para consultar novamente pelo cpf
    ##### pertende ao frame cpf
    def consultar_novamente_pelo_cpf(self):
        self.input_cpf.delete()
        self.FrameResultadoConsultaCpf.destroy()
        self.apareceu_frame_cpf

    ####função que retorna cpf invalido
    ##### pertende ao frame cpf
    def cpf_invalido(self):
        self.frame_errado_cpf = customtkinter.CTkFrame(master=self.frame_do_cpf,width=450,height=250,fg_color='white',bg_color='transparent')
        self.frame_errado_cpf.place(relx=0.43,rely=0.2)
        label_errado_cpf = customtkinter.CTkLabel(master=self.frame_errado_cpf,width=400,height=40,fg_color='transparent',bg_color='transparent',text='O CPF não foi encontrado',text_color='black',font=("Arial bold",15))
        label_errado_cpf.place(relx=0.1,rely=0.1)
        label_n_existe_cpf = customtkinter.CTkLabel(master=self.frame_errado_cpf,width=100,height=40,fg_color='transparent',bg_color='transparent',text=f'CPF inválido, tente novamente',text_color='black',font=("Arial bold",17))
        label_n_existe_cpf.place(relx=0.34,rely=0.6)
        consultar_novamente = customtkinter.CTkButton(master=self.frame_errado_cpf,width=200,height=30,fg_color='#054f77',bg_color='transparent',text='Consultar novamente',text_color='white',font=("Arial bold",16),command=self.consultar_novamente_pelo_cpf)
        consultar_novamente.place(relx=0.3,rely=0.8)
 
    #####função que mostra um frame do servidor caiu
    ##### pertende ao frame cpf
    def server_caiu_cpf(self):
        self.frame_server_c = customtkinter.CTkFrame(master=self.frame_do_cpf,width=450,height=250,fg_color='white',bg_color='transparent')
        self.frame_server.place(relx=0.43,rely=0.2)
        label_server_caiu = customtkinter.CTkLabel(master=self.frame_server_c,width=400,height=40,fg_color='transparent',bg_color='transparent',text='Sem acesso ao servidor',text_color='black',font=("Arial bold",15))
        label_server_caiu.place(relx=0.1,rely=0.1)
        label_sem_server = customtkinter.CTkLabel(master=self.frame_server_c,width=100,height=40,fg_color='transparent',bg_color='transparent',text=f'Acesso perdido, tente novamente',text_color='black',font=("Arial bold",17))
        label_sem_server.place(relx=0.34,rely=0.6)
        tentar_novamente = customtkinter.CTkButton(master=self.frame_server_c,width=200,height=30,fg_color='#054f77',bg_color='transparent',text='Tentar Novamente',text_color='white',font=("Arial bold",16),command=self.consultar_novamente_id)
        tentar_novamente.place(relx=0.3,rely=0.8)

    ##### segundo frame
    ##### pertende ao frame ID
    def verificar_id_apareceu(self):
        if self.frame_do_id is None:
            self.frame_do_cpf = None
            self.apareceu_frame_id()
        else:
            self.ocultar_frame_id()
    

    ### frame de consultar com ID
    ##### pertende ao frame ID
    def apareceu_frame_id(self):
        self.frame_do_id = customtkinter.CTkFrame(master=self.media_janela,width=900,height=400,fg_color='white',bg_color='transparent')
        self.frame_do_id.place(relx=0.3,rely=0.2)
        label_id = customtkinter.CTkLabel(master=self.frame_do_id,width=300,height=50,fg_color='transparent',bg_color='transparent',text='Pelo ID do aluno',text_color='black',font=("Arial bold",17))
        label_id.place(relx=0.3,rely=0.05)
        label_coloca_id = customtkinter.CTkLabel(master=self.frame_do_id,width=250,height=40,fg_color='transparent',bg_color='transparent',text='Entra com ID do Aluno',text_color='black',font=("Arial bold",15))
        label_coloca_id.place(relx=0.1,rely=0.2)
        self.input_id = customtkinter.CTkEntry(master=self.frame_do_id,width=250,height=40,fg_color='#d3d3d3',bg_color='transparent')
        self.input_id.place(relx=0.1,rely=0.4)
        self.ButtonSubmit_Id = customtkinter.CTkButton(master=self.frame_do_id,width=250, height=35,bg_color='transparent',fg_color='#054f77',text='Consultar',text_color='white',command=self.consulta_media_id)
        self.ButtonSubmit_Id.place(relx=0.1,rely=0.7) 
    
    ## ocultar frame do ID
    ##### pertende ao frame ID
    def ocultar_frame_id(self):
        if self.frame_do_id is not None:
            self.frame_do_id.place_forget()
            self.frame_do_id = None
    
    #função de consulta com ID
    ##### pertende ao frame ID
    def consulta_media_id(self):
        if self.ButtonSubmit_Id:
            try:
                self.aluno_id = self.input_id.get()
                self.conectar_banco_sistema()
                sql_query = "SELECT (nota_1 + nota_2 + nota_3) /3 FROM notas WHERE id = %s"
                cursor = self.conexao_sistema.cursor()
                cursor.execute(sql_query,(str(self.aluno_id),))
                self.somar_nota_id = cursor.fetchone()
                if self.somar_nota_id is not None:
                    self.pegar_nome_pelo_id()
                    self.resultado_nota_pelo_id()
                    cursor.close()
                    self.conexao_sistema.close()
                else:
                    self.id_passou_errado()
            except ConnectionError:
                self.server_caiu_id()
    
    ##função para pegar o nome pelo ID
    ##### pertende ao frame ID
    def pegar_nome_pelo_id(self):
        try:
            self.conectar_banco_sistema()
            sql_query = "SELECT nome FROM aluno_info INNER JOIN notas ON aluno_info.cpf = notas.cpf WHERE notas.id = %s"
            cursor = self.conexao_sistema.cursor()
            cursor.execute(sql_query,(str(self.aluno_id),))
            self.nome_aluno = cursor.fetchone()
        except:
            self.nome_aluno = 'erro'

    ####função para mostrar o resultado da consultas
    ##### pertende ao frame ID
    def resultado_nota_pelo_id(self):
        self.frame_resultado_consulta_id = customtkinter.CTkFrame(master=self.frame_do_id,width=450,height=250,fg_color='white',bg_color='transparent')
        self.frame_resultado_consulta_id.place(relx=0.43,rely=0.2)
        label_media_Id = customtkinter.CTkLabel(master=self.frame_resultado_consulta_id,width=400,height=40,fg_color='transparent',bg_color='transparent',text='Resultado da consulta pelo ID',text_color='black',font=("Arial bold",15))
        label_media_Id.place(relx=0.1,rely=0.1)
        label_nota_id = customtkinter.CTkLabel(master=self.frame_resultado_consulta_id,width=100,height=40,fg_color='transparent',bg_color='transparent',text=f'A media foi {str(round(self.somar_nota_id[0]))}' ,text_color='black',font=("Arial bold",17))
        label_nota_id.place(relx=0.4,rely=0.4)
        label_mostrando_nome_id = customtkinter.CTkLabel(master=self.frame_resultado_consulta_id,width=100,height=40,fg_color='transparent',bg_color='transparent',text=f'Media do aluno {str(self.nome_aluno[0])}',text_color='black',font=("Arial bold",17))
        label_mostrando_nome_id.place(relx=0.34,rely=0.6)
        pesquisar_novamente_id = customtkinter.CTkButton(master=self.frame_resultado_consulta_id,width=200,height=30,fg_color='#054f77',bg_color='transparent',text='Consultar novamente',text_color='white',font=("Arial bold",16),command=self.consultar_novamente_id)
        pesquisar_novamente_id.place(relx=0.3,rely=0.8)

    ##### função para fazer outra consulta
    ##### pertende ao frame ID
    def consultar_novamente_id(self):
        self.input_cpf.delete(0,50)
        self.frame_resultado_consulta_id.destroy()
        self.apareceu_frame_id()
    
    #### função que mostra um frame do id errado
    ##### pertende ao frame ID
    def id_passou_errado(self):
        self.frame_errado_id = customtkinter.CTkFrame(master=self.frame_do_id,width=450,height=250,fg_color='white',bg_color='transparent')
        self.frame_errado_id.place(relx=0.43,rely=0.2)
        label_errado_id = customtkinter.CTkLabel(master=self.frame_errado_id,width=400,height=40,fg_color='transparent',bg_color='transparent',text='O ID não foi encontrado',text_color='black',font=("Arial bold",15))
        label_errado_id.place(relx=0.1,rely=0.1)
        label_n_existe_id = customtkinter.CTkLabel(master=self.frame_errado_id,width=100,height=40,fg_color='transparent',bg_color='transparent',text=f'Id não foi existe, tente novamente',text_color='black',font=("Arial bold",17))
        label_n_existe_id.place(relx=0.34,rely=0.6)
        consultar_novamente = customtkinter.CTkButton(master=self.frame_errado_id,width=200,height=30,fg_color='#054f77',bg_color='transparent',text='Consultar novamente',text_color='white',font=("Arial bold",16),command=self.consultar_novamente_id)
        consultar_novamente.place(relx=0.3,rely=0.8)
    
    #### função falando que o servidor caiu
    ##### pertende ao frame ID
    def server_caiu_id(self):
        self.frame_server = customtkinter.CTkFrame(master=self.frame_do_id,width=450,height=250,fg_color='white',bg_color='transparent')
        self.frame_server.place(relx=0.43,rely=0.2)
        label_server_caiu = customtkinter.CTkLabel(master=self.frame_server,width=400,height=40,fg_color='transparent',bg_color='transparent',text='Sem acesso ao servidor',text_color='black',font=("Arial bold",15))
        label_server_caiu.place(relx=0.1,rely=0.1)
        label_sem_server = customtkinter.CTkLabel(master=self.frame_server,width=100,height=40,fg_color='transparent',bg_color='transparent',text=f'Acesso perdido, tente novamente',text_color='black',font=("Arial bold",17))
        label_sem_server.place(relx=0.34,rely=0.6)
        tentar_novamente = customtkinter.CTkButton(master=self.frame_server,width=200,height=30,fg_color='#054f77',bg_color='transparent',text='Tentar Novamente',text_color='white',font=("Arial bold",16),command=self.consultar_novamente_id)
        tentar_novamente.place(relx=0.3,rely=0.8)

    
def chamando_medias():
    app = medias_aluno()
    app.media_janela.mainloop()