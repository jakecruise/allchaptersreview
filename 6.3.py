def letter_counter(string, slice):
    count = 0
    for letter in string:
        if letter == slice:
            count += 1
    return count


print(letter_counter('banana', 'a'))

