from database.bd_usuario import *
from database.bd_trajes import *
from database.bd_aluguel import *
from export_json import *
import time
import os
from getpass import getpass
from classes.usuario import Usuario
from datetime import date, timedelta

usuario = Usuario(1, '', '')


def truncate(f, n):
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


def exportar_jsons():
    os.system("cls")
    print("Exportando JSONS...")
    colocar_jsons_em_arquivos()
    print("JSONS exportados com sucesso!")
    time.sleep(2)
    menu_escolhas()


def cadastrar_trajes_opcao():
    try:
        os.system("cls")
        print("-------------------- CADASTRO DE TRAJES --------------------")
        nome = input("Digite o nome do traje: ")
        valor = truncate(float(
            ''.join(input("Digite o valor do traje: R$ ").split('.')).replace(',', '.')), 2)
        quantidade = int(input("Digite a quantidade de trajes: "))
        cadastrar_trajes(nome, valor, quantidade)
        print("Traje cadastrado com sucesso!")
        time.sleep(2)
    except Exception as e:
        print("Erro: ", e)
        time.sleep(2)
        cadastrar_trajes_opcao()


def mostrar_trajes_opcao():
    os.system("cls")
    print("-------------------- TRAJES --------------------")
    mostrar_trajes()
    input("Digite qualquer tecla para voltar: ")
    menu_escolhas()


def excluir_trajes_opcao():
    try:
        os.system("cls")
        print("-------------------- EXCLUIR TRAJE --------------------")
        id_traje = input("Digite o nome do traje que deseja excluir: ")
        if verificar_traje(id_traje):
            excluir_traje(id_traje)
            print("Traje excluido com sucesso!")
            time.sleep(2)
        else:
            print("Traje não encontrado!")
            time.sleep(2)
        menu_escolhas()
    except Exception as e:
        print("Erro: ", e)
        print("Não é possível excluir um traje que já foi alugado!!!!!!!!")
        time.sleep(2)
        menu_escolhas()


def alugar_trajes_opcao():
    try:
        os.system("cls")
        print("-------------------- ALUGUEL DE TRAJES --------------------")
        id_traje = input("Digite o id do traje que deseja alugar: ")
        if verificar_traje(id_traje):
            quantidade = int(
                input("Digite a quantidade de trajes que deseja alugar: "))
            if verificar_quantidade_traje(id_traje, quantidade):
                data_aluguel = date.today()
                data_devolucao = date.today() + timedelta(7)
                valor = valor_total_trajes(id_traje, quantidade)
                os.system('cls')
                print(usuario.id)
                time.sleep(2)
                alugar_trajes(usuario.id, id_traje, data_aluguel,
                              data_devolucao, valor)
                subtrair_trajes(id_traje, quantidade)
                print("Traje alugado com sucesso!")
                time.sleep(2)
            else:
                print("Quantidade de trajes insuficiente!")
                time.sleep(2)
        else:
            print("Traje não encontrado!")
            time.sleep(2)
        menu_escolhas()
    except Exception as e:
        print("Erro: ", e)
        time.sleep(2)
        menu_escolhas()


def tela_inicial():
    menu_cadastro()
    opcao_tela_inicial = input("Digite sua opção: ")
    if opcao_tela_inicial == "1":
        login()
    elif opcao_tela_inicial == "2":
        cadastrar()
    elif opcao_tela_inicial == "3":
        sobre()
    elif opcao_tela_inicial == "4":
        print("Saindo...")


def menu_cadastro():
    os.system("cls")
    print("-------------------- TAKE DRESS --------------------")
    print("1 - Login")
    print("2 - Cadastrar")
    print("3 - Sobre")
    print("4 - Sair")


def sobre():
    os.system("cls")
    print("-------------------- SOBRE --------------------")
    print("O aplicativo Take-Dress tem o objetivo de oferecer um serviço \nde cadastro e aluguel de trajes.\n")
    print("Desenvolvedor 1: Dora Yovana\t Matrícula: 2840482123040")
    print("Desenvolvedor 2: Daoud Elias\t Matrícula: 2840482123040")
    print("Desenvolvedor 3: Murillo H.C\t Matrícula: 2840482123040\n")
    segura = input("Digite qualquer tecla para voltar: ")
    tela_inicial()


def cadastrar():
    os.system("cls")
    print("-------------------- CADASTRO DE USUÁRIO --------------------")
    usuario.set_usuario(input("Digite seu usuário: "))
    if verificar_usuario_cadastrado(usuario.get_usuario()):
        print("Usuário já cadastrado!")
        tentar = input("Deseja tentar novamente? (S/N): ")
        if tentar == "S":
            cadastrar()
        else:
            tela_inicial()
    else:
        usuario.set_senha(getpass("Digite sua senha: "))
        while senha_segura(usuario.get_senha()) == False:
            usuario.set_senha(getpass("Digite sua senha: "))

        cadastro(usuario.get_usuario(), usuario.get_senha())
        time.sleep(3)
        tela_inicial()


def login():
    os.system("cls")
    print("-------------------- LOGIN --------------------")

    usuario.set_usuario(input("Digite seu usuário: "))
    usuario.set_senha(getpass("Digite sua senha: "))

    if verificar_usuario(usuario.get_usuario(), usuario.get_senha()):
        usuario.set_id(pegar_id_usuario(usuario.get_usuario()))
        print("Login realizado com sucesso!")
        menu_escolhas()
    else:
        print("Usuário ou senha incorretos!")
        tentar = input("Deseja tentar novamente? (S/N): ")
        if tentar == "S":
            login()
        else:
            tela_inicial()


def mostrar_dados_usuario():
    os.system("cls")
    print("-------------------- DADOS DO USUÁRIO --------------------")
    senha = getpass("Digite sua senha para ver seus dados: ")
    if verificar_usuario(usuario.get_usuario(), senha):
        mostrar_usuario_logado(usuario.get_usuario())
        controle = input("Digite qualquer tecla para voltar: ")
        menu_escolhas()
    else:
        print("Senha incorreta!")
        tentar = input("Deseja tentar novamente? (S/N): ")
        if tentar == "S":
            mostrar_dados_usuario()
        else:
            menu_escolhas()


def alterar_senha():
    os.system("cls")
    print("-------------------- ALTERAR SENHA --------------------")
    if verificar_usuario_cadastrado(usuario.get_usuario()):
        usuario.set_senha(getpass("Digite sua senha atual: "))
        if verificar_senha(usuario.get_usuario(), usuario.get_senha()):
            usuario.set_senha(getpass("Digite sua nova senha: "))
            while senha_segura(usuario.get_senha()) == False:
                usuario.set_senha(getpass("Digite sua nova senha: "))
            alterar_senha_usuario(usuario.get_usuario(), usuario.get_senha())
            time.sleep(2)
            menu_escolhas()
        else:
            print("Senha incorreta!")
            tentar = input("Deseja tentar novamente? (S/N): ")
            if tentar == "S":
                alterar_senha()
            else:
                menu_escolhas()


def mostrar_alugueis_usuario_opcao():
    os.system("cls")
    print("-------------------- ALUGUEIS --------------------")
    mostrar_alugueis_usuario(usuario.get_usuario())
    controle = input("Digite qualquer tecla para voltar: ")
    menu_escolhas()


def excluir_aluguel_opcao():
    try:
        os.system("cls")
        print("-------------------- EXCLUIR ALUGUEL --------------------")
        aluguel = int(input("Digite o número do aluguel que deseja excluir: "))
        if verificar_aluguel(usuario.get_usuario(), aluguel):
            excluir_aluguel(usuario.get_usuario(), aluguel)
            print("Aluguel excluído com sucesso!")
            time.sleep(2)
            menu_escolhas()
        else:
            print("Aluguel não encontrado!")
            tentar = input("Deseja tentar novamente? (S/N): ")
            if tentar == "S":
                excluir_aluguel_opcao()
            else:
                menu_escolhas()
    except:
        print("Provavelmente você digitou um número inválido!")
        time.sleep(2)
        menu_escolhas()


def editar_trajes_opcao():
    try:
        os.system("cls")
        print("-------------------- EDITAR TRAJES --------------------")
        id_traje = int(input("Digite o número do traje que deseja editar: "))
        if verificar_traje(id_traje):
            nome = input("Digite o novo nome do traje: ")
            preco = truncate(float(
                ''.join(input("Digite o valor do traje: R$ ").split('.')).replace(',', '.')), 2)
            quantidade = int(input("Digite a nova quantidade do traje: "))
            editar_trajes(id_traje, nome, preco, quantidade)
            print("Traje editado com sucesso!")
            time.sleep(2)
            menu_escolhas()
        else:
            print("Traje não encontrado!")
            tentar = input("Deseja tentar novamente? (S/N): ")
            if tentar == "S":
                editar_trajes_opcao()
            else:
                menu_escolhas()
    except:
        print("Provavelmente você digitou um valor inválido!")
        time.sleep(2)
        menu_escolhas()


def menu():
    os.system("cls")
    print("-------------------- TAKE DRESS --------------------")
    print("1 - Cadastrar trajes")
    print("2 - Mostrar trajes")
    print("3 - Editar trajes")
    print("4 - Excluir trajes")
    print("5 - Alugar trajes")
    print("6 - Mostrar alugueis")
    print("7 - Excluir alugueis")
    print("8 - Alterar minha senha")
    print("9 - Mostrar meu id, usuário e senha")
    print("10 - Importar dados da API")
    print("11 - Mostrar dados importados")
    print("12 - Exportar dados para JSON")
    print("13 - Zipar JSONS")
    print("14 - Sair")


def menu_escolhas():
    escolha = "1"
    while escolha != "13":
        menu()
        escolha = input("Digite sua opção: ")
        if escolha == "1":
            cadastrar_trajes_opcao()
        elif escolha == "2":
            mostrar_trajes_opcao()
        elif escolha == "3":
            editar_trajes_opcao()
        elif escolha == "4":
            excluir_trajes_opcao()
        elif escolha == "5":
            alugar_trajes_opcao()
        elif escolha == "6":
            mostrar_alugueis_usuario_opcao()
        elif escolha == "7":
            excluir_aluguel_opcao()
        elif escolha == "8":
            alterar_senha()
        elif escolha == "9":
            mostrar_dados_usuario()
        elif escolha == "12":
            exportar_jsons()
        elif escolha == "13":
            try:
                os.system("cls")
                zipar_jsons()
                time.sleep(2)
            except Exception as e:
                print("Erro: ", e)
                print("Primeiro exporte os dados para um arquivo JSON!")
                time.sleep(2)
                menu_escolhas()
        elif escolha == "14":
            tela_inicial()
        else:
            print("Opção inválida!")


tela_inicial()
