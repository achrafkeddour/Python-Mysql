#first we connect to db
#2 create a cursor  cursor = conn.cursor()
#3 execute commands (select data) 'cursor.execute(sql_query)'
#4 bring data to the server 'result = cursor.fetchall()'


import mysql.connector

conn = mysql.connector.connect(
    host = '192.168.1.44',
    database = 'firstdb',
    user = 'achrafkdr',
    password = 'pass1'
)
print("connected succefully to database")

cursor = conn.cursor() #This cursor object is used to execute SQL queries.

sql_query1 = 'select * from students;' 

cursor.execute(sql_query1) # Execute the query (selecting what we want)

result = cursor.fetchall()  #fetching all result from database (bring result into python)

for row in result:
    print(row)

print("--------------------------------------------------------------------")


sql_query2 = "select * from students;"
cursor.execute(sql_query2)
result2 = cursor.fetchmany(2) #two rows
for row in result2:
    print(row)



cursor.fetchall() #lazem tkoun haka (fetchall) bach n9dr ndir close 
cursor.close()
conn.close()
