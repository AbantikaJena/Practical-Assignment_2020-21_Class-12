# Que 23

# Write a program to insert a new record in sql table employee using function Data_entry(). Assume table has the following columns:
# Empid, emp_name, emp_post, emp_mobile

import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "Pra_Exam_Ques")
mycursor = mydb.cursor()
n = int(input("Enter no of enteries : "))
def Data_entry(insert):
    mycursor.execute(insert)
for i in range(n):
    Empid = input("Enter Empid : ")
    emp_name = input("Enter emp_name : ")
    emp_post = input("Enter emp_post : ")
    emp_mobile = input("Enter emp_mobile : ")
    insert = "INSERT INTO EMPLOYEE VALUES('" + Empid + "','" + emp_name + "','" + emp_post + "','" + emp_mobile + "')"
    Data_entry(insert)
    print("Data Entered!")
mydb.commit()
print("Task done!!")
