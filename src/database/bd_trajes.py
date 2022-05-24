from .bd_conexao import conexao_mysql
from funcoes import truncate
from prettytable import PrettyTable


def cadastrar_trajes(nome, valor, quantidade):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute(
        "INSERT INTO trajes (nome, valor, quantidade) VALUES (%s, %s, %s)", (nome, valor, quantidade))
    conexao_mysqle.commit()
    conexao_mysqle.close()


def mostrar_trajes(admin_usuario):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    tableTrajes = PrettyTable()
    if admin_usuario:
        cursor.execute("SELECT * FROM trajes")
    else:
        cursor.execute("SELECT * FROM trajes WHERE quantidade != 0")
    trajes = cursor.fetchall()
    tableTrajes.field_names = ["ID", "NOME", "VALOR", "QUANTIDADE"]
    for traje in trajes:
        tableTrajes.add_row(
            [traje[0], traje[1], f"R${truncate(traje[2],2)}".replace('.', ','), traje[3]])
    print(tableTrajes)
    conexao_mysqle.close()


def excluir_traje(id_traje):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("DELETE FROM trajes WHERE id = %s", (id_traje,))
    conexao_mysqle.commit()
    conexao_mysqle.close()


def editar_trajes(id_traje, nome, preco, quantidade):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("UPDATE trajes SET nome = %s, valor = %s, quantidade = %s WHERE id = %s",
                   (nome, preco, quantidade, id_traje))
    conexao_mysqle.commit()
    conexao_mysqle.close()


def verificar_traje(id_traje):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT * FROM trajes WHERE id = %s", (id_traje,))
    result = cursor.fetchone()
    if result:
        conexao_mysqle.close()
        return True
    else:
        conexao_mysqle.close()
        return False


def verificar_quantidade_traje(id_traje, quantidade):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute(
        "SELECT * FROM trajes WHERE id = %s AND quantidade >= %s AND quantidade != 0", (id_traje, quantidade))
    result = cursor.fetchone()
    if result:
        conexao_mysqle.close()
        return True
    else:
        conexao_mysqle.close()
        return False


def valor_total_trajes(id_traje, quantidade):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT * FROM trajes WHERE id = %s", (id_traje,))
    traje = cursor.fetchone()
    valor_total = traje[2] * quantidade
    conexao_mysqle.close()
    return valor_total


def subtrair_trajes(id_traje, quantidade):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute(
        "UPDATE trajes SET quantidade = quantidade - %s WHERE id = %s", (quantidade, id_traje))
    conexao_mysqle.commit()
    conexao_mysqle.close()


def exportar_json():
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
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
    conexao_mysqle.close()
    return trajes_json
