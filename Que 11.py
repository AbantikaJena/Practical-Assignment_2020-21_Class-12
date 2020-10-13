# Que 11

# Write a program to create a data file STD.TXT which will store name and phone numbers of 5 students and then ask the user to enter name and print his/her phone number if it is available in the file otherwise display a message “Not found in the directory”

# Find student detail from file

def find():
    file = input('Enter file to save data : ')
    student_w = open(file, 'w')
    n = int(input("Enter the no of student : "))
    for i in range(n):
        Name = input("Enter name : ")
        Mobile = int(input(("Enter phone no : ")))
        if len(str(Mobile)) == 10 and str(Mobile)[0] != "0":
            student_w.write(Name + ":" + str(Mobile) + "\n")
        else:
            print("Invalid Mobile no. !!!")
            quit()
    student_w.close()

    student_r = open(file)
    ask = input("If you want to search for phone no y : ")
    ask_l = []
    if ask.lower() == "y":
        find = input("Enter name : ")
        for i in student_r.readlines():
            k = i.rstrip('\n').split(':')
            if k[0] == find:
                print("Phone no. of ",k[0],"is",k[1])
                ask_l.append(k[1])
        if len(ask_l)==0:
            print("Not found in the directory")
    student_r.close()
    print("Task done!!!")
find()