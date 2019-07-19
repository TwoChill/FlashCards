import random

correct = 0
incorrect = 0
total = correct + incorrect

print('\nPress CTRL + C to quit!\n')
try:
    table = int(input('What table? :> '))
    up_to = int(input('Up to? :> '))
except:
    if KeyboardInterrupt:
        print('Thank you for trying!\n')
        exit()

print(f'\n\n\nRecalling the table of {table}, up to {up_to}.')

while True:
    # Creates a random number between 1 and up_to variable.
    x = random.randint(1, up_to)

    print(f'\n\nWhat is {x} * {table}?')
    sum = x * table

    try:
        answer = int(input(':> '))
    except:
        if KeyboardInterrupt:
            try:
                print('Your grade is a', int(correct * 10 / total), '\n')
                exit()
            except:
                if ZeroDivisionError:
                    exit()

    if answer == sum:
        print('That\'s corect!\n')
        correct += 1
        total += 1
        print('Correct is:', correct)
        print('Total is:', total)

    else:
        print('\nThat\'s not correct!')
        print('Correct answer is', sum)
        print('=' * (18 + (len(str(sum)))))
        incorrect += 1
        total += 1
        print('Incorrect is:', incorrect)
        print('Total is:', total)
