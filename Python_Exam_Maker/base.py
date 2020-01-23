
from pathlib import Path
import platform
import os
from os import listdir
from os.path import isfile, join
import time
import random

# Questions and Answers are stored with this type of file extention.
answerYes = ('Y', 'y', 'YES', 'YEs', 'Yes', 'yEs', 'yeS', 'yes')
answerNo = ('N', 'NO', 'n', 'No', 'nO')
fileExtention = '.txt'
nameExamPathFile = ''
noFiles = 0


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
    directoryPath = os.path.dirname(os.path.abspath(__file__))
    scriptName = filePath[(len(directoryPath) + 1):-len(fileExtention)]
    parentPath = os.path.abspath(os.path.join(directoryPath, os.pardir))
    parentPath2 = os.path.abspath(os.path.join(parentPath, os.pardir))
    parentName = parentPath[(len(parentPath2) + 1):]
    directoryPathName = directoryPath[(len(parentPath) + 1):]

    return [fileExt, scriptName, filePath, directoryPath, directoryPathName, parentPath, parentName, parentPath2]


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")


# def createExamDir():
#     ''' Creates a new directory to save ExamFiles.fileExtention'''
#     # Break section up in 2
#     # 1. create folder
#     # 2. create file
#     try:
#             # Makes sure we are in the directory of this script.
#         os.chdir(f'{getScriptInfo(Path(__file__))[3]}')

#         # If a file allready exist raise error
#         if False:  # nameExamPathFile == getScriptInfo(Path(__file__))[6]:
#             print('Way', getScriptInfo(Path(__file__))[6])
#             raise FileExistsError
#         else:

#                         else:
#                             print(
#                                 '\nThat\'s not a valid input. Try again please!2')
#                             time.sleep(3)
#                             break

#                 elif answer in answerNo:
#                     while True:
#                         folderName = input(
#                             '\nWhat\'s the name of you exam file? :> ')
#                         answer = input(f"Is '{folderName}' correct?")
#                         if answer in answerYes:
#                             if dirName != '':
#                                 os.mkdir(f'{dirName}/{folderName}')
#                             else:
#                                 os.mkdir(f'{folderName}')
#                             break
#                         elif answer in answerNo:
#                             print(
#                                 'Just choose someting like "MyExam" or the subject you want to deep learn..')
#                             continue
#                         else:
#                             print(
#                                 '\nThat\'s not a valid input. Try again please!3')
#                             time.sleep(3)
#                             continue
#                 else:
#                     print(
#                         '\nThat\'s not a valid input. Try again please!4')
#                     time.sleep(3)
#                     continue

#         if dirName != '':
#             nameExamPathFile = dirName + "/" + folderName
#             return nameExamPathFile
#         else:
#             nameExamPathFile = folderName
#             return nameExamPathFile

#     except FileExistsError:
#         print('File Exist?')
#         pass


class FileHandling(object):
    ''' Everything to do with files '''

    def __init__(self, isTrue, addQuestion, questionNumber):
        self.isTrue = isTrue
        self.addQuestion = addQuestion
        self.questionNumber = questionNumber

    def createFolder(self):
        ''' Create a folder in current file directory if non exit '''

        # Make Parent Folder ([3] = Directory Path of This Script)
        os.chdir(f'{getScriptInfo(Path(__file__))[3]}')

        # Create a standard Parent Folder
        try:
            nameFolder = 'My_Exams'
            os.mkdir(f'{nameFolder}')
        except FileExistsError:
            pass

        parentExamFolder = f'{getScriptInfo(Path(__file__))[3]}/{nameFolder}'

        # If empty create Exam folder (Python)

        if not os.listdir(parentExamFolder):
            while True:
                answer = input(
                    '\nWhat\'s the foldername in which you\'ll store your exam files?\n(Ex: \'Python\' or \'Ruby\') :> ')
                answerCheck = input(f'\nIs \'{answer}\' correct? (Y/N) :> ')
                if answerCheck in answerNo:
                    continue
                else:
                    os.mkdir(f'{parentExamFolder}/{answer}')
                    print(f'\nYour \'{answer} folder\' has been made!')
                    time.sleep(3)
                    break
        else:
            print('\nFound the following exam\'s:\n\n')

            #########################################################
            ## Credits to User Adam on StackOverFlow. !Link Below! ##
            #########################################################
            paths = DisplayablePath.make_tree(Path(parentExamFolder))
            for path in paths:
                print(path.displayable())
            #########################################################

        # Back to main parent folder
        os.chdir(f'{getScriptInfo(Path(__file__))[3]}')

    def saveToFile(self, isTrue, addQuestion, questionNumber, fileMode):
        ''' To save Q and A to a file '''

        if isTrue is True:
            fileMode = ''

            # if questionNumber == 0:
            #     questionNumber += 1
            #     fileMode = 'w'
            # else:
            #     fileMode = 'a+'

            # Check if there are no whitespaces in filePath.
            self.replaceWhiteSpace(getScriptInfo(Path(__file__))[2], '_')

            with open(f"{nameExamPathFile}{fileExtention}", fileMode, encoding="utf-8") as f:
                strToFile = "{}\tQuestion:\t{}\n\tAnswer:\t\t{}\n\n".format(
                    questionNumber, addQuestion[questionNumber][0], addQuestion[questionNumber][1])

                f.write(strToFile)

    @staticmethod
    def foundFile():
        ''' Checks for ExamFiles '''

        # Lists all the files in the directory of this script with a certain !fileExtention!
        onlyFiles = [f for f in listdir(getScriptInfo(Path(__file__))[3]) if isfile(
            join(getScriptInfo(Path(__file__))[3], f)) if fileExtention in f]
        print(onlyFiles)
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
                    time.sleep(5)
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

#######################################################################################
#######################################################################################
# https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python #
#######################################################################################
#######################################################################################


class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))

#######################################################################################
#######################################################################################
