from pathlib import Path
import platform
import os
# from os import listdir
# from os.path import isfile, join
import time
import random

# Questions and Answers are stored with this type of file extention.
fileExtention = '.txt'
filePath = str(Path(__file__).absolute())
fileExt = filePath[len(filePath) - 3:]
directoryPath = str(os.path.dirname(os.path.abspath(__file__)))
scriptName = filePath[(len(directoryPath) + 1):-len(fileExtention)]
answerYes = ('Y', 'y', 'YES', 'YEs', 'Yes', 'yEs', 'yeS', 'yes')
answerNo = ('N', 'NO', 'n', 'No', 'nO')


class MyExam(object):
    ''' To create own exam'''

    def __init__(self):
        self.question = ''
        self.answer = ''

    def addNew(self, newQuestion=None, newAnswer=None):
        ''' Add a new Question and an Answer'''

        if newQuestion is None:
            newQuestion = []
        else:
            self.question = newQuestion

        if newAnswer is None:
            newAnswer = []
        else:
            self.answer = newAnswer

        return [self.question, self.answer]

    def randomQuestion(self, question):
        ''' Randomize questions '''

        randomNr = random.randint(1, len(question))
        print('This is random nr: ', randomNr)

        return self.question[randomNr], randomNr


class FileHandling(object):
    ''' Everything to do with files '''

    def __init__(self, isTrue, addQuestion, questionNumber):
        self.isTrue = isTrue
        self.addQuestion = addQuestion
        self.questionNumber = questionNumber
        self.Main_Folder_Path_Path = ''

    def createFolder(self):
        ''' Create a folder in current file directory if non exit '''

        # Make Parent Folder ([3] = Directory Path of This Script)
        print('This is CWD:', os.cwd())

        os.chdir(f'{directoryPath}')

        # Create a standard Parent Folder
        try:
            nameFolder = 'My_Exams'
            os.mkdir(f'{nameFolder}')
        except FileExistsError:
            pass

        Main_Folder_Path_Path = f'{directoryPath}/{nameFolder}'

        # If empty create Exam folder (Python)
        if not os.listdir(Main_Folder_Path_Path):
            while True:
                answer = input(
                    '\nWhat\'s the foldername in which you\'ll store your exam files?\n(Ex: \'Python\' or \'Ruby\') :> ')
                answerCheck = input(f'\nIs \'{answer}\' correct? (Y/N) :> ')
                if answerCheck in answerNo:
                    continue
                else:
                    os.mkdir(f'{Main_Folder_Path_Path}/{answer}')
                    print(f'\nYour \'{answer} folder\' has been made!')
                    time.sleep(3)
                    break
        else:
            print('\nFound the following exam\'s:\n\n')

            #########################################################
            ## Credits to User Adam on StackOverFlow. !Link Below! ##
            #########################################################
            paths = DisplayablePath.make_tree(Path(Main_Folder_Path_Path))
            for path in paths:
                print(path.displayable())
            #########################################################

        return Main_Folder_Path_Path, nameFolder

        os.chdir(f'{Main_Folder_Path_Path}')

    # Save Q and A to file
    def saveToFile(self, addQuestion, questionNumber, fileMode):
        ''' To save Q and A to a file '''

        with open("YourExam.txt", fileMode, encoding="utf-8") as f:
            strToFile = "{}\tQuestion:\t{}\n\tAnswer:\t\t{}\n\n".format(
                questionNumber, addQuestion[questionNumber][0], addQuestion[questionNumber][1])

            f.write(strToFile)

    def readFromFile(self, fileMode):
        ''' Read Exam Questions '''

        with open("YourExam.txt", "r") as f:
            f.read("YourExam.txt")

    # Create main folder AND CHILD folder
    @ staticmethod
    def createMainFolder():
        # Change to parent folder
        os.chdir(f'{directoryPath}')

        isTrue = True

        while isTrue:
            print('\nLet\'s make a new \'main\' folder for your exam\'s!\n')

            ##########################################################
            ## Credits to User Adam on StackOverFlow. !Link Below! ###
            ##########################################################
            print('-' * 30)                                          #
            paths = DisplayablePath.make_tree(Path(directoryPath))   #
            for path in paths:                                       #
                print(path.displayable())                            #
            print('-' * 30)                                          #
            ##########################################################

            answer = input(
                '\nChoose a folder name...\n(Ex: \'My_Exams\' or \'Main\'):> ')
            answerCheck = input(f'\nIs \'{answer}\' correct? (Y/N) :> ')

            if answerCheck in answerNo:
                continue
            else:
                nameFolder = f'{answer}'

                try:
                    os.mkdir(f'{nameFolder}')
                    sys_clear()
                    # print('\n')
                    break
                except FileExistsError:
                    print(
                        f"\nThere's already a folder with the name '{answer}'.")
                    while isTrue:
                        answerCheck = input(
                            f'Do you want to keep \'{answer}\' folder and it\'s content? (Y/N) :> ')
                        if answerCheck in answerNo:
                            sys_clear()
                            continue
                        else:
                            sys_clear()
                            isTrue = False

        Main_Folder_Path = f'{directoryPath}/{nameFolder}'

        # If My_Exam is empty create Exam folder (Python)
        if not os.listdir(Main_Folder_Path):
            while True:

                print(f'\nLet\'s create another folder inside \'{answer}\'. \n')

                ##########################################################
                ## Credits to User Adam on StackOverFlow. !Link Below! ###
                ##########################################################
                print('-' * 30)                                          #
                paths = DisplayablePath.make_tree(Path(directoryPath))   #
                for path in paths:                                       #
                    print(path.displayable())                            #
                print('-' * 30)                                          #
                ##########################################################

                answer = input(
                    '\nChoose a folder name: \n(Ex: \'Python\' / \'Ruby\' or \'Flashcards\') :> ')
                answerCheck = input(f'\nIs \'{answer}\' correct? (Y/N) :> ')
                if answerCheck in answerNo:
                    sys_clear()
                    continue
                else:
                    sys_clear()
                    # print('\n')
                    os.mkdir(f'{Main_Folder_Path}/{answer}')

                    print(f'\nYour \'{answer}\' has been made!')
                    time.sleep(3)
                    input('\nHit ENTER to continue... ')
                    sys_clear()
                    break
        else:
            print('\nFound the following exam\'s:\n')

            ##########################################################
            ## Credits to User Adam on StackOverFlow. !Link Below! ###
            ##########################################################
            print('-' * 30)                                          #
            paths = DisplayablePath.make_tree(Path(Main_Folder_Path))#
            for path in paths:                                       #
                print(path.displayable())                            #
            print('-' * 30)                                          #
            ##########################################################

            while True:

                if fileExtention in [f for f in os.listdir(Main_Folder_Path)]:
                    print('>> One')
                    answer = int(input(f'''\nDo you want to:
1. Create a new exam file? (second option = which folder inside '{answer}'.)
2. Create a new exam folder inside '{answer}'?
3. Delete an exam file?
4. Delete an exam folder?

5. Continue with an exiting exam file? (Shows only if there is a file with f'{fileExtention}')

:> '''))
                else:
                    print('>> Two')
                    answer = int(input(f'''\nDo you want to:
1. Create a new exam file? (second option = which folder inside '{answer}'.)
2. Create a new exam folder inside '{answer}'?
3. Delete an exam file?
4. Delete an exam folder?

:> '''))

        return Main_Folder_Path, nameFolder


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")

#######################################################################################
#######################################################################################
# https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python #
#######################################################################################
#######################################################################################
                                                                                      #
class DisplayablePath(object):                                                        #
    display_filename_prefix_middle = '├──'                                            #
    display_filename_prefix_last = '└──'                                              #
    display_parent_prefix_middle = '    '                                             #
    display_parent_prefix_last = '│   '                                               #
                                                                                      #
    def __init__(self, path, parent_path, is_last):                                   #
                                                                                      #
        self.path = Path(str(path))                                                   #
        self.parent = parent_path                                                     #
        self.is_last = is_last                                                        #
        if self.parent:                                                               #
            self.depth = self.parent.depth + 1                                        #
        else:                                                                         #
            self.depth = 0                                                            #
                                                                                      #
    @property                                                                         #
    def displayname(self):                                                            #
        if self.path.is_dir():                                                        #
            return self.path.name + '/'                                               #
        return self.path.name                                                         #
                                                                                      #
    @classmethod                                                                      #
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):              #
        root = Path(str(root))                                                        #
        criteria = criteria or cls._default_criteria                                  #
                                                                                      #
        displayable_root = cls(root, parent, is_last)                                 #
        yield displayable_root                                                        #
                                                                                      #
        children = sorted(list(path                                                   #
                               for path in root.iterdir()                             #
                               if criteria(path)),                                    #
                          key=lambda s: str(s).lower())                               #
        count = 1                                                                     #
        for path in children:                                                         #
            is_last = count == len(children)                                          #
            if path.is_dir():                                                         #
                yield from cls.make_tree(path,                                        #
                                         parent=displayable_root,                     #
                                         is_last=is_last,                             #
                                         criteria=criteria)                           #
            else:                                                                     #
                yield cls(path, displayable_root, is_last)                            #
            count += 1                                                                #
                                                                                      #
    @classmethod                                                                      #
    def _default_criteria(cls, path):                                                 #
        return True                                                                   #
                                                                                      #
    @property                                                                         #
    def displayname(self):                                                            #
        if self.path.is_dir():                                                        #
            return self.path.name + '/'                                               #
        return self.path.name                                                         #
                                                                                      #
    def displayable(self):                                                            #
        if self.parent is None:                                                       #
            return self.displayname                                                   #
                                                                                      #
        _filename_prefix = (self.display_filename_prefix_last                         #
                            if self.is_last                                           #
                            else self.display_filename_prefix_middle)                 #
                                                                                      #
        parts = ['{!s} {!s}'.format(_filename_prefix,                                 #
                                    self.displayname)]                                #
                                                                                      #
        parent = self.parent                                                          #
        while parent and parent.parent is not None:                                   #
            parts.append(self.display_parent_prefix_middle                            #
                         if parent.is_last                                            #
                         else self.display_parent_prefix_last)                        #
            parent = parent.parent                                                    #
                                                                                      #
        return ''.join(reversed(parts))                                               #
                                                                                      #
#######################################################################################
#######################################################################################
