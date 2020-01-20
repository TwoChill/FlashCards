from pathlib import Path
import platform
import os
import random
import curses


class myExam(object):
    ''' To create own exam'''

    def __init__(self):
        self.question = ''
        self.answer = ''

    def addNew(self, newQuestion=None, newAnswer=None):
        ''' Add new Question and / or Answer'''

        if newQuestion is None:
            newQuestion = []
        elif newQuestion is not None:
            self.question = newQuestion

        if newAnswer is None:
            newAnswer = []
        elif newAnswer is not None:
            self.answer = newAnswer

        return [self.question, self.answer]

    def addNewAnswer(self):
        ''' Add new answer '''

        self.answer = newAnswer
        return self.answer

    def randomQuestion(self, question):
        ''' Randomize questions '''

        randomNr = random.randint(1, len(question))
        print('This is random nr: ', randomNr)

        return self.question[randomNr], randomNr


def getScriptName():
    ''' Return script name'''

    filePath = str(Path(__file__).absolute())
    fileExtention = filePath[len(filePath) - 3:]
    directoryPath = str(os.path.dirname(os.path.abspath(__file__)))
    scriptName = filePath[(len(directoryPath) + 1):-len(fileExtention)]

    return scriptName


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")
