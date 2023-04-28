import mysql.connector
import tkinter as tk

class Prod:

    def __init__(self, master):
        self.master = master
        master.title("Produtos")

        self.connection()


        self.label_descricao = tk.Label(master, text="Descrição:")
        self.label_descricao.grid(row=0, column=0)

        self.entry_descricao = tk.Entry(master)
        self.entry_descricao.grid(row=0, column=1)

        self.label_valorP = tk.Label(master, text="Valor:")
        self.label_valorP.grid(row=1, column=0)

        self.entry_valorP = tk.Entry(master)
        self.entry_valorP.grid(row=1, column=1)

        self.label_categ = tk.Label(master, text="Categoria:")
        self.label_categ.grid(row=2, column=0)

        self.entry_categ = tk.Entry(master)
        self.entry_categ.grid(row=2, column=1)

        self.button_create = tk.Button(master, text="Criar", command=self.create)
        self.button_create.grid(row=3, column=0)

        self.button_read = tk.Button(master, text="Ler", command=self.read)
        self.button_read.grid(row=3, column=1)

        self.button_update = tk.Button(master, text="Atualizar", command=self.update)
        self.button_update.grid(row=4, column=0)

        self.button_delete = tk.Button(master, text="Deletar", command=self.delete)
        self.button_delete.grid(row=4, column=1)

        self.textbox = tk.Text(master)
        self.textbox.grid(row=5, column=0, columnspan=2)

    def connection(self):
        self.conex = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="ativextra"
        )

        self.cursor = self.conex.cursor()

    def create(self):
        descricao = self.entry_descricao.get()
        valorP = self.entry_valorP.get()
        categ = self.entry_categ.get()

        comad = f'INSERT INTO produto (descricao, valorP, categ) VALUES ("{descricao}", "{valorP}", "{categ}")'

        self.cursor.execute(comad)
        self.conex.commit()

    def update(self):
        qtd = self.entry_qtd.get()
        descricao = self.entry_descricao.get()
        valorP = self.entry_valorP.get()
        categ = self.entry_categ.get()

        comad = f"UPDATE produto SET descricao = '{descricao}', valorP = '{valorP}', categ = '{categ}' WHERE qtd = {qtd}"

        self.cursor.execute(comad)
        self.conex.commit()

    def delete(self):
        qtd = self.entry_qtd.get()

        comad = f"DELETE FROM produto WHERE qtd = '{qtd}'"

        self.cursor.execute(comad)
        self.conex.commit()

    def read(self):
        comad = 'SELECT * FROM produto'

        self.cursor.execute(comad)
        self.resultado = self.cursor.fetchall()

        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, self.resultado)

    def __del__(self):
        self.cursor.close()
        self.conex.close()

root = tk.Tk()
prod = Prod(root)
root.mainloop()
