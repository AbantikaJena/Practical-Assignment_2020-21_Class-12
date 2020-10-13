# que 18

# Write a program to read a text file ‘english.txt’ and display the number of vowels / consonants /uppercase/ lowercase characters available in the file

# Display the number of vowels / consonants /uppercase/ lowercase characters.

def characters()
    file = input('Enter file:')
    search_file = open(file, 'r')
    vowel_list = ["a", "e", "i", "o", "u"]
    lowercase, uppercase, vowel, consonant = 0, 0, 0, 0
    for i in search_file.readlines():
        for j in range(len(i)):
            if i[j].islower():
                lowercase += 1
            if i[j].isupper():
                uppercase += 1
            if i[j].isalpha():
                if i[j].lower() in vowel_list:
                    vowel += 1
                else:
                    consonant += 1
    
    print("No of Vowels : ", vowel, "\n",
          "No of consonents : ", consonant, "\n",
          "No of lowercases : ", lowercase, "\n",
          "No of uppercases : ", uppercase)
characters()
