from .bd_conexao import conexao_mysql
from prettytable import PrettyTable
from api import *
from PIL import Image
import io


def save_blob_image_on_database(image, name):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute(
        "INSERT INTO imagens (imagem,nome) VALUES (%s, %s)", (image, name,))
    conexao_mysqle.commit()
    conexao_mysqle.close()


def mostrar_todas_as_imagens_em_uma_tabela():
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT * FROM imagens")
    imagens = cursor.fetchall()
    table = PrettyTable(["ID", "Nome"])
    for imagem in imagens:
        table.add_row(
            [imagem[0], imagem[2]])
    print(table)
    conexao_mysqle.close()


def verificar_imagem(id_imagem):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT * FROM imagens WHERE id = %s", (id_imagem,))
    result = cursor.fetchone()
    if result:
        conexao_mysqle.close()
        return True
    else:
        conexao_mysqle.close()
        return False


def mostrar_imagem_na_tela(id):
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT * FROM imagens WHERE id = %s", (id,))
    imagem = cursor.fetchone()
    img = Image.open(io.BytesIO(imagem[1]))
    img.show()
    conexao_mysqle.close()


def exportar_json():
    conexao_mysqle = conexao_mysql()
    cursor = conexao_mysqle.cursor()
    cursor.execute("SELECT * FROM imagens")
    imagens = cursor.fetchall()
    imagens_json = []
    for imagem in imagens:
        imagens_json.append({
            "id": imagem[0],
            "imagem": str(imagem[1]),
            "nome": imagem[2],
        })
    conexao_mysqle.close()
    return imagens_json
