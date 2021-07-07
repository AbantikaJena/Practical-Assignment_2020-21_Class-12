# Que 5

# Write a program to store name, house and mobile number of any five students using delimiter ‘@’ in a file ‘student.dat’ and create a file ‘student.txt’ and copy all data using delimiter ‘#’.

# Store students details delimiter ‘@’ copy same delimiter ‘#’

def copy_data():
    file = input('Enter file to save data : ')
    student_w = open(file, 'w')
    n = int(input("Enter the no of student : "))
    House_list = ["Chenab", "Ganges", "Jhelum", "Kaveri", "Narmada", "Yamuna"]
    for i in range(n):
        Name = input("Enter name : ")
        House = input("Enter House : ")
        if House in House_list:
            Mobile = int(input(("Enter phone no : ")))
            if len(str(Mobile)) == 10 and str(Mobile)[0] != "0":
                student_w.write(str(Name + "@" + House + "@" + str(Mobile) + "\n"))
            else:
                print("Invalid Mobile no. !!!")
                quit()
        else:
            print("Invalid House. !!!")
            quit()
    student_w.close()

    student_r = open(file)
    file_copy = input('Enter file to copy data : ')
    student_copy = open(file_copy, "w")
    for i in student_r.readlines():
        j = i.rstrip("\n").split("@")
        p = "#".join(j) + "\n"
        student_copy.write(p)
    student_copy.close()
    student_r.close()
    print("Task Done!!!")

copy_data()