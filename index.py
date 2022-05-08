from bd_usuario import *
from bd_trajes import *
from bd_aluguel import *
from export_json import *
import time
import os
from getpass import getpass


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


def mostra_trajes():
    os.system("cls")
    print("-------------------- TRAJES --------------------")
    mostrar_trajes()
    input("Digite qualquer tecla para voltar: ")
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
    usuario = input("Digite seu usuário: ")
    if verificar_usuario_cadastrado(usuario):
        print("Usuário já cadastrado!")
        tentar = input("Deseja tentar novamente? (S/N): ")
        if tentar == "S":
            cadastrar()
        else:
            tela_inicial()
    else:
        senha = getpass("Digite sua senha: ")
        while senha_segura(senha) == False:
            senha = getpass("Digite sua senha: ")

        cadastro(usuario, senha)
        time.sleep(3)
        tela_inicial()


def login():
    os.system("cls")
    print("-------------------- LOGIN --------------------")
    usuario = input("Digite seu usuário: ")
    senha = getpass("Digite sua senha: ")

    if verificar_usuario(usuario, senha):
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
    usuario = input("Digite seu usuário: ")
    if verificar_usuario_cadastrado(usuario):
        mostrar_usuario_logado(usuario)
        controle = input("Digite qualquer tecla para voltar: ")
        menu_escolhas()
    else:
        print("Usuário não cadastrado!")
        tentar = input("Deseja tentar novamente? (S/N): ")
        if tentar == "S":
            mostrar_dados_usuario()


def menu():
    os.system("cls")
    print("-------------------- TAKE DRESS --------------------")
    print("1 - Cadastrar trajes")
    print("2 - Listar trajes")
    print("3 - Excluir trajes")
    print("4 - Alugar trajes")
    print("5 - Excluir aluguel")
    print("6 - Listar alugueis")
    print("7 - Alterar aluguel")
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
            mostra_trajes()
        elif escolha == "3":
            excluir_trajes()
        elif escolha == "4":
            alugar_trajes()
        elif escolha == "5":
            excluir_aluguel()
        elif escolha == "6":
            listar_alugueis()
        elif escolha == "7":
            alterar_aluguel()
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
