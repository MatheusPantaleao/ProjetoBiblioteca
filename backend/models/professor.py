from .pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, cpf, nome, idade, email, numero, area: str):
        super().__init__(cpf, nome, idade, email, numero)
        self.area = area

    def mostrar_dados(self):
        dados = super().mostrar_dados()
        dados["area"] = self.area
        return dados
