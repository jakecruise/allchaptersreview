file_handle = open('romeo.txt')
list_of_words = list()
for line in file_handle:
    words = line.split()
    for word in words:
        if word in list_of_words:
            continue
        else:
            list_of_words.append(word)
    list_of_words.sort()
print(list_of_words)
