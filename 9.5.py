file_handle = open('mbox-short.txt')

count_of_sender_domains = dict()

for line in file_handle:
    if not line.startswith('From '):
        continue
    else:
        line = line.strip().split()
        email_sender = line[1]
        user_name_and_domain = email_sender.split('@')
        domain = user_name_and_domain[1]
        if domain in count_of_sender_domains:
            count_of_sender_domains[domain] += 1
        else:
            count_of_sender_domains[domain] = 1

print(count_of_sender_domains)
