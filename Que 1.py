# Que 1
# Write a program that copies a text file “source.txt” onto “target.txt” barring the lines starting with a ‘@’ sign.

# Copies text file barring lines starting with “@”

def barring_lines():
    source = input("Enter source file name : ")
    f1 = open(source)
    target = input("Enter target file name : ")
    f2 = open(target, "w")
    for i in f1.readlines():
        if i[0] != "@":
            f2.writelines(i)
    f2.close()
    f1.close()
    print("Task Done!!!")
barring_lines()
