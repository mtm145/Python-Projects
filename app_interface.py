
from tkinter import *

from cadastro_pessoas import insert_table
from cadastro_pessoas import create_connection


database = r"F:\Estudos\python\pooTest\bancosqlite.db"
conn = create_connection(database)


def insertDatabase():
    try:
        insert_table(conn, f"""INSERT INTO pessoas (name, idade, email)
                        VALUES ('{nome_pessoa.get()}',
                        '{int(idade_pessoa.get())}',
                        '{email_pessoa.get()}'); """)
        alert.config(text="Usuário cadastrado com sucesso", bg='green')
    except ValueError:
        alert.config(
            text="Você não digitou um número, tente novamente!", bg='red')


root = Tk()
root.geometry('400x500')
root.title("Cadastro de pessoas")
pane = Frame(root,  borderwidth=1, relief='ridge')

pane.place(x=50, y=50, width=300, height=350)

Label(pane, text="Nome da pessoa:", justify='center').pack(
    side='top', ipadx=30, ipady=10)
nome_pessoa = Entry(pane)
nome_pessoa.pack(side='top', ipadx=30, ipady=6, )


Label(pane, text="Idade:", justify='center').pack(
    side='top', ipadx=30, ipady=10)
idade_pessoa = Entry(pane)
idade_pessoa.pack(
    side='top', ipadx=30, ipady=6)


Label(pane, text="Email:", justify='center').pack(
    side='top', ipadx=30, ipady=10)
email_pessoa = Entry(pane)
email_pessoa.pack(
    side='top', ipadx=30, ipady=6)


Button(pane, text="Cadastrar pessoa", command=insertDatabase).place(
    x=70, y=250, width=150, height=50)

alert = Label(root, text='', justify='center')
alert.pack(side='bottom', ipady=30)


root.mainloop()
