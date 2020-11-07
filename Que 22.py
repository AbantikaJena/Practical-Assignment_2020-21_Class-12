# Que 22

# Write a program to create Mysql table to store mobile model and price of any five mobiles and then using function update_data() update the price of mobile by 10% for all mobiles and display all updated records.

# Create Mysql table, store, update and display records.

import mysql.connector
mydb= mysql.connector.connect(host ="localhost",user="root",passwd="Mars 1507",database= "Pra_Exam_Ques")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Que22(Model char(8) , Price integer)")
mycursor.execute("INSERT INTO Que22 VALUES('A1',1000),('A2',2000),('A3',3000),('A4',4000),('A5',5000)")
def update_data():
    mycursor.execute("UPDATE Que22 SET Price = Price + Price*(10/100)")
update_data()
mydb.commit()
mycursor.execute("select * from Que22")
myrecords = mycursor.fetchall()
for x in myrecords:
    print(x)




