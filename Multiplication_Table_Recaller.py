import random
import time

correct = 0
incorrect = 0
total = correct + incorrect

print('=' * 30)
print('Type "quit" to see your grade!')
print('=' * 30)


def exit():
    print('\n\nThank you for trying!')
    time.sleep(3)
    quit()


# DRY.. Make table and vector into one function which you use twice.
try:
    # Promts user to choose which table to recall from memory
    table = input('\nWhich multiplication table to recall? :> '.lower())

    try:
        if table == 'quit' or table == 'result':
            raise KeyboardInterrupt

        table = int(table)

        if table in range(0, 1001):
            # Convert the string table into a interger
            table = int(table)
        elif int(table) not in range(0, 1001):
            print('\nSorry, I won\'t produces numbers higher then 1000, Smarty-Pants.')
            exit()
    except ValueError:
        print("\nThat's not a number!\n")
        raise KeyboardInterrupt

    # Prompts user to choose up to which vector they want to practice.
    vector = str(input('Up to which vector? :> ').lower())

    try:
        if vector == 'quit' or vector == 'result':
            raise KeyboardInterrupt

        vector = int(vector)

        if vector in range(0, 1001):
            # Convert the string vector into a interger
            vector = int(vector)
        elif int(vector) not in range(0, 1001):
            print('\nSorry, I won\'t produces numbers higher then 1000, Smarty-Pants.')
    except ValueError:
        print("\nThat's not a number!\n")
        raise KeyboardInterrupt

except KeyboardInterrupt:
    exit()

if vector == 0 or table == 0:
    exit()

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
        try:
            answer = str(input(':> '))          # Converters answer to a string

            if answer == 'quit' or answer == 'result':
                raise KeyboardInterrupt
            elif answer == "":                    # for error handling purposes.
                answer = 0

            answer = int(answer)                # Converters answer back to a integer

            if int(answer) not in range(0, 1001):
                print(
                    '\nSorry, I won\'t produces numbers higher then 1000, Smarty-Pants.')
        except ValueError:
            answer = 0

    except KeyboardInterrupt:
        try:
            print('\nYour grade is a', int(correct * 10 / total), '/ 10\n')
            exit()
        except ZeroDivisionError:
            exit()

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
