file_handle = open('mbox.txt')
email_count_per_day = dict()

for line in file_handle:
    line = line.strip()
    if not line.startswith('From '):
        continue
    else:
        line_in_list = line.split()
        # print(line_in_list)
        if line_in_list[2] not in email_count_per_day:
            email_count_per_day[line_in_list[2]] = 1
        else:
            email_count_per_day[line_in_list[2]] += 1

print(email_count_per_day)
