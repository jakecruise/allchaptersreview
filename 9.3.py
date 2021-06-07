file_handle = open('mbox-short.txt')

count_of_emails_from_sender = dict()

for line in file_handle:
    if not line.startswith('From '):
        continue
    else:
        line = line.strip()
        line = line.split()
        email_sender = line[1]
        print(email_sender)
        if count_of_emails_from_sender.get(email_sender) is None:
            count_of_emails_from_sender[email_sender] = 1
        else:
            count_of_emails_from_sender[email_sender] = count_of_emails_from_sender.get(email_sender) + 1

print(count_of_emails_from_sender)
