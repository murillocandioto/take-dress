from database.bd_usuario import exportar_json as json_usuarios
from database.bd_trajes import exportar_json as json_trajes
from database.bd_aluguel import exportar_json as json_alugueis
import json
import zipfile
import os


def colocar_jsons_em_arquivos():
    with open("usuarios.json", "w") as f:
        json.dump(json_usuarios(), f)
    with open("trajes.json", "w") as f:
        json.dump(json_trajes(), f)
    with open("alugueis.json", "w") as f:
        json.dump(json_alugueis(), f)


def zipar_jsons():
    with zipfile.ZipFile("jsons.zip", "w") as zip_file:
        zip_file.write("usuarios.json")
        zip_file.write("trajes.json")
        zip_file.write("alugueis.json")
    os.remove("usuarios.json")
    os.remove("trajes.json")
    os.remove("alugueis.json")
    print("Arquivos zipados com sucesso!")
