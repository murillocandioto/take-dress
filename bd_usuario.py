from bd_conexao import cursor, conexao_mysql


def verificar_usuario(usuario, senha):
    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def pegar_id_usuario(usuario):
    cursor.execute("SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
    result = cursor.fetchone()
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
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def cadastro(usuario, senha):
    cursor.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)", (usuario, senha))
    conexao_mysql.commit()
    print("Cadastro realizado com sucesso!")


def mostrar_usuario_logado(usuario):
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
    result = cursor.fetchone()
    print(f"ID: {result[0]}")
    print(f"Usuário: {result[1]}")
    print(f"Senha: {result[2]}")


def alterar_senha(usuario, senha):
    cursor.execute(
        "UPDATE usuarios SET senha = %s WHERE usuario = %s", (senha, usuario))
    conexao_mysql.commit()
    print("Senha alterada com sucesso!")


def exportar_json():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    usuarios_json = []
    for usuario in usuarios:
        usuarios_json.append({
            "id": usuario[0],
            "usuario": usuario[1],
            "senha": usuario[2]
        })
    return usuarios_json


def verificar_senha(usuario, senha):
    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def alterar_senha_usuario(usuario, senha):
    cursor.execute(
        "UPDATE usuarios SET senha = %s WHERE usuario = %s", (senha, usuario))
    conexao_mysql.commit()
    print("Senha alterada com sucesso!")
