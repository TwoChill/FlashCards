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

    if table == 'quit' or table == 'result':
        raise KeyboardInterrupt
    elif int(table) in range(1, 1001):
        table = int(table)          # Convert the string table into a interger
    elif int(table) not in range(1, 1001):
        print('\nSorry, I won\'t produces numbers higher then 1000, Smarty-Pants.')
        exit(0)
    else:
        print("That's not a number!")
        exit(0)

    # Prompts user to choose up to which vector they want to practice.
    vector = str(input('Up to which vector? :> ').lower())

    if vector == 'quit' or vector == 'result':
        raise KeyboardInterrupt
    elif int(vector) in range(1, 1001):
        vector = int(vector)     # Convert the string 'vector' into a interger.
    elif int(vector) not in range(1, 1001):
        print('\nSorry, I won\'t produces numbers higher then 1000, Smarty-Pants.')
        exit(0)
    else:
        print("That's not a number!")
        exit(0)

except KeyboardInterrupt:
    print('\n\nThank you for trying!\n')
    exit(0)


text = (f'\n\n\nRecalling the table of {table} with a vector of {vector}.')
print(text)
print('-' * len(text))     # A highlighter.


while True:
    # x Creates a random number between 1 and the num in the 'vector' variable.
    # xx Creates a random number to switch the questions.
    x = random.randint(1, vector)
    xx = random.randint(1, 3)
    if xx == 1:
        print(f'\n\nWhat is {x} * {table}?')
    else:   # 1 seems more dominant. xx gives this line more chances.
        print(f'\n\nWhat is {table} * {x}?')

    sum = x * table                         # Calculate the correct answer.

    try:
        answer = str(input(':> '))          # Converters answer to a string
        if answer == "":                    # for error handling purposes.
            answer = 0
        elif int(answer) not in range(1, 1001):
            print('That is not a numer')
        answer = int(answer)                # Converts answer to an interger.

    except KeyboardInterrupt:
        try:
            print('\nYour grade is a', int(correct * 10 / total), '/ 10\n')
            print('\n\nThank you for trying!\n')
            exit(0)
        except ZeroDivisionError:
            exit(0)

    if answer == sum:
        print('\nThat\'s correct!')
        print('=' * 15)                         # Highlights the right anwer.
        correct += 1
        total += 1

    else:
        print('\nThat\'s not correct!')
        print('Correct answer is', sum)
        print('=' * (18 + (len(str(sum)))))     # Highlights the right anwer.
        incorrect += 1
        total += 1
