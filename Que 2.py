# Que 2

# Write a program to store empid, name and salary of any 5 employees in a file ‘salary.dat’ then increase the salary of an employee by 15% whose empid is 101. After updating a record, print the salary report in a suitable format.

# Save information then increase the salary of one

file = input('Enter file:')
salary_w = open(file, 'w')
salary_r = open(file, 'r')

n = int(input("Enter the no of employee : "))
for i in range(n):
    Empid = int(input("Enter empid : "))
    Name = input("Enter name : ")
    Salary = float(input(("Enter salary : ")))
    salary_w.write(str(Empid) + ":" + Name + ":" + str(Salary) + "\n")

print('{:^83s}'.format('-:Initial Details:-'))
print('-'*70)
print('| {:^20} | {:^20} | {:^20} |'.format("Empid", "Name", "Salary"))
print('-'*70)
salary_w.close()

for i in salary_r.readlines():
    j = i.rstrip("\n").split(":")
    #for k in j:
    #    l = k.split(":")
    #    print("l in k : ", l)
    print('| {:^20} | {:^20} | {:^20} |'.format(j[0], j[1], j[2]))
print('-' * 70)
salary_r.close()

choice_ask = input("Enter y if want to make changes in salary : ")
if choice_ask.lower() == "y":
    number_of_changes = int(input("Enter the changes to be done : "))
    if number_of_changes <= n :
        for i in range(number_of_changes):
             change_id = int(input("Enter the empid : "))
             salary_rw = open(file, 'r+')
             for j in salary_rw.readlines():
                 data = j.rstrip("\n").split(":")
                 print("data : ", data)
                 if change_id == int(data[0]):
                     #print("data[0] : ", int(data[0]))
                     data[2] = str(float(data[2]) + float(data[2])*(15/100))
                     print("data[2] : ", data[2])
                     salary_rw.write(':'.join(data) + "\n")
                     print("Changes done of", change_id, "!!!")
                 else:
                     salary_rw.write(':'.join(data) + "\n")


             salary_rw.close()
    else:
        print("Not enough data !!!")

print('{:^83s}'.format('-:Updated Details:-'))
print('-'*70)
print('| {:^20} | {:^20} | {:^20} |'.format("Empid", "Name", "Salary"))
print('-'*70)
count = 1

salary_r = open(file, 'r')
for i in salary_r.readlines():
    j = i.rstrip("\n").split(":")
    if count > n:
        print('| {:^20} | {:^20} | {:^20} |'.format(j[0], j[1], j[2]))
    count += 1
print('-' * 70)
salary_r.close()
