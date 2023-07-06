import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="attendance",
    password="password",
    database="attendance"
)

query = "select * from Professors"

cursor = cnx.cursor()

cursor.execute(query)
names = cursor.fetchall()

print(names)

cnx.close()