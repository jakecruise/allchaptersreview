file_handle = open('mbox-short.txt')

count_emails_from_sender = dict()

for line in file_handle:
    if not line.startswith('From '):
        continue
    else:
        line = line.strip().split()
        email_sender = line[1]
        count_emails_from_sender[email_sender] = count_emails_from_sender.get(email_sender, 0) + 1

print(count_emails_from_sender)

list_of_count_email_tuples = list()
for email, count in count_emails_from_sender.items():
    list_of_count_email_tuples.append((count, email))

print(sorted(list_of_count_email_tuples, reverse=True))  # using sorted() creates a new list
print(list_of_count_email_tuples)
sorted_list = list_of_count_email_tuples.sort(reverse=True)  # returns None for sorted list
print(sorted_list)  # prints None
print(list_of_count_email_tuples)  # prints mutated list (sorted)
