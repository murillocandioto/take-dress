from bd_conexao import cursor, conexao_mysql
import json


def alugar_trajes():
    return


def excluir_aluguel():
    return


def listar_alugueis():
    return


def alterar_aluguel():
    return


def exportar_json():
    cursor.execute("SELECT * FROM alugueis")
    alugueis = cursor.fetchall()
    alugueis_json = []
    for aluguel in alugueis:
        alugueis_json.append({
            "id": aluguel[0],
            "id_usuario": aluguel[1],
            "id_traje": aluguel[2],
            "data_aluguel": aluguel[3],
            "data_devolucao": aluguel[4],
            "valor": aluguel[5]
        })
    return alugueis_json
