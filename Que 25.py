# Que 25

# Write a program to add a new column email char(30) in Mysql table Users which has the following columns:
# User_id, User_name, User_password

import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "Pra_Exam_Ques")
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE USERS ADD EMAIL CHAR(30)")
mydb.commit()
