from pathlib import Path
import platform
import os
from os import listdir
from os.path import isfile, join
import main

import random
import time

# Questions and Answers are stored with this type of file extention.
fileExtention = '.txt'
newDirName = ''
newFolderName = ''


class MyExam(object):
    ''' To create own exam'''

    def __init__(self):
        self.question = ''
        self.answer = ''

    def addNew(self, newQuestion=None, newAnswer=None):
        ''' Add a new Question and an Answer'''

        if newQuestion is None:
            newQuestion = []
        elif newQuestion is not None:
            self.question = newQuestion

        if newAnswer is None:
            newAnswer = []
        elif newAnswer is not None:
            self.answer = newAnswer

        return [self.question, self.answer]

    def randomQuestion(self, question):
        ''' Randomize questions '''

        randomNr = random.randint(1, len(question))
        print('This is random nr: ', randomNr)

        return self.question[randomNr], randomNr


def getScriptInfo(pathFileName):
    ''' Return scriptfile information'''

    filePath = str(pathFileName.absolute())
    fileExt = filePath[len(filePath) - 3:]
    directoryPath = str(os.path.dirname(os.path.abspath(__file__)))
    scriptName = filePath[(len(directoryPath) + 1):-len(fileExtention)]
    parentPath = os.path.abspath(os.path.join(directoryPath, os.pardir))
    parentPath2 = os.path.abspath(os.path.join(parentPath, os.pardir))
    parentName = parentPath[(len(parentPath2) + 1):]
    directoryPathName = directoryPath[(len(parentPath) + 1):]
    examFolder = directoryPath + '/' + os.listdir(directoryPath)[-1]

    return [fileExt, scriptName, filePath, directoryPath, directoryPathName, parentPath, parentName, parentPath2, examFolder]


class FileHandling(object):
    ''' Everything to do with files '''

    def __init__(self, isTrue, addQuestion, questionNumber):
        self.isTrue = isTrue
        self.addQuestion = addQuestion
        self.questionNumber = questionNumber

    def saveToFile(self, isTrue, addQuestion, questionNumber, fileMode):
        ''' To save Q and A to a file '''

        if isTrue is True:
            fileMode = ''

            # if questionNumber == 0:
            #     questionNumber += 1
            #     fileMode = 'w'
            # else:
            #     fileMode = 'a+'

            examDir = + '/'
            # Check if there are no whitespaces in filePath.
            self.replaceWhiteSpace(getScriptInfo(Path(__file__))[2], '_')

            with open(f"{}{fileExtention}", fileMode, encoding="utf-8") as f:
                strToFile = "{}\tQuestion:\t{}\n\tAnswer:\t\t{}\n\n".format(
                    questionNumber, addQuestion[questionNumber][0], addQuestion[questionNumber][1])

                f.write(strToFile)

    def createExamDir(self):
        ''' Creates a new directory to save ExamFiles.fileExtention'''
        dirName = ''
        folderName = ''

        try:
            # Makes sure we are in the directory of this script.
            os.chdir(f'{getScriptInfo(Path(__file__))[3]}')

            # If a file allready exist raise error
            if getScriptInfo(Path(__file__))[6] == getScriptInfo(Path(__file__))[6]:
                raise FileExistsError
            else:
                while True:
                    answer = input(
                        'Create a new folder for your Exam File? (Y/N) :> ')
                    if answer in main.answerYes:
                        while True:
                            dirName = input(
                                'What\'s the name of the folder? :> ')
                            answer = input(f"Is '{dirName}' correct?")
                            if answer == main.answerYes:
                                os.mkdir(f'{dirName}')
                                break
                            elif answer == main.answerNo:
                                print('GOT IT')
                                continue
                            else:
                                print(
                                    '\nThat\'s not a valid input. Try again please!2')
                                time.sleep(3)
                                continue
                    elif answer in main.answerNo:
                        while True:
                            folderName = input(
                                'What\'s the name of you exam file? :> ')
                            answer = input(f"Is '{folderName}' correct?")
                            if answer == main.answerYes:
                                if dirName != '':
                                    os.mkdir(f'{dirName}/{folderName}')
                                else:
                                    os.mkdir(f'{folderName}')
                                break
                            elif answer == main.answerNo:
                                print('YES2')
                                continue
                            else:
                                print(
                                    '\nThat\'s not a valid input. Try again please!3')
                                time.sleep(3)
                                continue
                    else:
                        print(
                            '\nThat\'s not a valid input. Try again please!4')
                        time.sleep(3)
                        continue

            if dirName != '':
                return dirName + "/" + folderName
            else:
                return folderName

        except FileExistsError:
            pass

    @staticmethod
    def foundFile():
        ''' Checks for ExamFiles '''

        # Lists all the files in the directory of this script with a certain !fileExtention!
        onlyFiles = [f for f in listdir(getScriptInfo(Path(__file__))[8]) if isfile(
            join(getScriptInfo(Path(__file__))[8], f)) if fileExtention in f]

        numFoundFiles = len(onlyFiles)
        fileMode = ''

        while True:
            try:
                if numFoundFiles > 0:
                    answer = int(input("\n\tI've detected " + str(numFoundFiles) + " more " + fileExtention +
                                       " files.\n\tWhat do you want to do?\n\n1. Read file(s)\n2. Overwrite existing file(s)\n3. Continue with existing?"))
                    if answer == 1:
                        fileMode = 'r'
                        break
                    elif answer == 2:
                        fileMode = 'w'
                        break
                    elif answer == 3:
                        fileMode = 'a+'
                        break
                    else:
                        raise ValueError
                else:
                    print('Wakker Worden')
                    fileMode = 'w'
                    break

            except ValueError:
                print('\nThat\'s not a valid input. Try again!')
                time.sleep(3)
                continue

        return fileMode

    @classmethod
    def replaceWhiteSpace(cls, char, string=None):
        ''' Replace white Spaces with a character '''
        indx = 0

        for i in string:
            if ' ' in string[indx]:
                string[indx] = string[indx].replace(' ', char)
            indx += 1

        return string
#     # Save Append Read Files
#     # Lists certain
#     # Naming there 'YouExam' Files
#     pass


# def saveToFile(isTrue, addQuestion, questionNumber):
#     ''' To save Q and A to a file '''

#     if isTrue is True:
#         with open("YourExam.txt", 'w', encoding="utf-8") as f:
#             strToFile = "{}\tQuestion:\t{}\n\tAnswer:\t\t{}\n\n".format(
#                 questionNumber, addQuestion[questionNumber][0], addQuestion[questionNumber][1])

#             f.write(strToFile)


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")
