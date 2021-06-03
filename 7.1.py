file_handle = open('mbox-short.txt', 'r')
file_contents = file_handle.read()

contents_in_capital_letters = file_contents.upper()
print(contents_in_capital_letters)