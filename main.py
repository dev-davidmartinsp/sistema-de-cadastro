import tkinter as tk
import sqlite3


janela=tk.Tk()
janela.title("cadastro e login")
janela.attributes("-fullscreen", True)

conexao = sqlite3.connect("funcionarios.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")
conexao.commit()
conexao.close()

def cadastro():
    janela.withdraw()
    janela2=tk.Toplevel()
    janela2.title("Cadastro")
    janela2.attributes("-fullscreen", True)

    frame_cabecalho2=tk.Frame(janela2, bg="#00EEFF", height=60)
    frame_cabecalho2.grid(row=1, column=0, sticky="ew")
    frame_cabecalho2.columnconfigure(0, weight=1)

    janela2.columnconfigure(0, weight=1)
    btn_login=tk.Button(frame_cabecalho2, text="Login", font=("Arial", 15, "bold"),bg="#00EEFF", bd=0, command=login)
    btn_login.grid(row=0, column=0, padx=20)

    janela2.columnconfigure(0, weight=1)

    cd_label1=tk.Label(janela2, text="Cadastro", font=("Arial", 30))
    cd_label1.grid(row=2, column=0, pady=20)
    
    frame_central=tk.Frame(janela2, width=480, height=340)
    frame_central.grid(row=3, column=0, pady=20)

    frame_central.columnconfigure(1, weight=1)

    cd_label2=tk.Label(frame_central, text="Nome:", font=("Arial", 20))
    cd_label2.grid(row=0, column=0)
    
    entry_nome=tk.Entry(frame_central, font=("Arial", 20))
    entry_nome.grid(row=0, column=1, sticky="ew")

    cd_label3=tk.Label(frame_central, text="E-mail:", font=("Arial", 20))
    cd_label3.grid(row=1, column=0)

    entry_email=tk.Entry(frame_central, font=("Arial", 20))
    entry_email.grid(row=1, column=1, sticky="ew")

    cd_label4=tk.Label(frame_central, text="Senha:", font=("Arial", 20))
    cd_label4.grid(row=2, column=0)

    entry_senha=tk.Entry(frame_central, font=("Arial", 20), show="*")
    entry_senha.grid(row=2, column=1, sticky="ew")

    cd_label5=tk.Label(janela2, text="", font=("Arial", 20))
    cd_label5.grid(row=5, column=0)
    def cadastrar():
        nome=entry_nome.get()
        email=entry_email.get()
        senha=entry_senha.get()

        if not nome or not email or not senha:
            cd_label5.config(text="Erro, preencha todos os campos")
            return
        try:
            conexao=sqlite3.connect("funcionarios.db")
            cursor=conexao.cursor()
            cursor.execute("INSERT INTO funcionarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
            conexao.commit()
            cd_label5.config(text=" Usuário cadastrado com sucesso!")
            

        except sqlite3.IntegrityError:
            cd_label5.config(text="E-mail já cadastrado")
        finally:
            conexao.close()

    btn_cadastrar=tk.Button(janela2,text="cadastrar", underline=1, font=("Arial", 15, "bold"), bd=0, command= cadastrar)
    btn_cadastrar.grid(row=4, column=0)

def login():
    janela.withdraw()
    janela3=tk.Toplevel()
    janela3.title("Cadastro")
    janela3.attributes("-fullscreen", True)

    frame_cabecalho2=tk.Frame(janela3, bg="#00EEFF", height=60)
    frame_cabecalho2.grid(row=1, column=0, sticky="ew")
    frame_cabecalho2.columnconfigure(0, weight=1)

    janela3.columnconfigure(0, weight=1)
    btn_login=tk.Button(frame_cabecalho2, text="cadastro", font=("Arial", 15, "bold"),bg="#00EEFF", bd=0, command=cadastro)
    btn_login.grid(row=0, column=0, padx=20)

    janela3.columnconfigure(0, weight=1)

    lg_label1=tk.Label(janela3, text="Login", font=("Arial", 30))
    lg_label1.grid(row=2, column=0, pady=20)
    
    frame_central=tk.Frame(janela3, width=480, height=340)
    frame_central.grid(row=3, column=0, pady=20)

    frame_central.columnconfigure(1, weight=1)

    lg_label2=tk.Label(frame_central, text="Nome:", font=("Arial", 20))
    lg_label2.grid(row=0, column=0)
    
    lg_entry_nome=tk.Entry(frame_central, font=("Arial", 20))
    lg_entry_nome.grid(row=0, column=1, sticky="ew")

    lg_label3=tk.Label(frame_central, text="E-mail:", font=("Arial", 20))
    lg_label3.grid(row=1, column=0)

    lg_entry_email=tk.Entry(frame_central, font=("Arial", 20))
    lg_entry_email.grid(row=1, column=1, sticky="ew")

    lg_label4=tk.Label(frame_central, text="Senha:", font=("Arial", 20))
    lg_label4.grid(row=2, column=0)

    lg_entry_senha=tk.Entry(frame_central, font=("Arial", 20), show="*")
    lg_entry_senha.grid(row=2, column=1, sticky="ew")

    lg_label5 = tk.Label(janela3, text="", font=("Arial", 20))
    lg_label5.grid(row=5, column=0)


    def verificar_login():
        nome=lg_entry_nome.get()
        email=lg_entry_email.get()
        senha=lg_entry_senha.get()

        if not nome or not senha or not email:
            lg_label5.config(text="Preencha todos os campos")
            return
        
        conexao=sqlite3.connect("funcionarios.db")
        cursor=conexao.cursor()

        cursor.execute(
            "SELECT * FROM funcionarios WHERE nome=? AND email=? AND senha=?", (nome,email, senha)
        )
        funcionario=cursor.fetchone()
        conexao.close()

        if funcionario:
            janela3.withdraw()
            janela4=tk.Toplevel()
            janela4.title("Cadastro")
            janela4.attributes("-fullscreen", True)

            frame_cabecalho2=tk.Frame(janela4, bg="#00EEFF", height=60)
            frame_cabecalho2.grid(row=1, column=0, sticky="ew")
            frame_cabecalho2.columnconfigure(0, weight=1)

            janela4.columnconfigure(0, weight=1)
            btn_cadastro=tk.Button(frame_cabecalho2, text="Cadastro", font=("Arial", 15 ,"bold"),bg="#00EEFF",bd=0, command=cadastro)
            btn_cadastro.grid(row=0, column=0, padx=20)

            btn_login=tk.Button(frame_cabecalho2, text="Login", font=("Arial", 15, "bold"),bg="#00EEFF", bd=0, command=login)
            btn_login.grid(row=0, column=1)

            janela4.columnconfigure(0, weight=1)

            lg_label1=tk.Label(janela4, text="Tela para funcionários", font=("Arial", 30))
            lg_label1.grid(row=2, column=0, pady=20)
    
            frame_central=tk.Frame(janela4, width=480, height=340)
            frame_central.grid(row=3, column=0, pady=20)

            frame_central.columnconfigure(1, weight=1)

        else:
            lg_label5.config(text="Nome, e-mail ou senha incorretos")
    btn_entrar = tk.Button(janela3,text="Entrar",font=("Arial", 15, "bold"),bd=0,command=verificar_login)
    btn_entrar.grid(row=4, column=0)
    
janela.columnconfigure(0, weight=1)

frame_cabecalho=tk.Frame(janela, bg="#00EEFF", height=60)
frame_cabecalho.grid(row=1, column=0, sticky="ew")

btn_cadastro=tk.Button(frame_cabecalho, text="Cadastro", font=("Arial", 15 ,"bold"),bg="#00EEFF",bd=0, command=cadastro)
btn_cadastro.grid(row=0, column=0, padx=20)

btn_login=tk.Button(frame_cabecalho, text="Login", font=("Arial", 15, "bold"),bg="#00EEFF", bd=0, command=login)
btn_login.grid(row=0, column=1)
janela.columnconfigure(0, weight=1)

label1=tk.Label(janela, text="SEJA BEM-VINDO", font=("Arial", 30))
label1.grid(row=2, column=0, pady=20)

label2=tk.Label(janela, text="Eu sou o David, sou um estudante de Desenvolvimento de sistemas.Conheça meu código:Este é um sistema de cadastro e login para funcionários de uma empresa que precisam fazer login para que possam trabalhar", font=("Arial", 20), wraplength=700, justify="left")
label2.grid(row=3, column=0, pady=20)

label3=tk.Label(janela, text="Conheça a empresa:", font=("Arial", 25))
label3.grid(row=4, column=0)

label4=tk.Label(janela, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", font=("Arial", 20), wraplength=700, justify="left")
label4.grid(row=5, column=0, pady=20)


janela.mainloop()
