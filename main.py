import mysql.connector

class prod:

    def connection(self):
        self.conex = mysql.connector.conect(
            host="localhost",
            user = "root",
            password = "1234",
            database = "ativextra"
        )

        self.cursor = self.conex.cursor()

    def create(self, descricao, valorP, categ):
        comad = f'INSERT INTO produto (descricao, valorP, categ) VALUES ("{descricao}", "{valorP}", "{categ}")'

        self.cursor.execute(comad)
        self.conex.comit()

    def update(self, qtd, descricao, valorP, categ):
        comad = f"UPDATE produto SET descricao = '{descricao}', valorP = '{valorP}', categ = '{categ}' WHERE qtd = {qtd}"

        self.cursor.execute(comad)
        self.conex.commit()

    def delete(self, qtd):
        comad = f"DELETE FROM produto WHERE qtd = '{qtd}'"

        self.cursor.execute(comad)
        self.conex.commit()

        self.cursor.close()
        self.conex.close()


    def read(self):
        comad = 'SELECT * FROM produto'

        self.cursor.execute(comad)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)

        self.cursor.close()
        self.conex.close()