from pathlib import Path
import base
import time
import traceback
import logging
from os import listdir
from os.path import isfile, join
# scriptName = base.getScriptInfo(Path(__file__))[3]


addQuestion = {}
addAnswers = {}


# Clears screen
base.sys_clear()

# Create instance of class myExam
obj = base.MyExam()

try:
    # create Main Folder
    base.FileHandling.createExam()

    # create Exam File

    questionNumber = 0

    while True:

        addQuestion[len(addQuestion) + 1] = obj.addNew(
            input('\n\tAdd Exam Question\n\n:> '), input('\n\n\tAdd Exam Answer\n\n:> '))

        # Clears screen
        base.sys_clear()

        print('Question:\t', addQuestion[(
            len(addQuestion))][0], '\nAnswer:\t\t', addQuestion[(len(addQuestion))][1])

        while True:

            answer = input('\n\tSave Q and A to file? (Y/N) :> ')

            if answer in base.answerYes:

                if questionNumber == 0:
                    questionNumber += 1
                    base.FileHandling.saveToFile(
                        True, addQuestion, questionNumber, 'w+')
                else:
                    base.FileHandling.saveToFile(
                        True, addQuestion, questionNumber, 'a+')

                try:
                    print("\tExam Question {}:\tSaved!".format(questionNumber))
                except Exception as e:
                    print("Exam Question{}:\tNot Saved!".format(questionNumber))
                    time.sleep(2)
                    logging.error(traceback.format_exc())

                time.sleep(2)
                break
            elif answer in base.answerNo:
                questionNumber -= 1
                break
            else:
                print("\n\t'" + answer + "' is not a valid input!")
                time.sleep(3)
                continue

        answer = input('\nAdd another Q and A? (Y/N) :> ')

        # Variable also used to count the number of question added.
        questionNumber += 1

        if answer in base.answerYes:
            base.sys_clear()
            continue
        elif answer in base.answerNo:
            input('\nPress enter to quit')
            break
        else:
            print("\n\t'" + answer + "' is not a valid input!")
            time.sleep(3)
            continue

except Exception as e:
    print('\nAn error has occurred!\n')
    logging.error(traceback.format_exc())
    time.sleep(3)
