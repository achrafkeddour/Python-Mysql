import mysql.connector

conn = mysql.connector.connect(
    host = '192.168.1.44',
    user= 'achrafkdr',
    database='firstdb',
    password='pass1'
)

print("connected to database succefully !!!")
