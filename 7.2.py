file_handle = open(input('Enter the file name: '))
count_spam_confidence_num = 0
total_spam_confidence_num = 0

for line in file_handle:
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    else:
        spam_confidence_str = line[line.find(':') + 1:]
        spam_confidence_str = spam_confidence_str.strip()
        spam_confidence_num = float(spam_confidence_str)
        count_spam_confidence_num += 1
        total_spam_confidence_num += spam_confidence_num

print(f"Average spam confidence: {total_spam_confidence_num/count_spam_confidence_num}")
