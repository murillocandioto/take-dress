from .bd_conexao import cursor, conexao_mysql
from prettytable import PrettyTable
from api import *
from PIL import Image
import io


def save_blob_image_on_database(image, name):
    cursor.execute(
        "INSERT INTO imagens (imagem,nome) VALUES (%s, %s)", (image, name,))
    conexao_mysql.commit()


def mostrar_todas_as_imagens_em_uma_tabela():
    cursor.execute("SELECT * FROM imagens")
    imagens = cursor.fetchall()
    table = PrettyTable(["ID", "Nome"])
    for imagem in imagens:
        table.add_row(
            [imagem[0], imagem[2]])
    print(table)


def verificar_imagem(id_imagem):
    cursor.execute("SELECT * FROM imagens WHERE id = %s", (id_imagem,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def mostrar_imagem_na_tela(id):
    cursor.execute("SELECT * FROM imagens WHERE id = %s", (id,))
    imagem = cursor.fetchone()
    img = Image.open(io.BytesIO(imagem[1]))
    img.show()
