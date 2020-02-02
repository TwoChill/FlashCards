import os
import sys
import time as systime
import random
import platform
from pathlib import Path
from os.path import isfile, join

answerNo = ('N', 'NO', 'NEE')
answerYes = ('Y', 'YES', 'J', 'JA')
menuOption_Back = ('B', 'BACK', 'RETURN')
menuOption_Quit = ('Q', 'QUIT', 'STOP')
selectAll = ('A', 'ALL', 'EVERYTHING',
             'SELECT EVERYTHING', 'SELECT ALL', 'SELECT A')
bottomPrintStatement_1 = 'Which \'Directory\' do you want to delete?\n'
bottomPrintStatement_2 = 'Create Exam Folder\n'


def startMenu(parent_Folder_Path):
    ''' Display Main Menu'''

    # Keep Directory Tree and Clear Screen
    keepDirTreeUp(None, None, 'Menu\n')

    list = ['Create a New Exam Folder', 'Rename an Exam Folder', 'Delete an Exam Folder',
            'Create a New Exam File', 'Rename an Exam File', 'Delete an Exam File', 'Quit']

    # Print a numbered list on screen.
    for num, item in enumerate(list, 1):
        if item in list[-1:]:
            print('\n' + str(num) + '. ' + item)
        else:
            print(str(num) + '. ' + item)

    try:
        menuOption = int(input("\n:> "))
        fileHandeling(menuOption, parent_Folder_Path)
    except ValueError:

        # Keep Directory Tree and Clear Screen
        keepDirTreeUp()
        print('That\'s not what I expected. Try Again')
        systime.sleep(3)

        # Back to Main Menu
        startMenu(parent_Folder_Path)

    return menuOption, parent_Folder_Path


def fileHandeling(menuOption, parent_Folder_Path):
    ''' Handels everything to do with files '''

    if menuOption == 1:
        exam_Folder_Name, exam_Folder_Path = createExam()
    elif menuOption == 2:
        pass
    elif menuOption == 3:
        deleteExam(menuOption, parent_Folder_Path)
    elif menuOption == 4:
        pass
    elif menuOption == 5:
        pass
    elif menuOption == 6:
        pass
    elif menuOption == 7 or menuOption in menuOption_Quit:

        # Keep Directory Tree and Clear Screen
        keepDirTreeUp()
        loadingAnimation("Quitting", None, 15, .05)
        sys_clear()
        quit()
    else:
        pass


def loadingAnimation(txt, chars, vector, sleep):
    ''' Display's an animation for 'Loading' or 'Deleting' '''

    if chars is None:
        chars = "/—\|"

    chars = f'{chars}' * vector
    for char in chars:
        sys.stdout.write(f'\r' + f'{txt} ' + char)
        systime.sleep(sleep)
        sys.stdout.flush()


def createMain():
    ''' Create main directory '''

    # Change into directory of this script.
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    try:
        # Create Main Folder
        parent_Folder_Name = 'My_Exams'
        os.mkdir(f'{parent_Folder_Name}')
    except FileExistsError:
        pass

    # Change directory to My_Exams
    os.chdir(os.getcwd() + '/' + parent_Folder_Name)

    # Save directory path
    parent_Folder_Path = os.getcwd() + '/' + parent_Folder_Name

    return parent_Folder_Name, parent_Folder_Path


def createExam():
    ''' Create child folder and exam file '''

    # Keep Directory Tree and Clear Screen
    keepDirTreeUp(None, None, bottomPrintStatement_2)

    try:
        while True:
            exam_Folder_Name = input('Exam Folder Name? :> ')

            # Keep Directory Tree and Clear Screen
            keepDirTreeUp(None, None, bottomPrintStatement_2)

            answer = input(
                f'Is \'{exam_Folder_Name}\' correct? (Y/N) :> ').upper()

            if answer in answerNo:

                # Keep Directory Tree and Clear Screen
                keepDirTreeUp(None, None, bottomPrintStatement_2)

                continue
            elif answer in answerYes:

                # Makes new Exam Directory
                os.mkdir(f'{exam_Folder_Name}')

                # Keep Directory Tree and Clear Screen
                keepDirTreeUp(None, None, bottomPrintStatement_2)

                # Back to Main Menu
                startMenu(os.getcwd())
                break
            else:
                # Keep Directory Tree and Clear Screen
                keepDirTreeUp(None, None, bottomPrintStatement_2)

                print('That\'s not a correct answer!')
                systime.sleep(2)
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


def deleteExam(menuOption, parent_Folder_Path):
    ''' Delete Exam Folder '''

    # Keep Directory Tree and Clear Screen
    keepDirTreeUp(None, None, bottomPrintStatement_1)

    while True:
        try:
            # If My_Exam folder is empty..
            if len(os.listdir(os.getcwd())) == 0:

                # Show Searching Animation.
                loadingAnimation('Searching...', None, 15, .05)
                systime.sleep(1)

                # Keep Directory Tree and Clear Screen
                keepDirTreeUp(
                    None, None, bottomPrintStatement_1)

                print('No Exam(\'s) found!')
                systime.sleep(5)

                # Back to Main Menu
                startMenu(parent_Folder_Path)

            # Create a dictionary and prints a list of folders inside current working directory.
            delDir = {}
            count = 1
            for num, item in enumerate(os.listdir(os.getcwd()), 1):
                delDir[num] = item
                print(str(num) + '. ' + "'" + item + "'")
                count += 1

            # Print Back option on screen.
            print('\n' + str(count) + '. ' + 'Back')

            while True:
                try:
                    folderNr = int(input('\n:> '))

                    # If folderNr in range of the number of folders..
                    if folderNr in range(1, (len(delDir)) + 1):
                        # if not loop through files en remove them
                        # then remove folder itself

                        # Change working directory to user's chosen path.
                        os.chdir(f'{os.getcwd()}/{delDir[folderNr]}')

                        # Create dictionary of files in current working directory
                        delFile = {}
                        for num, files in enumerate(os.listdir(os.getcwd()), 1):
                            delFile[num] = files

                        # If there are more the 5 file in directory, speed up animation.
                        if len(delFile) > 5:
                            vector = 10     # Used for nr animation dispay
                            time = .01      # Used for systime.sleep between animations
                        else:
                            vector = 15     # Used for nr animation dispay
                            time = .05      # Used for systime.sleep between animations

                        # If chosen folder is NOT empty
                        folderNotEmpty = len(
                            [f for f in os.listdir(os.getcwd())])

                        if folderNotEmpty > 0:
                            print(
                                f'\nDirectory: \'{delDir[folderNr]}\' is not empty!\n')

                            # Keep Directory Tree and Clear Screen
                            keepDirTreeUp(
                                None, f'{delDir[folderNr]}', bottomPrintStatement_1)

                            # !!! Next answer should be a list created by a for loop wich also inclueds subfolders in list.
                            try:
                                while True:
                                    answer = int(
                                        input(f'1. Delete Directory: \'{delDir[folderNr]}\'?\n2. Delete Files?\n\n3. Back\n\n:> '))
                                    if answer == 1:

                                        # Keep Directory Tree and Clear Screen
                                        keepDirTreeUp(
                                            None, f'{delDir[folderNr]}')

                                        # Delete's files in chosen folder first.
                                        for files in os.listdir(os.getcwd()):
                                            os.remove(f'{os.getcwd()}/{files}')

                                            # Change to parent directory of current working directory and..
                                            os.chdir(
                                                os.path.dirname(os.getcwd()))

                                        # ..delete chosen folder itself.
                                        os.rmdir(
                                            f'{os.getcwd()}/{delDir[folderNr]}')

                                        # Show Deleting Animation.
                                        loadingAnimation(
                                            f'DELETING \'{delDir[folderNr]}\'.. ', None, 15, .05)

                                        # Keep Directory Tree and Clear Screen
                                        keepDirTreeUp()

                                        # Back to Main Menu
                                        startMenu(parent_Folder_Path)
                                        break
                                    elif answer == 2:

                                        # Keep Directory Tree and Clear Screen
                                        keepDirTreeUp(
                                            None, f'{delDir[folderNr]}', )

                                        # Creates a dict of files inside current working directory
                                        for num, files in delFile.items():
                                            print(str(num) + '. ' + files)

                                        while True:
                                            try:
                                                # If there's only 1 file in the directory
                                                if len([f for f in os.listdir(os.getcwd())]) == 1:
                                                    fileNr = 1
                                                    answer = input(
                                                        f'DELETE2 \'{delFile[fileNr]}\'? (Y/N) :> ').upper()
                                                else:
                                                    # When there are more then one file in the directory
                                                    try:
                                                        fileNr = int(input(
                                                            '\nDelete which file(s)?\n--Type \'0\' for All--\n\n:> '))

                                                        # Keep Directory Tree and Clear Screen
                                                        keepDirTreeUp(
                                                            None, f'{delDir[folderNr]}')
                                                    except ValueError:
                                                        fileNr = 0
                                                        # IF BACK go back !!!
                                                    if fileNr == 0:
                                                        for num, file in delFile.items():

                                                            # Show Deleting Animation.
                                                            loadingAnimation(
                                                                f'DELETING.. \'{delFile[num]}\'.. ', None, vector, time)

                                                            # Removing files from the directory. Via this for loop, removes them all.
                                                            os.remove(
                                                                os.getcwd() + '/' + f'{file}')
                                                            keepDirTreeUp(
                                                                None, f'{delDir[folderNr]}')

                                                        # Change current working directory to My_Exam folder.
                                                        os.chdir(
                                                            os.path.dirname(os.getcwd()))

                                                        # Keep Directory Tree and Clear Screen
                                                        keepDirTreeUp()

                                                        print(
                                                            f'\nAll files has been deleted!')
                                                        systime.sleep(5)

                                                        # Back to Main Menu
                                                        startMenu(
                                                            parent_Folder_Path)
                                                    else:

                                                        # Keep Directory Tree and Clear Screen
                                                        keepDirTreeUp(
                                                            None, f'{delDir[folderNr]}')

                                                        answer = input(
                                                            f'\nDELETE \'{delFile[fileNr]}\'? (Y/N) :> ').upper()

                                                        if answer in answerNo:

                                                            # Keep Directory Tree and Clear Screen
                                                            keepDirTreeUp(
                                                                None, f'{delDir[folderNr]}')
                                                            continue
                                                        else:

                                                            # Keep Directory Tree and Clear Screen
                                                            keepDirTreeUp(
                                                                None, f'{delDir[folderNr]}')
                                                            os.remove(
                                                                f'{os.getcwd()}/{delFile[fileNr]}')

                                                            # Show Deleting Animation.
                                                            loadingAnimation(
                                                                f'DELETING.. \'{delFile[num]}\'.. ', None, vector, time)

                                                # Program Flow
                                                if answer in answerNo:

                                                    # Keep Directory Tree and Clear Screen
                                                    keepDirTreeUp(
                                                        None, f'{delDir[folderNr]}')
                                                    continue
                                                elif answer in answerYes:

                                                    # Keep Directory Tree and Clear Screen
                                                    keepDirTreeUp(
                                                        None, f'{delDir[folderNr]}')

                                                    # Show Deleting Animation.
                                                    loadingAnimation(
                                                        f'DELETING \'{delFile[fileNr]}\'.. ', None, 15, .05)

                                                    # Removing file
                                                    try:
                                                        os.remove(
                                                            f'{os.getcwd()}/{delFile[fileNr]}')
                                                    except FileNotFoundError:

                                                        # Keep Directory Tree and Clear Screen
                                                        keepDirTreeUp(
                                                            None, f'{delDir[folderNr]}')

                                                        print(
                                                            f'\'{delFile[fileNr]}\' has been deleted!')

                                                        systime.sleep(5)

                                                        # Back to Main Menu
                                                        startMenu(
                                                            parent_Folder_Path)

                                            except ValueError:
                                                # Keep Directory Tree and Clear Screen
                                                keepDirTreeUp()
                                                print('This the one')
                                                systime.sleep(10)
                                                continue
                                    else:
                                        # Keep Directory Tree and Clear Screen
                                        keepDirTreeUp()

                                        # Back to Main Menu
                                        startMenu(parent_Folder_Path)

                            except ValueError:
                                # Keep Directory Tree and Clear Screen
                                keepDirTreeUp()
                                print('This the two')
                                systime.sleep(10)
                                continue

                        # If chosen folder IS empty
                        else:
                            # Keep Directory Tree and Clear Screen
                            keepDirTreeUp(os.path.dirname(
                                os.getcwd()), None, bottomPrintStatement_1)

                            # Confrimation of Deletion:
                            while True:
                                answer = input(
                                    f'DELETE \'{delDir[folderNr]}\'? (Y/N) :> ').upper()

                                if answer in answerNo:

                                    # Keep Directory Tree and Clear Screen
                                    keepDirTreeUp(os.path.dirname(
                                        os.getcwd()), None, bottomPrintStatement_1)

                                    break
                                elif answer in answerYes:

                                    # Keep Directory Tree and Clear Screen
                                    keepDirTreeUp(os.path.dirname(
                                        os.getcwd()), None, bottomPrintStatement_1)

                                    # Show Deleting Animation.
                                    loadingAnimation(
                                        f'DELETING \'{delDir[folderNr]}\'.. ', None, vector, time)

                                    # Keep Directory Tree and Clear Screen
                                    keepDirTreeUp(os.path.dirname(
                                        os.getcwd()), None, bottomPrintStatement_1)

                                    # Change current working directory to deleted folder's parent
                                    os.chdir(os.path.dirname(os.getcwd()))

                                    # Remove current directory
                                    os.rmdir(
                                        f'{os.getcwd()}/{delDir[folderNr]}')

                                    print(
                                        f'\n\'{delDir[folderNr]}\' has been deleted!')

                                    systime.sleep(5)

                                    # Back to Main Menu
                                    startMenu(parent_Folder_Path)
                                    break
                    else:
                        # Keep Directory Tree and Clear Screen
                        keepDirTreeUp()

                        # Back to Main Menu
                        startMenu(parent_Folder_Path)

                except ValueError:

                    # Back to Main Menu
                    startMenu(parent_Folder_Path)
                    break

                    keepDirTreeUp()
                    continue
        except ValueError:

            # Keep Directory Tree and Clear Screen
            keepDirTreeUp(os.path.dirname(os.getcwd()))
            print('This the three')
            systime.sleep(10)
            continue

    return answer


def keepDirTreeUp(dirPath=None, dirName=None, bottomStatement=None):
    ''' Shows Directory Tree to User with or without the Directory Name and/or printstatement at the bottom'''

    sys_clear()

    if dirPath is None:
        dirPath = os.getcwd()

    if dirName is None:
        print('\nYour Directory Tree\n')
    else:
        print(f'\nDirectory Tree: \'{dirName}\'\n')

    if bottomStatement is None:
        bottomStatement = '\r'

    print('-' * (len(f' Tree: \'{dirName}\'') + 6))
    ##########################################################
    #  Credits to User Adam on StackOverFlow. !Link Below!   #
    ##########################################################
    paths = DisplayablePath.make_tree(Path(dirPath))         #
    for path in paths:                                       #
        print(path.displayable())                            #
    ##########################################################
    print('-' * (len(f' Tree: \'{dirName}\'') + 6) + '\n')

    print(bottomStatement)


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
