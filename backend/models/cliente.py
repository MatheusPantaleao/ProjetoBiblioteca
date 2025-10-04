from .pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, cpf, nome, idade, email, numero, matricula: str):
        super().__init__(cpf, nome, idade, email, numero)
        self.matricula = matricula

    def mostrar_dados(self):
        dados = super().mostrar_dados()
        dados["matricula"] = self.matricula
        return dados
