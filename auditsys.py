import os
from datetime import date
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sgt$GT2023",
    database="AuditSystem"
)
def updateCustomer(id, name, surname):
    mycursor = mydb.cursor()
    mycursor.execute("update UserInformation set FirstName = %s, LastName = %s where PersonID = %s", (name, surname, int(id)))
    mycursor.execute("update AuditLog set VisitedAt = CURRENT_TIMESTAMP where PersonID = %s", (int(id),))
    mydb.commit()
    mycursor.close()
    print("Information updated successfully")


def searchID(id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM UserInformation where PersonID = %s", (int(id),))
    myresult = mycursor.fetchone()
    for x in myresult:
        return x

def saveToDb(id, name, surname):
    mycursor = mydb.cursor()

    sql1 = "INSERT INTO UserInformation (PersonID, FirstName, LastName) VALUES (%s, %s, %s)"
    val1 = (int(id), name, surname)

    sql2 = "INSERT INTO AuditLog (PersonID) VALUES (%s)"
    val2 = (int(id),)
    mycursor.execute(sql1, val1)
    mycursor.execute(sql2, val2)
    mydb.commit()
    mycursor.close()
    print("Information uploaded")

name = input("Type the name here: ")
surname = input("Type the surname here: ")
id = input("Type the ID number here: ")

found = searchID(id)
if found == 1:
    answer = input("Customer exist. Do you want to update? Y/N: ")
    if answer.upper() == "Y":
        updateCustomer(id, name, surname)
    else:
        print("Bye-bye")
        exit()
else:
    saveToDb(id, name, surname)



# currentDate = date.today().strftime("%Y-%m-%d")
# folder = os.path.join(os.getcwd(), currentDate)
# if not os.path.exists(folder):
#     os.makedirs(folder)
# else:
#     print("File located in existing folder", {os.path.join(os.getcwd(), currentDate)})
#
# fileInFolder = os.path.join(folder, f"{id}.txt")
# with open(fileInFolder, "w") as f:
#     f.write(f"{name} {surname}, {id}")
#
# for fileInFolder in os.listdir(folder):
#     with open(os.path.join(folder, fileInFolder), "r") as f:
#         print(f.readlines())


