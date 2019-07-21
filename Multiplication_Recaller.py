import random

correct = 0
incorrect = 0
total = correct + incorrect

print('=' * 30)
print('Type "quit" to see your grade!')
print('=' * 30)

try:
    # Promts user to choose which table to recall from memory
    table = str(input('\nWhich multiplication table to recall? :> ').lower())

    if table == 'quit':
        raise KeyboardInterrupt
    elif int(table) in range(1, 1001):
        table = int(table)          # Convert the string table into a interger
    elif int(table) not in range(1, 1001):
        print('\nSorry, I won\'t produces numbers higher then 1000, Smarty-Pants.')
        exit(0)
    else:
        print("That's not a number!")
        exit(0)

    # Prompts user to choose up to how many times
    up_to = str(input('Up to how many times? :> ').lower())

    if up_to == 'quit':
        raise KeyboardInterrupt
    elif int(up_to) in range(1, 1001):
        up_to = int(up_to)          # Convert the string up_to into a interger
    elif int(up_to) not in range(1, 1001):
        print('\nSorry, I won\'t produces numbers higher then 1000, Smarty-Pants.')
        exit(0)
    else:
        print("That's not a number!")
        exit(0)

except:
    if KeyboardInterrupt:
        print('\n\nThank you for trying!\n')
        exit(0)


print(f'\n\n\nRecalling the table of {table} up to {up_to} times.')
print('-' * (37 + (len(str(table)) + len(str(up_to)))))     # A highlighter


while True:
    # Creates a random number between 1 and up_to variable.
    x = random.randint(1, up_to)

    print(f'\n\nWhat is {x} * {table}?')
    sum = x * table                         # Calculate the correct answer

    try:
        answer = str(input(':> '))          # Converters answer to a string
        if answer == "":                    # for error handling purposes.
            answer = 0
        elif int(answer) not in range(1, 1001):
            print('That is not a numer')
        answer = int(answer)                # Converts answer to an interger

    except:
        if KeyboardInterrupt:
            try:
                print('\nYour grade is a', int(correct * 10 / total), '/ 10\n')
                print('\n\nThank you for trying!\n')
                exit(0)
            except:
                if ZeroDivisionError:
                    exit(0)

    if answer == sum:
        print('That\'s correct!\n')
        correct += 1
        total += 1

    else:
        print('\nThat\'s not correct!')
        print('Correct answer is', sum)
        print('=' * (18 + (len(str(sum)))))     # Highlights the right anwer
        incorrect += 1
        total += 1
