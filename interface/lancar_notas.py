import tkinter
import customtkinter
import psycopg2
from time import sleep

class adicionar_notas():
    def __init__(self):
        self.janela_notas = tkinter.Tk()
        self.janela_notas.title('Lançar Notas')
        self.janela_notas.configure(background='white')
        self.janela_notas.attributes('-fullscreen', True)

        ############frame de cadastrar notas
        ##########frame de cadatrar notas
        frame_lancar_notas = customtkinter.CTkFrame(master=self.janela_notas,width=400,height=500,fg_color='transparent',bg_color='transparent')
        frame_lancar_notas.place(relx=0.1,rely=0.1)
        label_inicial = customtkinter.CTkLabel(master=frame_lancar_notas,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Deseja lançar notas dos alunos?',text_color='black',font=('Arial bold',17))
        label_inicial.place(relx=0.1,rely=0.1)
        button_nota_1 = customtkinter.CTkButton(master=frame_lancar_notas,width=200,height=40,fg_color="#0097b2",bg_color='transparent',text='Adicionar Nota 1',text_color='black',command=self.adicionar_nota_1)
        button_nota_1.place(relx=0.2,rely=0.3)
        button_nota_2 = customtkinter.CTkButton(master=frame_lancar_notas,width=200,height=40,fg_color="#0097b2",bg_color='transparent',text='Adicionar Nota 2',text_color='black',command=self.adicionar_nota_2)
        button_nota_2.place(relx=0.2,rely=0.5)
        button_nota_3 = customtkinter.CTkButton(master=frame_lancar_notas,width=200,height=40,fg_color="#0097b2",bg_color='transparent',text='Adicionar Nota 3',text_color='black',command=self.adicionar_nota_3)
        button_nota_3.place(relx=0.2, rely=0.7)

    ################
    ###### função da primeiro frame da nota 1
    ###################
    def adicionar_nota_1(self):
        self.frame_nota_1 = customtkinter.CTkFrame(master=self.janela_notas,width=500,height=400,fg_color='#d3d3d3',bg_color='transparent')
        self.frame_nota_1.place(relx=0.5,rely=0.2)
        label_sobre = customtkinter.CTkLabel(master=self.frame_nota_1,width=300,height=40,fg_color='transparent',bg_color='transparent',text='Deseja adicionar a primeira nota?',text_color='black')
        label_sobre.place(relx=0.2,rely=0.1)
        label_entrar = customtkinter.CTkLabel(master=self.frame_nota_1,width=300,height=30,fg_color='transparent',bg_color='transparent',text='CPF do Aluno',text_color='black')
        label_entrar.place(relx=0.2,rely=0.2)
        self.input_cpf = customtkinter.CTkEntry(master=self.frame_nota_1,width=300,height=30,bg_color='transparent',fg_color='white')
        self.input_cpf.place(relx=0.2,rely=0.3)
        label_entrar_nota = customtkinter.CTkLabel(master=self.frame_nota_1,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Nota do Aluno',text_color='black')
        label_entrar_nota.place(relx=0.2,rely=0.4)
        self.input_nota = customtkinter.CTkEntry(master=self.frame_nota_1,width=300,height=30,bg_color='transparent',fg_color='white')
        self.input_nota.place(relx=0.2,rely=0.5)
        self.button_salvar_nota_1 = customtkinter.CTkButton(master=self.frame_nota_1,width=200,height=40,fg_color="#0097b2",bg_color='transparent',text='lançar',text_color='black',command=self.verificar_nota_1)
        self.button_salvar_nota_1.place(relx=0.3,rely=0.65)
        
    ################
    ###### função da primeiro frame da nota 2
    ###################
    def adicionar_nota_2(self):
        self.frame_nota_2 = customtkinter.CTkFrame(master=self.janela_notas,width=500,height=400,fg_color='#d3d3d3',bg_color='transparent')
        self.frame_nota_2.place(relx=0.5,rely=0.2)
        label_sobre = customtkinter.CTkLabel(master=self.frame_nota_2,width=300,height=40,fg_color='transparent',bg_color='transparent',text='Deseja adicionar a primeira nota?',text_color='black')
        label_sobre.place(relx=0.2,rely=0.1)
        label_entrar = customtkinter.CTkLabel(master=self.frame_nota_2,width=300,height=30,fg_color='transparent',bg_color='transparent',text='CPF do Aluno',text_color='black')
        label_entrar.place(relx=0.2,rely=0.2)
        self.input_cpf = customtkinter.CTkEntry(master=self.frame_nota_2,width=300,height=30,bg_color='transparent',fg_color='white')
        self.input_cpf.place(relx=0.2,rely=0.3)
        label_entrar_nota = customtkinter.CTkLabel(master=self.frame_nota_2,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Nota do Aluno',text_color='black')
        label_entrar_nota.place(relx=0.2,rely=0.4)
        self.input_nota = customtkinter.CTkEntry(master=self.frame_nota_2,width=300,height=30,bg_color='transparent',fg_color='white')
        self.input_nota.place(relx=0.2,rely=0.5)
        self.button_salvar_nota_2 = customtkinter.CTkButton(master=self.frame_nota_2,width=200,height=40,fg_color="#0097b2",bg_color='transparent',text='lançar',text_color='black',command=self.verificar_nota_2)
        self.button_salvar_nota_2.place(relx=0.3,rely=0.65)
        
    ################
    ###### função da primeiro frame da nota 3
    ###################
    def adicionar_nota_3(self):
        self.frame_nota_3 = customtkinter.CTkFrame(master=self.janela_notas,width=500,height=400,fg_color='#d3d3d3',bg_color='transparent')
        self.frame_nota_3.place(relx=0.5,rely=0.2)
        label_sobre = customtkinter.CTkLabel(master=self.frame_nota_3,width=300,height=40,fg_color='transparent',bg_color='transparent',text='Deseja adicionar a primeira nota?',text_color='black')
        label_sobre.place(relx=0.2,rely=0.1)
        label_entrar = customtkinter.CTkLabel(master=self.frame_nota_3,width=300,height=30,fg_color='transparent',bg_color='transparent',text='CPF do Aluno',text_color='black')
        label_entrar.place(relx=0.2,rely=0.2)
        self.input_cpf = customtkinter.CTkEntry(master=self.frame_nota_3,width=300,height=30,bg_color='transparent',fg_color='white')
        self.input_cpf.place(relx=0.2,rely=0.3)
        label_entrar_nota = customtkinter.CTkLabel(master=self.frame_nota_3,width=300,height=30,fg_color='transparent',bg_color='transparent',text='Nota do Aluno',text_color='black')
        label_entrar_nota.place(relx=0.2,rely=0.4)
        self.input_nota = customtkinter.CTkEntry(master=self.frame_nota_3,width=300,height=30,bg_color='transparent',fg_color='white')
        self.input_nota.place(relx=0.2,rely=0.5)
        button_salvar_nota_3 = customtkinter.CTkButton(master=self.frame_nota_3,width=200,height=40,fg_color="#0097b2",bg_color='transparent',text='lançar',text_color='black',command=self.verificar_nota_3)
        button_salvar_nota_3.place(relx=0.3,rely=0.65)
    

    ############
    #### conectar o banco de dados
    def conexao_banco_1(self):
            self.conexao_1 = psycopg2.connect(database = "sistema", host= "localhost", user = "postgres",password="5115",port="5432")
    
    #######################
    ######## função de retorno de erro no servidor
    def aviso_erro_serve(self):
        self.frame_erro_serve = customtkinter.CTkFrame(master=self.janela_notas,width=900,height=100,fg_color='#0097b2',bg_color='transparent')
        self.frame_erro_serve.place(relx=0.17,rely=0.8)
        label_aviso = customtkinter.CTkLabel(master=self.frame_erro_serve,width=800,height=30,fg_color='transparent',bg_color='transparent',text='Erro no servidor',text_color='black',font=('Arial bold',18))
        label_aviso.place(relx=0.06,rely=0.1)
        aviso_label_grande = customtkinter.CTkLabel(master=self.frame_erro_serve,width=800,height=40,fg_color='transparent',bg_color='transparent',text='Servidor caiu, tente novamente',text_color='black',font=('Arial bold',17))
        aviso_label_grande.place(relx=0.06,rely=0.5)
        self.limpar_input()
        sleep(7)
        self.frame_erro_serve.destroy()
    

    #######################
    ###### Valida se tem 11 numeros do CPF 
    def validar_entrada_cpf_notas(self):
        cpf = self.input_cpf.get()
        if len(cpf) == 11 and cpf.isdigit():
            self.verificar_se_tem_esse_cpf_notas()
        else:
            self.aviso_cpf_incompleto()
    

    #########################
    ########## função que retorna uma aviso de cpf incompleto
    def aviso_cpf_incompleto(self):
        self.frame_erro = customtkinter.CTkFrame(master=self.janela_notas,width=900,height=100,fg_color='#0097b2',bg_color='transparent')
        self.frame_erro.place(relx=0.17,rely=0.8)
        aviso_label = customtkinter.CTkLabel(master=self.frame_erro,width=800,height=30,fg_color='transparent',bg_color='transparent',text='Cpf incompleto',text_color='black',font=('Arial bold',18))
        aviso_label.place(relx=0.06,rely=0.1)
        aviso_label_grande = customtkinter.CTkLabel(master=self.frame_erro,width=800,height=40,fg_color='transparent',bg_color='transparent',text='Insira os 11 numeros do CPF do aluno',text_color='black',font=('Arial bold',17))
        aviso_label_grande.place(relx=0.06,rely=0.5)
        self.limpar_input()
        sleep(7)
        self.frame_erro.destroy()

    #############################
    ###### função que verificar se existe esse cpf na informação aluno
    def verificar_se_tem_esse_cpf_notas(self):
        try:
            cpf_aluno = self.input_cpf.get()
            self.conexao_banco_1()
            cursor = self.conexao_1.cursor()
            sql_query = "SELECT cpf FROM aluno_info WHERE cpf = %s"
            cursor.execute(sql_query, (str(cpf_aluno),))
            self.resultado_verificar = cursor.fetchone()
            if self.resultado_verificar is not None:
                if self.verificar_nota_3:
                    self.salvando_notas_alunos_nota_3()
                elif self.verificar_nota_2:
                    self.salvando_notas_alunos_nota_2()
                else:
                    self.salvando_notas_alunos_nota_1()
            else:
                self.aviso_nao_tem_cpf()
        except psycopg2.Error:
            self.aviso_erro_serve()
    

    ##############################
    ########### função que retorna um aviso de não tem o cpf informado
    ###### na tabela da informação do aluno
    def aviso_nao_tem_cpf(self):
        self.frame_nao_tem_cpf = customtkinter.CTkFrame(master=self.janela_notas,width=900,height=100,fg_color='#0097b2',bg_color='transparent')
        self.frame_nao_tem_cpf.place(relx=0.17,rely=0.8)
        label_aviso = customtkinter.CTkLabel(master=self.frame_nao_tem_cpf,width=800,height=30,fg_color='transparent',bg_color='transparent',text='CPF não achado',text_color='black',font=('Arial bold',18))
        label_aviso.place(relx=0.06,rely=0.1)
        aviso_label_grande = customtkinter.CTkLabel(master=self.frame_nao_tem_cpf,width=800,height=40,fg_color='transparent',bg_color='transparent',text='Não tem aluno com esse CPF',text_color='black',font=('Arial bold',17))
        aviso_label_grande.place(relx=0.06,rely=0.5)
        self.limpar_input()
        sleep(7)
        self.frame_nao_tem_cpf.destroy()
    

    ##########################
    ############ função que retorna um aviso que já tem nota
    ######## no cpf informado
    def aviso_tem_nota(self):
        self.frame_tem_nota = customtkinter.CTkFrame(master=self.janela_notas,width=900,height=100,fg_color='#0097b2',bg_color='transparent')
        self.frame_tem_nota.place(relx=0.17,rely=0.8)
        label_aviso = customtkinter.CTkLabel(master=self.frame_tem_nota,width=800,height=30,fg_color='transparent',bg_color='transparent',text='Já tem nota',text_color='black',font=('Arial bold',18))
        label_aviso.place(relx=0.06,rely=0.1)
        aviso_label_grande = customtkinter.CTkLabel(master=self.frame_tem_nota,width=800,height=40,fg_color='transparent',bg_color='transparent',text='Esse aluno já tem nota desse semetre',text_color='black',font=('Arial bold',17))
        aviso_label_grande.place(relx=0.06,rely=0.5)
        self.limpar_input()
        sleep(7)
        self.frame_tem_nota.destroy()

    #####################
    ######## função que salva as notas do aluno no banco
    ###### nota 1 ou a primeira nota a ser inserida
    def salvando_notas_alunos_nota_1(self):
        try:
            aluno_cpf = self.input_cpf.get()
            nota = self.input_nota.get()
            self.conexao_banco_1()
            cursor = self.conexao_1.cursor()
            sql_query = "INSERT INTO notas(nota_1, cpf) VALUES (%s , %s)"
            cursor.execute(sql_query,(nota, aluno_cpf))
            self.conexao_1.commit()
            self.conexao_1.close()
            cursor.close()
            self.aviso_nota_salva()
        except psycopg2.Error:
            self.aviso_erro_serve()

    #####################
    ######## função que salva as notas do aluno no banco
    ###### nota 2 ou a segunda nota a ser inserida  
    def salvando_notas_alunos_nota_2(self):
        try:
            if():
                aluno_cpf = self.input_cpf.get()
                nota = self.input_nota.get()
                self.conexao_banco_1()
                cursor = self.conexao_1.cursor()
                sql_query = "UPDATE notas SET nota_2 = %s WHERE nota_2 IS NULL AND cpf = %s"
                cursor.execute(sql_query,(nota, aluno_cpf))
                self.conexao_1.commit()
                self.conexao_1.close()
                cursor.close()
                self.aviso_nota_salva()
            else:
                self.aviso_tem_nota()
        except psycopg2.Error:
            self.aviso_erro_serve()
    
    #####################
    ######## função que salva as notas do aluno no banco
    ###### nota 3 ou a terceira nota a ser inserida
    def salvando_notas_alunos_nota_3(self):
        try:
            if():
                aluno_cpf = self.input_cpf.get()
                nota = self.input_nota.get()
                self.conexao_banco_1()
                cursor = self.conexao_1.cursor()
                sql_query = "UPDATE notas SET nota_3 = %s WHERE nota_3 IS NULL AND cpf = %s"
                cursor.execute(sql_query,(nota, aluno_cpf))
                self.conexao_1.commit()
                self.conexao_1.close()
                cursor.close()
                self.aviso_nota_salva()
            else:
                self.aviso_tem_nota()
        except psycopg2.Error:
            self.aviso_erro_serve()
    
    #####################
    ######## função que avisa que a nota foi salva
    def aviso_nota_salva(self):
        self.frame_nota_salva = customtkinter.CTkFrame(master=self.janela_notas,width=900,height=100,fg_color='#0097b2',bg_color='transparent')
        self.frame_nota_salva.place(relx=0.17,rely=0.8)
        label_aviso = customtkinter.CTkLabel(master=self.frame_nota_salva,width=800,height=30,fg_color='transparent',bg_color='transparent',text='Nota salva',text_color='black',font=('Arial bold',18))
        label_aviso.place(relx=0.06,rely=0.1)
        aviso_label_grande = customtkinter.CTkLabel(master=self.frame_nota_salva,width=800,height=40,fg_color='transparent',bg_color='transparent',text='Nota foi salva com sucesso',text_color='black',font=('Arial bold',17))
        aviso_label_grande.place(relx=0.06,rely=0.5)
        self.limpar_input()
        sleep(7)
        self.frame_nota_salva.destroy()
    
    #########################
    ######## função que limpa os inputs
    def limpar_input(self):
        self.input_cpf.delete(0, 100)
        self.input_nota.delete(0, 100)
    
    #############################
    ######## função de verificar se tem a terceira nota já cadastrada
    def verificar_nota_3(self):
        try:
            aluno_cpf = self.input_cpf.get()
            self.conexao_banco_1()
            cursor = self.conexao_1.cursor()
            sql_query = "SELECT nota_1 FROM notas WHERE cpf = %s"
            cursor.execute(sql_query,(str(aluno_cpf),))
            resu_nota_1 = cursor.fetchone()
            if resu_nota_1 is not None:
                sql_query = "SELECT nota_3 FROM notas WHERE cpf = %s"
                cursor.execute(sql_query,(str(aluno_cpf),))
                self.resu_nota_3 = cursor.fetchone()
                if self.resu_nota_3 is not None:
                    self.validar_entrada_cpf_notas()
                else:
                    self.aviso_tem_nota()
            else:
                self.aviso_nota_1_nao_tem()
        except psycopg2.Error:
            self.aviso_erro_serve()
        
    #############################
    ######## função de verificar se tem a segunda nota já cadastrada
    def verificar_nota_2(self):
        try:
            aluno_cpf = self.input_cpf.get()
            self.conexao_banco_1()
            cursor = self.conexao_1.cursor()
            sql_query = "SELECT nota_1 FROM notas WHERE cpf = %s"
            cursor.execute(sql_query,(str(aluno_cpf),))
            resu_nota_1 = cursor.fetchone()
            if resu_nota_1 is not None:
                sql_query = "SELECT nota_2 FROM notas WHERE cpf = %s"
                cursor.execute(sql_query,(str(aluno_cpf),))
                self.resu_nota_2 = cursor.fetchone()
                if self.resu_nota_2 is not None:
                    self.validar_entrada_cpf_notas()
                else:
                    self.aviso_tem_nota()
            else:
                self.aviso_nota_1_nao_tem()
        except psycopg2.Error:
            self.aviso_erro_serve()
    
    #############################
    ######## função de verificar se tem a primeira nota já cadastrada
    def verificar_nota_1(self):
        try:
            aluno_cpf = self.input_cpf.get()
            self.conexao_banco_1()
            cursor = self.conexao_1.cursor()
            sql_query = "SELECT nota_1 FROM notas WHERE cpf = %s"
            cursor.execute(sql_query,(str(aluno_cpf),))
            resu_nota_1 = cursor.fetchone()
            if resu_nota_1 is None:
                self.validar_entrada_cpf_notas()
            else:
                self.aviso_tem_nota()
        except psycopg2.Error:
            self.aviso_erro_serve()
    

    ####################
    ######## função que retorna um aviso que não existe nota 1 cadastrada
    def aviso_nota_1_nao_tem(self):
        self.frame_nota_1_n_tem = customtkinter.CTkFrame(master=self.janela_notas,width=900,height=100,fg_color='#0097b2',bg_color='transparent')
        self.frame_nota_1_n_tem.place(relx=0.17,rely=0.8)
        label_aviso = customtkinter.CTkLabel(master=self.frame_nota_1_n_tem,width=800,height=30,fg_color='transparent',bg_color='transparent',text='Primeira nota',text_color='black',font=('Arial bold',18))
        label_aviso.place(relx=0.06,rely=0.1)
        aviso_label_grande = customtkinter.CTkLabel(master=self.frame_nota_1_n_tem,width=800,height=40,fg_color='transparent',bg_color='transparent',text='Insire a primeira nota antes',text_color='black',font=('Arial bold',17))
        aviso_label_grande.place(relx=0.06,rely=0.5)
        self.limpar_input()
        sleep(7)
        self.frame_nota_salva.destroy()

def chamando_notas():
    app = adicionar_notas()
    app.janela_notas.mainloop()