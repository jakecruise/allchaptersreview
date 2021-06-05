numbers_for_analysis = list()

while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        break
    else:
        user_input = int(user_input)
        numbers_for_analysis.append(user_input)

print(f'Maximum: {max(numbers_for_analysis):.1f}')
print(f'Minimum: {min(numbers_for_analysis):.1f}')
