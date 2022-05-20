import mysql.connector

conexao_mysql = mysql.connector.connect(
    host="takedress.cdzwvprld3eb.us-east-1.rds.amazonaws.com",
    user="root",
    port="3306",
    passwd="take-dress2022",
    database="take_dress"
)

cursor = conexao_mysql.cursor()
