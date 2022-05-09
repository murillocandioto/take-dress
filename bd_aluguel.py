from bd_conexao import cursor, conexao_mysql


def alugar_trajes(id_usuario, id_traje, data_aluguel, data_devolucao, valor):
    cursor.execute("INSERT INTO alugueis (id_usuario, id_traje, data_aluguel, data_devolucao, valor) VALUES (%s, %s, %s, %s, %s)",
                   (id_usuario, id_traje, data_aluguel, data_devolucao, valor))
    conexao_mysql.commit()


def verificar_aluguel(usuario, id_aluguel):
    cursor.execute(
        "SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
    id_usuario = cursor.fetchone()[0]
    cursor.execute(
        "SELECT id FROM alugueis WHERE id_usuario = %s AND id =%s", (id_usuario, id_aluguel))
    if cursor.fetchone():
        return True
    else:
        return False


def excluir_aluguel(usuario, id_aluguel):
    cursor.execute(
        "SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
    id_usuario = cursor.fetchone()[0]
    cursor.execute(
        "DELETE FROM alugueis WHERE id = %s AND id_usuario = %s", (id_aluguel, id_usuario))
    conexao_mysql.commit()


def exportar_json():
    cursor.execute("SELECT * FROM alugueis")
    alugueis = cursor.fetchall()
    alugueis_json = []
    for aluguel in alugueis:
        alugueis_json.append({
            "id": aluguel[0],
            "id_usuario": aluguel[1],
            "id_traje": aluguel[2],
            "data_aluguel": f"{aluguel[3]}",
            "data_devolucao": f"{aluguel[4]}",
            "valor": aluguel[5]
        })
    return alugueis_json


def mostrar_alugueis_usuario(usuario):
    cursor.execute(
        "SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
    id_usuario = cursor.fetchone()[0]
    cursor.execute(
        "SELECT * FROM alugueis WHERE id_usuario = %s", (id_usuario,))
    alugueis = cursor.fetchall()
    for aluguel in alugueis:
        print(
            f"ID do aluguel: {aluguel[0]} \t ID do usuario: {aluguel[1]} \t ID do traje: {aluguel[2]} \t Data do aluguel: {aluguel[3]} \t Data da devolução: {aluguel[4]} \t Valor: R${aluguel[5]}")
