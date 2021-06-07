file_handle = open('mbox.txt')

count_emails_from_sender = dict()

for line in file_handle:
    if not line.startswith('From '):
        continue
    else:
        line = line.strip().split()
        sender_email = line[1]

    if sender_email in count_emails_from_sender:
        count_emails_from_sender[sender_email] += 1
    else:
        count_emails_from_sender[sender_email] = 1

maximum_value = None
most_frequent_sender = None
for key, value in count_emails_from_sender.items():
    if maximum_value is None or value > maximum_value:
        maximum_value = value
        most_frequent_sender = key

print(most_frequent_sender, maximum_value)
