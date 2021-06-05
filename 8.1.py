def chop(any_list):
    any_list.pop(-1)
    any_list.pop(0)
    return None


def middle(any_list):
    new_list_with_middle_elements = any_list[1:len(any_list)-1]
    return new_list_with_middle_elements

letters = ['a', 'b', 'c', 'd', 'e', 'f']
chop(letters)
print(letters)
print(middle(letters))
