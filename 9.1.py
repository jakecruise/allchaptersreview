file_handle = open('words.txt')
words_dictionary = dict()

for line in file_handle:
    words = line.strip().split()
    for word in words:
        words_dictionary[word] = "doesn't matter"
print('programs' in words_dictionary)
