import tkinter
import customtkinter
import psycopg2
from time import sleep

class cadastrar_aluno():
    def __init__(self):
        self.janela_cadastrar = tkinter.Tk()
        self.janela_cadastrar.title('Cadastrar Aluno')
        self.janela_cadastrar.configure(background='white')
        self.janela_cadastrar.attributes('-fullscreen', True)

        ########
        ###frame de cadastrar o aluno
        label_cadastrar = customtkinter.CTkLabel(master=self.janela_cadastrar,width=400,height=30,fg_color='transparent',bg_color='transparent',text='Cadastrar aluno',text_color='black')
        label_cadastrar.place(relx=0.08,rely=0.05)
        label_name = customtkinter.CTkLabel(master=self.janela_cadastrar,width=200,height=40,fg_color='transparent',bg_color='transparent',text_color='black',text='Nome:')
        label_name.place(relx=0.08,rely=0.15)
        self.input_name = customtkinter.CTkEntry(master=self.janela_cadastrar,width=200,height=40,fg_color='#d6dee2',bg_color='transparent')
        self.input_name.place(relx=0.18,rely=0.15)
        label_sobrenome = customtkinter.CTkLabel(master=self.janela_cadastrar,width=200,height=40,fg_color='transparent',bg_color='transparent',text='Sobrenome:',text_color='black')
        label_sobrenome.place(relx=0.068,rely=0.23)
        self.input_sobrenome = customtkinter.CTkEntry(master=self.janela_cadastrar,width=200,height=40,fg_color='#d6dee2',bg_color='transparent')
        self.input_sobrenome.place(relx=0.18,rely=0.23)
        label_sexo = customtkinter.CTkLabel(master=self.janela_cadastrar,width=200,height=40,fg_color='transparent',bg_color='transparent',text='Sexo:',text_color='black')
        label_sexo.place(relx=0.08,rely=0.31)
        self.input_sexo = customtkinter.CTkEntry(master=self.janela_cadastrar,width=200,height=40,bg_color='transparent',fg_color='#d6dee2')
        self.input_sexo.place(relx=0.18,rely=0.31)
        label_cpf = customtkinter.CTkLabel(master=self.janela_cadastrar,width=200,height=40,fg_color='transparent',bg_color='transparent',text='CPF:',text_color='black')
        label_cpf.place(relx=0.08,rely=0.39)
        self.input_cpf = customtkinter.CTkEntry(master=self.janela_cadastrar,width=200,height=40,bg_color='transparent',fg_color='#d6dee2')
        self.input_cpf.place(relx=0.18,rely=0.39)
        label_idade = customtkinter.CTkLabel(master=self.janela_cadastrar,width=200,height=40,fg_color='transparent',bg_color='transparent',text='Nascimento:',text_color='black')
        label_idade.place(relx=0.066,rely=0.47)
        self.input_idade = customtkinter.CTkEntry(master=self.janela_cadastrar,width=200,height=40,bg_color='transparent',fg_color='#d6dee2')
        self.input_idade.place(relx=0.18,rely=0.47)
        self.button_submit_cadastro_aluno = customtkinter.CTkButton(master=self.janela_cadastrar,width=200,height=40,bg_color='transparent',fg_color='#054f77',text='Cadastrar',text_color='black',command=self.validar_entrada_cpf)
        self.button_submit_cadastro_aluno.place(relx=0.18,rely=0.55)

    ##### Valida se tem 11 numeros do CPF
    ##### função do cadastrar aluno
    def validar_entrada_cpf(self):
        cpf = self.input_cpf.get()
        if len(cpf) == 11 and cpf.isdigit():
            self.validar_entrada_idade()
        else:
            self.insira_11_numeros()
    
    def validar_entrada_idade(self):
        cpf = self.input_idade.get()
        if len(cpf) == 4 and cpf.isdigit():
            self.verificar_cpf_usado()
        else:
            self.insira_4_numeros()

    ###### função paara validar o cpf do aluno
    ######## função do cadastrar aluno
    def verificar_cpf_usado(self):
            try:
                cpf_aluno = self.input_cpf.get()
                self.conexao_banco_1()
                sql_query = "SELECT cpf FROM aluno_info WHERE cpf = %s"
                cursor = self.conexao_1.cursor()
                cursor.execute(sql_query, (str(cpf_aluno),))
                self.resultado_consulta = cursor.fetchone()
                if self.resultado_consulta is None:
                    self.salvar_dados_do_cadastro()
                    cursor.close()
                    self.conexao_1.close()
                else:
                    self.mostar_cpf_usado()
                    cursor.close()
                    self.conexao_1.close()
            except psycopg2.Error:
                self.retorna_erro_frame()

    ############
    #### conectar o banco de dados
    def conexao_banco_1(self):
            self.conexao_1 = psycopg2.connect(database = "sistema", host= "localhost", user = "postgres",password="5115",port="5432")
    

    ###### função que retorna um frame de erro no cpf 
    ###### pertence a função cadastro aluno
    def mostar_cpf_usado(self):
        frame_cpf_usado = customtkinter.CTkFrame(master=self.janela_cadastrar,width=400,height=100,fg_color='#d3d3d3',bg_color='transparent')
        frame_cpf_usado.place(relx=0.08,rely=0.65)
        label_cpf_usado = customtkinter.CTkLabel(master=frame_cpf_usado,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Cpf sendo usado',text_color='Black',font=("Arial bold",18))
        label_cpf_usado.place(relx=0.1,rely=0.2)
        label_cpf_usado_novamente = customtkinter.CTkLabel(master=frame_cpf_usado,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Insira um diferente',text_color='Black',font=("Arial bold",15))
        label_cpf_usado_novamente.place(relx=0.1, rely=0.6)
        sleep(5)
        self.limpar_inputs()
        frame_cpf_usado.destroy()
    

    ###### função que salva os dados do cadastro do aluno
    ###### pertence a função cadastro aluno
    def salvar_dados_do_cadastro(self):
        nome = self.input_name.get()
        sobrenome = self.input_sobrenome.get()
        cpf = self.input_cpf.get()
        sexo = self.input_sexo.get() 
        idade = self.input_idade.get()
        sql_query = "INSERT INTO aluno_info(nome,sobrenome,cpf,sexo,idade) VALUES( %s, %s, %s, %s, %s)"
        if self.resultado_consulta is None:
            self.conexao_banco_1()
            cursor_1 = self.conexao_1.cursor()
            cursor_1.execute(sql_query,(nome,sobrenome,cpf,sexo,idade))
            self.conexao_1.commit()
            self.conexao_1.close()
            self.limpar_inputs()
            self.dados_salvo_aviso()
        else:
            self.limpar_inputs()
            self.retorna_erro_frame()
    

    ###### frame que retorna o aviso de dados salvos
    ###### pertence a função cadastro aluno
    def dados_salvo_aviso(self):
        frame_aviso = customtkinter.CTkFrame(master=self.janela_cadastrar,width=400,height=100,fg_color='#d3d3d3',bg_color='transparent')
        frame_aviso.place(relx=0.08,rely=0.65)
        label_aviso_salvo = customtkinter.CTkLabel(master=frame_aviso,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Os dados foram salvos',text_color='Black',font=("Arial bold",18))
        label_aviso_salvo.place(relx=0.1,rely=0.2)
        label_aviso_novamente = customtkinter.CTkLabel(master=frame_aviso,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Dados salvo',text_color='Black',font=("Arial bold",15))
        label_aviso_novamente.place(relx=0.1, rely=0.6)
        sleep(5)
        self.limpar_inputs()
        frame_aviso.destroy()
    

    ###### frame que retorna o aviso de inserir 11 numeros do cpf
    ###### pertence a função cadastro aluno
    def insira_11_numeros(self):
        frame_aviso_falta = customtkinter.CTkFrame(master=self.janela_cadastrar,width=400,height=100,fg_color='#d3d3d3',bg_color='transparent')
        frame_aviso_falta.place(relx=0.08,rely=0.65)
        label_aviso_falta = customtkinter.CTkLabel(master=frame_aviso_falta,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Insira os 11 numeros',text_color='Black',font=("Arial bold",18))
        label_aviso_falta.place(relx=0.1,rely=0.2)
        label_aviso_falta_novamente = customtkinter.CTkLabel(master=frame_aviso_falta,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Falta numeros no CPF',text_color='Black',font=("Arial bold",15))
        label_aviso_falta_novamente.place(relx=0.1, rely=0.6)
        sleep(5)
        self.limpar_inputs()
        frame_aviso_falta.destroy()

    ###### frame que retorna o aviso de inserir 4 numeros da idade
    ###### pertence a função cadastro aluno
    def insira_4_numeros(self):
        frame_aviso_falta_idade = customtkinter.CTkFrame(master=self.janela_cadastrar,width=400,height=100,fg_color='#d3d3d3',bg_color='transparent')
        frame_aviso_falta_idade.place(relx=0.08,rely=0.65)
        label_aviso_falta_idade = customtkinter.CTkLabel(master=frame_aviso_falta_idade,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Insira os 4 numeros',text_color='Black',font=("Arial bold",18))
        label_aviso_falta_idade.place(relx=0.1,rely=0.2)
        label_aviso_falta_novamente_idade = customtkinter.CTkLabel(master=frame_aviso_falta_idade,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Falta numeros na idade',text_color='Black',font=("Arial bold",15))
        label_aviso_falta_novamente_idade.place(relx=0.1, rely=0.6)
        sleep(5)
        self.limpar_inputs()
        frame_aviso_falta_idade.destroy()
        
    
    ###### frame que retorna o aviso de erro na conexão no banco
    ###### pertence a função cadastro aluno
    def retorna_erro_frame(self):
        frame_aviso_erro = customtkinter.CTkFrame(master=self.janela_cadastrar,width=400,height=100,fg_color='#d3d3d3',bg_color='transparent')
        frame_aviso_erro.place(relx=0.08,rely=0.65)
        label_aviso_erro = customtkinter.CTkLabel(master=frame_aviso_erro,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Erro no banco de dados',text_color='Black',font=("Arial bold",18))
        label_aviso_erro.place(relx=0.1,rely=0.2)
        label_aviso_novamente_erro = customtkinter.CTkLabel(master=frame_aviso_erro,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Dados não salvo',text_color='Black',font=("Arial bold",15))
        label_aviso_novamente_erro.place(relx=0.1, rely=0.6)
        sleep(5)
        self.limpar_inputs()
        frame_aviso_erro.destroy()
    

    ###### função que limpa todos os inputs do cadastro aluno
    ###### pertence a função cadastro aluno
    def limpar_inputs(self):
        self.input_cpf.delete(0, 50)
        self.input_idade.delete(0, 50)
        self.input_name.delete(0, 50)
        self.input_sexo.delete(0, 50)
        self.input_sobrenome.delete(0, 50)
    
    ##############################################################
    ############### começa o beckend da nota  ####################
    ##############################################################
    
       


###### chamando a class
def chamando_cadastramento():
    app = cadastrar_aluno()
    app.janela_cadastrar.mainloop()