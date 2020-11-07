# Que 21

# Write a program to a create Mysql table to store adno,name and fees paid by students in a table fees then read all the record using python function display() to display the data stored in a table.

# Create Mysql table, store and display records.

import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "Pra_Exam_Ques")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Fees(Admno char(8) , Name Varchar(15), Fees_paid integer)")
mycursor.execute("INSERT INTO Fees VALUES('A1','AVI',100),('A2','AYUSH',95),('A3','ADITI',98),('A4','RAVI',85),('A5','RADHA',99)")
mydb.commit()
def display():
    mycursor.execute("select * from Fees")
    myrecords = mycursor.fetchall()
    for x in myrecords:
        print(x)
display()
