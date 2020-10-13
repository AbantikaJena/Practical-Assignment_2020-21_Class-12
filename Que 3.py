# Que 3

# Take a sample text file “words.txt” which has few words then find the most commonly occurring word in the text file.

# Most commonly occurring word in the text file

def common_word():
    name = input('Enter file:')
    file = open(name, 'r')
    counts = dict()
    for line in file:
        words = line.split()
        for word in words:
            word_l = word.lower()
            counts[word_l] = counts.get(word_l, 0) + 1

    big_count = None
    big_word = None
    for word, count in list(counts.items()):
        if big_count is None or count > big_count:
            big_word = word
            big_count = count

    print(big_word, " appeared ", big_count, "times.")
common_word()
