class fornecedor:
    def __init__(self, nome, Fvalor):
        self.__nome = nome
        self.__Fvalor = Fvalor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if nome == '':
            raise ValueError(' Nome invalido')
        self.__nome = nome.upper()

    @property
    def Fvalor(self):
        return self._Fvalor

    @Fvalor.setter
    def Fvalor(self, Fvalor):
        if Fvalor == '':
            raise ValueError(' Valor invalido')
        self.__Fvalor = Fvalor.upper()