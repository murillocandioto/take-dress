from bd_conexao import cursor, conexao_mysql
from funcoes import truncate
from prettytable import PrettyTable


def cadastrar_trajes(nome, valor, quantidade):
    cursor.execute(
        "INSERT INTO trajes (nome, valor, quantidade) VALUES (%s, %s, %s)", (nome, valor, quantidade))
    conexao_mysql.commit()


def mostrar_trajes():
    tableTrajes = PrettyTable()
    cursor.execute("SELECT * FROM trajes")
    trajes = cursor.fetchall()
    tableTrajes.field_names = ["ID", "NOME", "VALOR", "QUANTIDADE"]
    for traje in trajes:
        tableTrajes.add_row(
            [traje[0], traje[1], f"R${truncate(traje[2],2)}".replace('.', ','), traje[3]])
    print(tableTrajes)


def excluir_traje(id_traje):
    cursor.execute("DELETE FROM trajes WHERE id = %s", (id_traje,))
    conexao_mysql.commit()


def editar_trajes(id_traje, nome, preco, quantidade):
    cursor.execute("UPDATE trajes SET nome = %s, valor = %s, quantidade = %s WHERE id = %s",
                   (nome, preco, quantidade, id_traje))
    conexao_mysql.commit()


def verificar_traje(id_traje):
    cursor.execute("SELECT * FROM trajes WHERE id = %s", (id_traje,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def verificar_quantidade_traje(id_traje, quantidade):
    cursor.execute(
        "SELECT * FROM trajes WHERE id = %s AND quantidade >= %s", (id_traje, quantidade))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def valor_total_trajes(id_traje, quantidade):
    cursor.execute("SELECT * FROM trajes WHERE id = %s", (id_traje,))
    traje = cursor.fetchone()
    valor_total = traje[2] * quantidade
    return valor_total


def subtrair_trajes(id_traje, quantidade):
    cursor.execute(
        "UPDATE trajes SET quantidade = quantidade - %s WHERE id = %s", (quantidade, id_traje))
    conexao_mysql.commit()


def exportar_json():
    cursor.execute("SELECT * FROM trajes")
    trajes = cursor.fetchall()
    trajes_json = []
    for traje in trajes:
        trajes_json.append({
            "id": traje[0],
            "nome": traje[1],
            "valor": traje[2],
            "quantidade": traje[3]
        })
    return trajes_json
