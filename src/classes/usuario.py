class Usuario:
    def __init__(self, id, usuario, senha, admin=False):
        self.id = id
        self.usuario = usuario
        self.senha = senha
        self.admin = admin

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_senha(self, senha):
        self.senha = senha

    def set_id(self, id):
        self.id = id

    def set_admin(self, admin):
        self.admin = admin

    def get_usuario(self):
        return self.usuario

    def get_senha(self):
        return self.senha

    def get_id(self):
        return self.id

    def get_admin(self):
        return self.admin

    def __str__(self):
        return f"{self.id} - {self.usuario} - {self.senha}"
