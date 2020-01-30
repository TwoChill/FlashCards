import os
import sys
import time
import random
import platform
from pathlib import Path
from os.path import isfile, join

answerNo = ('N', 'NO', 'n', 'No', 'nO')
answerYes = ('Y', 'y', 'YES', 'YEs', 'Yes', 'yEs', 'yeS', 'yes')


def startMenu():
    ''' Option menu '''

    keepDirTreeUp()

    list = ['Create New Exam', 'Rename Exam', 'Delete Exam',
            'Create new Q and A', 'Rename Q and A', 'Delete Q and A']

    for num, item in enumerate(list, 1):
        print(str(num) + '. ' + item)

    try:
        menuOutput = int(input("\n:> "))
    except ValueError:
        keepDirTreeUp()
        print('That\'s not what I expected. Try Again')
        time.sleep(3)
        startMenu()

    return menuOutput


def fileHandeling(menuOutput):
    ''' Handels everything to do with files '''

    if menuOutput == 1:
        pass
    if menuOutput == 2:
        pass
    if menuOutput == 3:
        deleteExam(menuOutput)
    if menuOutput == 4:
        pass
    if menuOutput == 5:
        pass
    if menuOutput == 6:
        pass


def createMain():
    ''' Create main directory '''

    try:
        parent_Folder_Name = 'My_Exams'
        os.mkdir(f'{parent_Folder_Name}')
    except FileExistsError:
        pass

    # Change directory to My_Exams
    os.chdir(os.getcwd() + '/' + parent_Folder_Name)

    # Save directory path
    parent_Folder_Path = os.getcwd() + '/' + parent_Folder_Name

    return parent_Folder_Name, parent_Folder_Path


def createExam(parentPath):
    ''' Create child folder and exam file '''

    keepDirTreeUp()

    try:
        while True:
            exam_Folder_Name = input('\nExam Folder Name? :> ')
            keepDirTreeUp()
            answer = input(f'\nIs \'{exam_Folder_Name}\' correct? (Y/N) :> ')
            if answer in answerNo:
                keepDirTreeUp()
                continue
            elif answer in answerYes:
                os.mkdir(f'{exam_Folder_Name}')
                print(f'\n\'{exam_Folder_Name}\' has been made.')
                keepDirTreeUp()
                time.sleep(3)
                break
            else:
                print('\nThat\'s not a correct answer!')
                keepDirTreeUp()
                time.sleep(2)
                continue

        exam_Folder_Path = f'{parentPath}/{exam_Folder_Name}'

        return exam_Folder_Name, exam_Folder_Path

    except FileExistsError:
        randomnr = str(random.randint(2, 100))

        if f'{exam_Folder_Name}_{randomnr}' == os.path.isdir(f'{parentPath}/{exam_Folder_Name}' + '/' + f'{exam_Folder_Name}_{randomnr}'):
            randomnr += randomnr

        os.mkdir(f'{exam_Folder_Name}_{randomnr}')

        exam_Folder_Path = f'{parentPath}/{exam_Folder_Name}'
        return exam_Folder_Name, exam_Folder_Path


def keepDirTreeUp(dirPath=None, printStatement=None):
    ''' Shows Directory Tree to User '''

    sys_clear()

    if dirPath is None:
        dirPath = os.getcwd()

    if printStatement is None:
        print('\nYour Directory Tree\n')
    else:
        print(f'\n{printStatement}\n')

    print('-' * (len(max([f for f in os.listdir(dirPath)])) + 6))
    ##########################################################
    #  Credits to User Adam on StackOverFlow. !Link Below!   #
    ##########################################################
    paths = DisplayablePath.make_tree(Path(dirPath))         #
    for path in paths:                                       #
        print(path.displayable())                            #
    ##########################################################
    print('-' * (len(max([f for f in os.listdir(dirPath)])) + 6) + '\n')


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")


class DisplayablePath(object):

    #######################################################################################
    # https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python #
    #######################################################################################

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

        displayable_root = cls(
            root, parent, is_last)
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
