import fornecedor


class prod (fornecedor.fornecedor):

    def __init__(self, descricao, valorP, categ):
        super().__init__(fornecedor.nome, fornecedor.Fvalor)

    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        if descricao == '':
            raise ValueError(' Descrição errado')
        self.__descricao = descricao.upper()

    @property
    def categ(self):
        return self.__categ

    @categ.setter
    def categ(self, categ):
        if categ == '':
            raise ValueError('Categoria errada')
        self.__categ = categ.upper()

    @property
    def valorP(self):
        return self.__valorP

    @valorP.setter
    def valorP(self, valorP):
        if valorP == '':
            raise ValueError('Valor errado')
        self.__valorP = valorP.upper()



