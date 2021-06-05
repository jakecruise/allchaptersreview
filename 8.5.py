file_handle = open('mbox-short.txt')
count = 0

for line in file_handle:
    line = line.strip()
    if not line.startswith('From '):
        continue
    end_of_email = line.find(' ', 5) + 1
    print(line[5:end_of_email])
    count += 1

print(f'There were {count} lines in the file with From as the first word')