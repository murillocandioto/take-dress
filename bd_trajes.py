from bd_conexao import cursor, conexao_mysql
import json


def truncate(f, n):
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


def cadastrar_trajes(nome, valor, quantidade):
    cursor.execute(
        "INSERT INTO trajes (nome, valor, quantidade) VALUES (%s, %s, %s)", (nome, valor, quantidade))
    conexao_mysql.commit()


def mostrar_trajes():
    cursor.execute("SELECT * FROM trajes")
    trajes = cursor.fetchall()
    for traje in trajes:
        print(
            f"ID do traje: {traje[0]} \t Nome: {traje[1]} \t Preço: R${truncate(traje[2],2).replace('.',',')} \t Quantidade: {traje[3]}")


def excluir_trajes(id_traje):
    cursor.execute("DELETE FROM trajes WHERE id = %s", (id_traje,))
    conexao_mysql.commit()


def editar_trajes(id_traje, nome, preco, quantidade):
    cursor.execute("UPDATE trajes SET nome = %s, preco = %s, quantidade = %s WHERE id = %s",
                   (nome, preco, quantidade, id_traje))
    conexao_mysql.commit()


def diminuir_um_traje(id_traje):
    cursor.execute(
        "UPDATE trajes SET quantidade = quantidade - 1 WHERE id = %s", (id_traje,))
    conexao_mysql.commit()


def adicionar_um_traje(id_traje):
    cursor.execute(
        "UPDATE trajes SET quantidade = quantidade + 1 WHERE id = %s", (id_traje,))
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
