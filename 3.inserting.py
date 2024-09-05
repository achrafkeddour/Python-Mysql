import mysql.connector

conn = mysql.connector.connect(
    host = '192.168.1.44',
    database = 'firstdb',
    user = 'achrafkdr',
    password = 'pass1'
)
print("connected to database ! ")

cursor = conn.cursor() #create cursor to execute commands (create , execute , fetch )

sqlquery = "select name,AGE from students;"
cursor.execute(sqlquery) #execute

result = cursor.fetchall() #fetching result

print("table before inserting : ")
for row in result:
    print(row)
print()


#inserting
sqlinsert = "insert into students(name,familly,AGE,password) VALUES (%s,'infamilly',10,%s);"
data = ("nuser", "neword")

cursor.execute(sqlinsert,data)
print('data inserted !!\n')

conn.commit() #save changes
print(f"{cursor.rowcount} row(s) affected.")


readagain = "select * from students;"
cursor.execute(readagain)
new_table = cursor.fetchall()

print()
print("new table : ")
for row in new_table:
    print(row)
