import mysql.connector
import time


def conexao_mysql():
    try:
        conexao_mysql = mysql.connector.connect(
            host="takedress.cdzwvprld3eb.us-east-1.rds.amazonaws.com",
            user="root",
            port="3306",
            passwd="take-dress2022",
            database="take_dress"
        )
        return conexao_mysql
    except:

        print("Erro ao conectar com o banco de dados, verifique sua internet")
        time.sleep(3)
        exit()
