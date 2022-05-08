class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.senha}"
