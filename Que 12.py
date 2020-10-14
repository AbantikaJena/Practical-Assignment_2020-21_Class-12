# Que 12

# Write a program to accept employee’s name and his basic salary of any five employees and store in a file EMP.TXT and print the given output:
#  SALARY REGISTER
# S.No. Name Basic DA HRA Total PF Net-pay

# Accept employee’s name and his basic salary and show other details.

file = input('Enter file : ')
empl_w = open(file, 'w')
n = int(input("Enter the no of employee : "))
for i in range(n):
    Name = input("Enter name : ")
    Salary = float(input("Enter basic salary : "))
    empl_w.write(str(Name + ":" + str(Salary) + "\n"))
empl_w.close()

print('{:^43s}'.format('-:SALARY REGISTER:-'))
print('-' * 185)
print('| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |'
      .format("S.No.", "Name", "Basic", "DA", "HRA", "Total", "PF", "Net_pay"))
print('-' * 185)

SNo = 1
empl_r = open(file, "r")
for i in empl_r.readlines():
    k = i.rstrip('\n').split(':')
    DA = (float(k[1]))*(30/100)
    HRA = (float(k[1]))*(10/100)
    Total = (float(k[1])) + DA + HRA
    PF = ((float(k[1])) + DA) * (10/100)
    Net_pay = Total - PF
    print('| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |'
          .format(SNo, k[0], (float(k[1])), DA, HRA, Total, PF, Net_pay))
    SNo += 1
print('-' * 185)
empl_r.close()
