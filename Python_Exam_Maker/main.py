from pathlib import Path
import os
import base as base
import time

import traceback
import logging

scriptName = base.getScriptName()

addQuestion = {}
addAnswers = {}

# Clears screen
base.sys_clear()

# Create instance of class myExam
obj = base.myExam()

# Show how to use and recommendation on how to use properly.
# Like if you create a new exam, try to make it about one topic only (classExam.txt or stringManipulation)

# Create a menu: 1 Create Exam. 2 Delete Exam. 3 Execute Exam. 3
# Check to see if '.txt' file (with previous dictionary) is available.
# If so, ask user to continue with *.txt-file or create a new one.

# Use class methode to add a question to dict: 'addQuestion'
try:
    while True:
        addQuestion[len(
            addQuestion) + 1] = obj.addNew(input('\n\tAdd Exam Question\n\n:> '), input('\n\n\tAdd Exam Answer\n\n:> '))

        base.sys_clear()

        print('Question:\t', addQuestion[(
            len(addQuestion))][0], '\nAnswer:\t\t', addQuestion[(len(addQuestion))][1])

        answer = input('\n\n\tAdd another? (Y/N) :> ').capitalize()

        if answer in ('Y', 'y', 'YES', 'YEs', 'Yes', 'yEs', 'yeS', 'yes'):
            base.sys_clear()
            continue
        elif answer in ('N', 'NO', 'n', 'No', 'nO'):
            input('\nPress enter to quit')
            break
        else:
            print("\t'" + answer + "' is not a valid input!")
            time.sleep(3)
            base.sys_clear()
            continue

except Exception as e:
    print('\nAn error has occurred!\n')
    logging.error(traceback.format_exc())
    time.sleep(3)
