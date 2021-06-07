file_handle = open('mbox-short.txt')

count_emails_each_hour = dict()

for line in file_handle:
    if not line.startswith('From '):
        continue
    else:
        line = line.strip().split()
        time_of_email = line[5]
        # print(time_of_email)
        hour_of_email = time_of_email[0:2]
        # print(hour_of_email)
        count_emails_each_hour[hour_of_email] = count_emails_each_hour.get(hour_of_email, 0) + 1

# print(count_emails_each_hour)

sorted_email_per_hour = list()
for hour, count in count_emails_each_hour.items():
    # print(hour, count)
    sorted_email_per_hour.append((hour, count))

# print(sorted_email_per_hour)
sorted_email_per_hour.sort()
print(sorted_email_per_hour)
for hour, count in sorted_email_per_hour:
    print(hour, count)
