total = 0
count = 0
average = 0
max = None
min = None

while True:
    value_entered = input("Enter a number: ")
    if value_entered == 'done':
        break

    try:
        value_entered = int(value_entered)
        total += value_entered
        count += 1
        if min is None or value_entered < min:
            min = value_entered
        if max is None or value_entered > max:
            max = value_entered
    except:
        print("Invalid input")

print('Total:', total)
print('Count:', count)
print('Average:', float(total/count))
print('Maximum number entered:', max)
print('Minimum number entered:', min)

