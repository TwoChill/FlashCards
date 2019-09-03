import random
import time

name = "Boolean Expression Quiz"
question_var = "Question:"
answer_var = "Evaluates to?:"

# Dictonary with questions on the LEFT and the answers to the Right.
dic_quiz = {
    "not False": "True",
    "not True": "False",

    "True or False": "True",
    "True or True": "True",
    "False or True": "True",
    "False or False": "False",

    "True and False": "False",
    "True and True": "True",
    "False and True": "False",
    "False and False": "False",

    "not(True or False)": "False",
    "not(True or True)": "False",
    "not(False or True)": "False",
    "not(False or False)": "True",

    "not(True and False)": "True",
    "not(True and True)": "False",
    "not(False and True)": "True",
    "not(False and False)": "True",

    "1 != 0": "True",
    "1 != 1": "False",
    "0 != 1": "True",
    "0 != 0": "False",

    "1 == 0": "False",
    "1 == 1": "True",
    "0 == 1": "False",
    "0 == 0": "True",
}

print("\n")
print("=" * len(name), f"\n{name}")
print("=" * len(name))


def range_a(string):
    a = string[0]
    return a


def range_b(string):
    b = string[1]
    return b


def rapport():
    print(f'''
      ==================================
      Boolean Expression Quiz -  Results:
      ==================================
     |       Correct Answerd:    {correct_answerd}      |
     |       Incorrect Answerd:  {incorrect_answerd}      |
     |       Total Questions:    {total_answerd}      |
     |                                  |
     |       Your Grade:         {grade}      |
      ==================================
    ''')
    time.sleep(5)
    exit()


def perfect_grade():
    print(f'''
      ===================================
      Boolean Expression Quiz -  Results:
      ===================================
     |       Correct Answerd:    {correct_answerd}      |
     |       Incorrect Answerd:  {incorrect_answerd}      |
     |       Total Questions:    {total_answerd}      |
     |                                  |
     |       Your Grade:         {grade}!    |
      ==================================
    ''')
    time.sleep(5)
    exit()


def quit(grade):
    if ((correct_answerd > 10) or (incorrect_answerd > 10)) or (total_answerd > 10):
        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0
        perfect_grade()
    else:
        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0
        rapport()


randomnr = random.randint(0, len(dic_quiz))

correct_answerd = 0
total_answerd = 0
incorrect_answerd = total_answerd - correct_answerd
grade = 0

# Source: quora.com/# How-do-I-convert-a-dictionary-to-a-list-in-Python
list_value = [v for v in dic_quiz]

# Range values to pass into the function later.
# Users can choose between questions (ranges).
all_questions = 2, 25
_or_ = 2, 5
_and_ = 6, 9
or_and = 2, 9
not_or = 10, 13
not_and = 14, 17
not_or_not_and = 10, 17
not_equal = 18, 21
equal_to = 22, 25
not_equal_and_equal_to = 18, 25

# This block is to prompt user to choose a catagory.
try:
    ranges = int(input(('''
    Which do you want to recall?
    ===========================

     1. All Questions
     2. Or
     3. And
     4. Or & And
     5. Not(_or_)
     6. Not (_and_)
     7. Not(_or_) & Not (_and_)
     8. Not Equal (!=)
     9. Equal To (==)
    10. Not Equal (!=) & Equal To (==)

    :> ''')))

    # This block is used to match the users choice,
    # with the corrospondig dictionary ranges.
    if ranges == 1:
        print("\n\t:> All Questions")
        ranges = all_questions
    elif ranges == 2:
        print("\n\t:> Or")
        ranges = _or_
    elif ranges == 3:
        print("\n\t:> Or & And")
        ranges = _and_
    elif ranges == 4:
        print("\n\t:> Or & And")
        ranges = or_and
    elif ranges == 5:
        print("\n\t:> Not(_or_)")
        ranges = not_or
    elif ranges == 6:
        print("\n\t:> Not (_and_)")
        ranges = not_and
    elif ranges == 7:
        print("\n\t:> Not(_or_) & Not (_and_)")
        ranges = not_or_not_and
    elif ranges == 8:
        print("\n\t:> Not Equal (!=)")
        ranges = not_equal
    elif ranges == 9:
        print("\n\t:> Equal To (==)")
        ranges = equal_to
    elif ranges == 10:
        print("\n\t:> Not Equal (!=) & Equal To (==)")
        ranges = not_equal_and_equal_to
    else:
        print("\n\t:> All Questions")
        ranges = all_questions
except:
    if ValueError:
        print("\n\t:> All Questions")
        ranges = all_questions
    else:
        time.sleep(5)
        exit()


print("\n")
print("=" * 32)
print("Type 'quit' or 'result' to exit!")
print("=" * 32)

while True:
    # reminder_count is used to skip the 'remember to type quit' print function twice.
    previous_randomnr = randomnr
    reminder_count = 0

    # Random number generated which correlates to a random question being asked.
    randomnr = random.randint(range_a(ranges), range_b(ranges))

    # This will prevent the program from asking the 'remember to type quit' sentence twice in a row.
    if (previous_randomnr == randomnr) and (reminder_count == 1):
        reminder_count == 0
        continue
    elif previous_randomnr == randomnr:
        print("Type 'quit' or 'result' to exit!")
        reminder_count += 1
        continue

    # Gets a random question(key) from the dic_quiz.
    question = list_value[randomnr]

    print(f"\n\n{question_var}\t-->\t{question}")
    try:
        # Asks the user for an answer(input)
        answer = input(f"{answer_var}\t-->\t").capitalize()
    except KeyboardInterrupt:
        exit()

    if (answer == 'Quit') or (answer == 'Result'):
        quit(grade)
    elif answer == dic_quiz.get(question).lower():
        print("\n\n\t\t\t\tCORRECT!\n\t\t\t\t========")
        correct_answerd += 1
        total_answerd += 1
        previous_randomnr = randomnr

        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0

    elif answer != dic_quiz.get(question).lower():
        print("\n\n\t\t\t\tINCORRECT!!\n\t\t\t\t===========")
        print("\nCorrect answer:\t-->\t\t" + dic_quiz.get(question).upper())
        print("\t\t\t\t" + ("=" * len(dic_quiz.get(question))))
        total_answerd += 1
        previous_randomnr = randomnr

        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0
    else:
        previous_randomnr = randomnr

        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0

        continue
