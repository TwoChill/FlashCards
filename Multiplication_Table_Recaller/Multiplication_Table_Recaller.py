import random
import time

correct = 0
incorrect = 0
total = correct + incorrect

print('=' * 42)
print('Type "quit" or "result" to see your grade!')
print('=' * 42)


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

    except ValueError:
        print("\nThat's not a number!\n")
        raise KeyboardInterrupt

    # Prompts user to choose up to which vector they want to practice.
    vector = str(input('Up to which vector? :> ').lower())

    try:
        if vector == 'quit' or vector == 'result':
            raise KeyboardInterrupt

        vector = int(vector)

    except ValueError:
        print("\nThat's not a number!\n")
        raise KeyboardInterrupt

except KeyboardInterrupt:
    exit()

if vector == 0 or table == 0:
    exit()

text = (f'\n\n\nRecalling the table of {table} with a vector of {vector}')
print(text)
print('=' * (len(text) - 3))     # A highlighter.


while True:
    # x Creates a random number between 1 and the num in the 'vector' variable.
    # xx Creates a random number to switch the questions.
    x = random.randint(1, vector)
    xx = random.randint(1, 3)

    if xx == 1:
        print(f'\n\nWhat is {x} * {table}?')
    else:   # Nr.1 seems more dominant. xx gives this line more chances.
        print(f'\n\nWhat is {table} * {x}?')

    sum = x * table                         # Calculate the correct answer.

    try:
        try:
            answer = str(input(':> '))

            if answer == 'quit' or answer == 'result':
                raise KeyboardInterrupt
            elif answer == "":
                answer = 0

            # Converters answer back to a integer
            answer = int(answer)

        except ValueError:                      # If a string in answer..
            answer = 0                          # .. converters to incorrect integer

    except KeyboardInterrupt:
        try:
            print('\nYour grade is a', int(correct * 10 / total), '/ 10\n')
            # Makes the highlights the same charachter length as the string above.
            if int(correct * 10 / total) == 10:
                print('=' * 23)
            else:
                print('=' * 22)

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
