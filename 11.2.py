import re

file_handle = open('mbox.txt')

sum_of_rev_nums = 0
count = 0
for line in file_handle:
    if not re.search('^New Revision: [0-9]+', line):
        continue
    else:
        value = re.findall('^New Revision: ([0-9]+)', line)
        # print(value)
        sum_of_rev_nums += int(value[0])
        count += 1

print(sum_of_rev_nums / count)
