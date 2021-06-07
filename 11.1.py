import re

file_handle = open('mbox.txt')

regex_input = input('Enter a regular expression: ')

count = 0
for line in file_handle:
    if not re.search(regex_input, line):
        continue
    else:
        count += 1

print(f'mbox.txt has {count} lines that matched {regex_input}')

