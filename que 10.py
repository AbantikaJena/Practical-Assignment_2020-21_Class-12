# Que 10

# Write a program to store few sentences in a file SENT.TXT then count and print number of “to” and “the” present in a file.

# Count the number of times word ocurred

def count_word():
    file = input("Enter the file name : ")
    f = open(file)
    word1 = input("Enter the first word to find : ")
    word2 = input("Enter the second word to find : ")
    c_1,c_2=0,0
    for i in f.read().split():
        if word1 == i:
            c_1 += 1
        if word2 == i:
            c_2 += 1
    print(word1, " occurs ", c_1, " time/s.", "\n",
          word2, " occurs ", c_2, " time/s.")
count_word()