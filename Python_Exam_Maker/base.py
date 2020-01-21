import platform
import os
import random

# Questions and Answers are stored with this type of file extention.
fileExtention = '.txt'


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
    ''' Return script name'''

    filePath = str(pathFileName.absolute())
    fileExt = filePath[len(filePath) - 3:]
    directoryPath = str(os.path.dirname(os.path.abspath(__file__)))
    scriptName = filePath[(len(directoryPath) + 1):-len(fileExtention)]

    return [filePath, fileExt, directoryPath, scriptName]


# class FileHandling(object):
#     ''' Everything to do with files '''
#     # Save Append Read Files
#     # Lists certain
#     # Naming there 'YouExam' Files
#     pass


def saveToFile(isTrue, addQuestion, questionNumber):
    ''' To save Q and A to a file '''

    if isTrue is True:
        with open("YourExam.txt", 'w', encoding="utf-8") as f:
            strToFile = "{}\tQuestion:\t{}\n\tAnswer:\t\t{}\n\n".format(
                questionNumber, addQuestion[questionNumber][0], addQuestion[questionNumber][1])

            f.write(strToFile)


def appendToFile(isTrue, addQuestion, questionNumber):
    ''' To append Q and A to a file '''

    if isTrue is True:
        with open("YourExam.txt", 'a+', encoding="utf-8") as f:
            strToFile = "{}\tQuestion:\t{}\n\tAnswer:\t\t{}\n\n".format(
                questionNumber, addQuestion[questionNumber][0], addQuestion[questionNumber][1])

            f.write(strToFile)


def readFromFile(isTrue):
    ''' Read Exam Questions '''

    if isTrue is True:
        with open("YourExam.txt", "r") as f:
            f.read("YourExam.txt")


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")
