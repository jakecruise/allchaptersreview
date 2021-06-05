while True:
    file_name = input('Enter the file name: ')
    try:
        if file_name == 'na na boo boo':
            print("NANA BOO BOO TO YOU - You have been punk'd!")
        elif file_name == '':
            break
        else:
            file_handle = open(file_name)
            count = 0
            for line in file_handle:
                if line.startswith("Subject:"):
                    count += 1
            print(f'There were {count} subject lines in mbox.txt')
    except:
        print(f'File cannot be opened: {file_name}')


