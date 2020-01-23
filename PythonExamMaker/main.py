import base
import traceback
import logging
import time

addQuestion = {}
addAnswers = {}
questionNumber = 0
isTrue = False

# Create instance of class myExam
obj = base.MyExam()
fileHandling = base.FileHandling(True, addQuestion, questionNumber)

base.sys_clear()
# Show how to use and recommendation on how to use properly.
# Like if you create a new exam, try to make it about one topic only (classExam.txt or stringManipulation)

# Create a menu: 1 Create Exam. 2 Delete Exam. 3 Execute Exam. 3
# Check to see if '.txt' file (with previous dictionary) is available.
# If so, ask user to continue with *.txt-file or create a new one.

# Use class methode to add a question to dict: 'addQuestion'

fileHandling.createFolder()

try:

    while True:

        addQuestion[len(
            addQuestion) + 1] = obj.addNew(input('\n\tAdd Exam Question\n\n:> '), input('\n\n\tAdd Exam Answer\n\n:> '))

        # Clears screen
        base.sys_clear()

        print('Question:\t', addQuestion[(
            len(addQuestion))][0], '\nAnswer:\t\t', addQuestion[(len(addQuestion))][1])

        # File handeling
        while True:

            answer = input('\n\tSave Q and A to file? (Y/N) :> ')

            if answer in base.answerYes:
                fileMode = base.FileHandling.foundFile()
                isTrue = True

                if questionNumber == 0:
                    questionNumber += 1

                # Saves questions and answers to string
                # fileMode = base.FileHandling.foundFile()
                fileHandling.saveToFile(
                    isTrue, addQuestion, questionNumber, fileMode)

                try:
                    print("\tExam Question {}:\tSaved!".format(questionNumber))
                except Exception as e:
                    print("Exam Question{}:\tNot Saved!".format(questionNumber))
                    time.sleep(2)
                    logging.error(traceback.format_exc())
                    break

                time.sleep(2)
                break
            elif answer in base.answerNo:
                questionNumber -= 1
                break
            else:
                print("\n\t'" + answer + "' is not a valid input!")
                time.sleep(3)
                continue

        answer = input('\n\nAdd another Q and A? (Y/N) :> ')

        # Variable also used to count the number of question added.
        questionNumber += 1

        if answer in base.answerYes:
            base.sys_clear()
            continue
        elif answer in base.answerNo:
            input('\nPress enter to quit')
            break
        else:
            print("\n\t'" + answer + "' is not a valid input!!!")
            time.sleep(3)
            continue

except Exception as e:
    print('\nAn error has occurred!\n')
    logging.error(traceback.format_exc())
    time.sleep(3)
