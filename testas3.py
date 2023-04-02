import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sgt$GT2023",
    database="sgt2023"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT count(*) FROM Customer")

myresult = mycursor.fetchone()

for x in myresult:
    print(x)


