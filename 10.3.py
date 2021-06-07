import string

file_handle = open('huck_finn.txt')

count_frequency_of_letter = dict()

for line in file_handle:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    for letter in line:
        if not letter.isalpha():
            continue
        else:
            count_frequency_of_letter[letter] = count_frequency_of_letter.get(letter, 0) + 1

print(count_frequency_of_letter)

count_frequency_of_letter_sorted = list()
for letter, count in count_frequency_of_letter.items():
    count_frequency_of_letter_sorted.append((count, letter))

count_frequency_of_letter_sorted.sort(reverse=True)
print(count_frequency_of_letter_sorted)

for count, letter in count_frequency_of_letter_sorted:
    print(count, letter)
