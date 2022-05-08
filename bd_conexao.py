import mysql.connector

conexao_mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="take-dress2022",
    database="take_dress"
)

cursor = conexao_mysql.cursor()
