from .bd_conexao import cursor, conexao_mysql
from funcoes import data_en_brasil
from prettytable import PrettyTable


def truncate(f, n):
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


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
    tableAluguel = PrettyTable()
    cursor.execute(
        "SELECT id FROM usuarios WHERE usuario = %s", (usuario,))
    id_usuario = cursor.fetchone()[0]
    cursor.execute(
        "SELECT * FROM alugueis WHERE id_usuario = %s", (id_usuario,))
    alugueis = cursor.fetchall()
    tableAluguel.field_names = ["ID", "ID_TRAJE",
                                "DATA_ALUGUEL", "DATA_DEVOLUCAO", "VALOR"]
    for aluguel in alugueis:
        tableAluguel.add_row(
            [aluguel[0], aluguel[2], data_en_brasil(aluguel[3]), data_en_brasil(aluguel[4]), f'R${truncate(aluguel[5],2)}'.replace('.', ',')])
    print(tableAluguel)
