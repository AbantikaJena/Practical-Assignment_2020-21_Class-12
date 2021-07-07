# Que 20

# Write a program to take a sample of ten phishing e-mails from file ‘email.txt’ and find most commonly occurring word.

# Most commonly occurring word in the text file

def common_word():
    file = input('Enter file:')

    email_rw = open(file, 'r+')
    symbol = ["@", "_", "."]
    for word in email_rw.read().split():
        for i in range(len(symbol)):
            word = word.replace(symbol[i], " ")
            if i == len(symbol) - 1:
                email_rw.write(word + "\n")
    email_rw.close()

    email_r = open(file, "r")
    counts = dict()
    n = 1
    for line in email_r:
        if n > 10:
            words = line.split()
            for word in words:
                word_l = word.lower()
                counts[word_l] = counts.get(word_l, 0) + 1
        n += 1
    email_r.close()
    big_count = None
    big_word = None
    for word, count in list(counts.items()):
        if big_count is None or count > big_count:
            big_word = word
            big_count = count

    print(big_word, " appeared ", big_count, "times.")

common_word()
