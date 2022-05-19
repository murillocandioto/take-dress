class Usuario:
    def __init__(self, id, usuario, senha):
        self.id = id
        self.usuario = usuario
        self.senha = senha

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_senha(self, senha):
        self.senha = senha

    def set_id(self, id):
        self.id = id

    def get_usuario(self):
        return self.usuario

    def get_senha(self):
        return self.senha

    def get_id(self):
        return self.id

    def __str__(self):
        return f"{self.id} - {self.usuario} - {self.senha}"
