import random
import sys
import time

name = "Class Word Drills"
question_var = "Question:"
answer_var = "Your answer:"

# Dictonary with questions on the LEFT and the answers to the Right.
dic_quiz = {
    "Tell Python to make a new type of thing.": "class",
    "Two meanings: The most basic type of thing, and any instance of some thing.": "object",
    "What you get when you tell Python to create a class.": "instance",
    "How you define a function inside a class.": "def",
    "Inside the function in a class, ***** is a variable for the instance/object being accessed.": "self",
    "The concept that one class can inherit traits from another class, much like you and your parents.": "inheritance",
    "The concept that a class can be made up of other classes as parts, much like how a car has wheels.": "composition",
    "A property classes have that are from composition an are usually variables.": "attribute",
    "A phrase to say that something inherits from another, as in a 'salmon' is a 'fish'.": "is-a",
    "A phrase to say that something is composed of other things or has a trait.'.": "has-a",

    "Make a class named X that is-a Y": "class X(Y)",
    "Make a class named X that has-a __init__ that takes self and J parameters.": "class X(object): def __init__(self, J)",
    "Make a class named X that has-a function named M that takes self and J parameters.": "class x(object): def M(self, J):",
    "Set foo to a instance of class X": "foo = X()",
    "From foo, get the M function, and call it with parameters self, J.": "foo.M(J)",
    "From foo, get the K attribute, and set it to Q.": "foo.K = Q",

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


def rapport_1dgt():
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


def rapport_2dgt():
    print(f'''
      ===================================
      Boolean Expression Quiz -  Results:
      ===================================
     |       Correct Answerd:    {correct_answerd}      |
     |       Incorrect Answerd:  {incorrect_answerd}      |
     |       Total Questions:    {total_answerd}     |
     |                                  |
     |       Your Grade:         {grade}      |
      ==================================
    ''')
    time.sleep(5)
    exit()


def quit(grade):
    if grade >= 10 or total_answerd >= 10:
        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0
        rapport_2dgt()
    else:
        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0
        rapport_1dgt()


def dic_quiz_reverse(dic_quiz):
    copy = dic_quiz.copy().items()
    dic_quiz.clear()
    for k, v in copy:
        dic_quiz[v] = k
    return dic_quiz


# Checks to see if the questions and answers should be reversed.
if len(sys.argv) == 2 and sys.argv[1] == 'reverse':
    dic_quiz = dic_quiz_reverse(dic_quiz)
    print('1', dic_quiz)  # VALUE

list_value = [v for v in dic_quiz]


randomnr = random.randint(0, len(dic_quiz))

correct_answerd = 0
total_answerd = 0
incorrect_answerd = total_answerd - correct_answerd
grade = 0

# Range values to pass into the function later.
# Users can choose between questions (ranges).
all_questions = 0, 15
class_word_drills = 0, 9
class_phrase_drills = 10, 15

# This block is to prompt user to choose a catagory.
try:
    ranges = int(input(('''
    Which do you want to recall?
    ===========================

     1. All Questions
     2. Class Word Drills
     3. Class Phrase Drills

    :> ''')))

    # This block is used to match the users choice,
    # with the corrospondig dictionary ranges.
    if ranges == 1:
        print("\n\t:> All Questions")
        ranges = all_questions
    elif ranges == 2:
        print("\n\t:> Class Word Drills")
        ranges = class_word_drills
    elif ranges == 3:
        print("\n\t:> Class Phrase Drills")
        ranges = class_phrase_drills
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
        answer = input(f"{answer_var}\t-->\t").lower()
    except KeyboardInterrupt:
        exit()

    if (answer == 'quit') or (answer == 'result'):
        quit(grade)

    elif answer == list_value:
        print("\n\n\t\t\t\tCORRECT!\n\t\t\t\t========")
        correct_answerd += 1
        total_answerd += 1
        previous_randomnr = randomnr

        try:
            grade = int(correct_answerd * 10 / total_answerd)
        except ZeroDivisionError:
            grade = 0

    elif answer != list_value:
        print("\n\n\t\t\t\tINCORRECT!!\n\t\t\t\t===========")
        print(f"\nCorrect answer:\t-->\t\t", dic_quiz.get(question))
        print("\t\t\t\t" + ("=" * len(question)))
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
