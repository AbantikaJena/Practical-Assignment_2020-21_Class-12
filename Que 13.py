# Que 13

# Write a program to accept name, amount collected from student and house(e.g. Chenab, Ganges…..) of any 5 students, store in file STUDENT.txt then print the given output of the given house Name of the student House Amount Collected.

# Student details show in tabular form

def Amount_Collected():
    file = input('Enter file:')
    student_w = open(file, 'w')
    House_list = ["Chenab", "Ganges", "Jhelum", "Kaveri", "Narmada", "Yamuna"]

    n = int(input("Enter the no of student : "))
    for i in range(n):
        Name = input("Enter name : ")
        House = input("Enter House : ")
        if House in House_list:
            Amount = float(input(("Enter amount paid : ")))
            student_w.write(str(Name + ":" + House + ":" + str(Amount) + "\n"))
        else:
            print("Invalid House. !!!")
            quit()
    student_w.close()

    print('{:^83s}'.format('-:Students\' Details:-'))
    print('-'*70)
    print('| {:^20} | {:^20} | {:^20} |'.format("Name of student", "House", "Amount Collected"))
    print('-'*70)

    student_r = open(file)
    for i in student_r.readlines():
        j = i.rstrip("\n").split(":")
        print('| {:^20} | {:^20} | {:^20} |'.format(j[0], j[1], j[2]))
    print('-' * 70)
    student_r.close()

Amount_Collected()