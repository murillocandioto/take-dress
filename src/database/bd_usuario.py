from .bd_conexao import conexao_mysql
from prettytable import PrettyTable


def verificar_usuario(usuario, senha):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha))
    result = cursor.fetchone()
    if result:
        conexao_mysqle.close()
        return True
    else:
        conexao_mysqle.close()
        return False


def pegar_id_usuario(usuario):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
    result = cursor.fetchone()
    conexao_mysqle.close()
    return result[0]


def senha_segura(senha):

    if len(senha) <= 8:
        print("A senha deve conter no mínimo 8 caracteres!")
        return False

    if senha.isdigit():
        print("A senha deve conter no mínimo 1 letra!")
        return False

    if senha.isalpha():
        print("A senha deve conter no mínimo 1 número!")
        return False

    if senha.isalnum():
        print("A senha deve conter no mínimo 1 caracter especial!")
        return False

    if senha.isupper():
        print("A senha deve conter no mínimo 1 minúscula!")
        return False

    if senha.islower():
        print("A senha deve conter no mínimo 1 maiúscula!")
        return False
    return True


def verificar_usuario_cadastrado(usuario):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
    result = cursor.fetchone()
    if result:
        conexao_mysqle.close()
        return True
    else:
        conexao_mysqle.close()
        return False


def cadastro(usuario, senha):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)", (usuario, senha))
    conexao_mysqle.commit()
    print("Cadastro realizado com sucesso!")
    conexao_mysqle.close()


def mostrar_usuario_logado(usuario):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
    result = cursor.fetchone()
    print(f"ID: {result[0]}")
    print(f"Usuário: {result[1]}")
    print(f"Senha: {result[2]}")
    conexao_mysqle.close()


def alterar_senha(usuario, senha):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute(
        "UPDATE usuarios SET senha = %s WHERE usuario = %s", (senha, usuario))
    conexao_mysqle.commit()
    print("Senha alterada com sucesso!")
    conexao_mysqle.close()


def exportar_json():
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    usuarios_json = []
    for usuario in usuarios:
        usuarios_json.append({
            "id": usuario[0],
            "usuario": usuario[1],
            "senha": usuario[2]
        })
    conexao_mysqle.close()
    return usuarios_json


def verificar_senha(usuario, senha):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha))
    result = cursor.fetchone()
    if result:
        conexao_mysqle.close()
        return True
    else:
        conexao_mysqle.close()
        return False


def alterar_senha_usuario(usuario, senha):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute(
        "UPDATE usuarios SET senha = %s WHERE usuario = %s", (senha, usuario))
    conexao_mysqle.commit()
    print("Senha alterada com sucesso!")
    conexao_mysqle.close()


def mostrar_todos_usuarios_cadastrados():
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    tableUsuarios = PrettyTable()
    tableUsuarios.field_names = ["ID", "Usuário", "Senha"]
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        tableUsuarios.add_row([usuario[0], usuario[1], usuario[2]])
    print(tableUsuarios)
    conexao_mysqle.close()


def excluir_usuario(usuario):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("DELETE FROM usuarios WHERE usuario = %s", (usuario,))
    conexao_mysqle.commit()
    print("Usuário excluído com sucesso!")
    conexao_mysqle.close()
