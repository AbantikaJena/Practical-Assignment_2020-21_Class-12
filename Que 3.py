# Que 3

# Take a sample text file “words.txt” which has few words then find the most commonly occurring word in the text file.

# Most commonly occurring word in the text file

name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, " appeared ", bigcount, "times.")