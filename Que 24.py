# Que 24

# Write a function Delete_record() to remove the record from Mysql table lib which has the following structure:
# Accno, Bookname, Publisher, Price
# (To delete a record, Accno will be entered by the user)

import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "Pra_Exam_Ques")
mycursor = mydb.cursor()
n = int(input("Enter no of enteries delete : "))
def Delete_record(insert):
    mycursor.execute(insert)
for i in range(n):
    Accno = input("Enter Accno : ")
    insert = "DELETE FROM LIB WHERE  Accno = '" + Accno + "'"
    Delete_record(insert)
    print("Data Deleted!")
mydb.commit()
print("Task done!!")
