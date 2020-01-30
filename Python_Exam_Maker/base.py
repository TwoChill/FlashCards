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


def startMenu():
    ''' Option menu '''

    keepDirTreeUp()

    list = ['Create New Exam', 'Rename Exam', 'Delete Exam',
            'Create new Q and A', 'Rename Q and A', 'Delete Q and A', 'Quit']

    # Print a numbered list on screen.
    for num, item in enumerate(list, 1):
        if item in list[-1:]:
            print('\n' + str(num) + '. ' + item)
        else:
            print(str(num) + '. ' + item)

    try:
        menuOption = int(input("\n:> "))
        fileHandeling(menuOption)
    except ValueError:
        keepDirTreeUp()
        print('That\'s not what I expected. Try Again')
        systime.sleep(3)
        startMenu()

    return menuOption


def fileHandeling(menuOption):
    ''' Handels everything to do with files '''

    if menuOption == 1:
        pass
    elif menuOption == 2:
        pass
    elif menuOption == 3:
        deleteExam(menuOption)
    elif menuOption == 4:
        pass
    elif menuOption == 5:
        pass
    elif menuOption == 6:
        pass
    elif menuOption == 7 or menuOption in menuOption_Quit:
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
            answer = input(
                f'\nIs \'{exam_Folder_Name}\' correct? (Y/N) :> ').upper()
            if answer in answerNo:
                keepDirTreeUp()
                continue
            elif answer in answerYes:
                os.mkdir(f'{exam_Folder_Name}')
                print(f'\n\'{exam_Folder_Name}\' has been made.')
                keepDirTreeUp()
                systime.sleep(3)
                break
            else:
                print('\nThat\'s not a correct answer!')
                keepDirTreeUp()
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


def deleteExam(menuOption):
    ''' Delete Exam Folder '''

    keepDirTreeUp()

    while True:
        try:
            print('Which folder(s) do you want to delete?\n')

            delDir = {}
            for num, item in enumerate(os.listdir(os.getcwd()), 1):
                delDir[num] = item
                print(str(num) + '. ' + item)

            folderNr = int(input('\n:> '))
            if folderNr in range(1, (len(delDir)) + 1):
                # if not loop through files en remove them
                # then remove folder itself

                # Change working directory to user's chosen path.
                os.chdir(f'{os.getcwd()}/{delDir[folderNr]}')

                # If chosen folder is NOT empty
                folderNotEmpty = len([f for f in os.listdir(os.getcwd())])

                if folderNotEmpty > 0:
                    print(
                        f'\nDirectory: \'{delDir[folderNr]}\' is not empty!\n')

                    keepDirTreeUp(None, f'{delDir[folderNr]}')
                    # print(f'Files found in \'{delDir[folderNr]}\' directory')
                    # for num, item in enumerate(os.listdir(os.getcwd() + '/' + f'{delDir[folderNr]}'), 1):
                    #     print('\t' + str(num) + '. ' + item)

                    try:
                        while True:
                            answer = int(
                                input(f'1. Delete Directory: \'{delDir[folderNr]}\'?\n2. Delete Files?\n\n3. Back\n\n:> '))
                            if answer == 1:
                                keepDirTreeUp(None, f'{delDir[folderNr]}')

                                # Delete's files in chosen folder.
                                for files in os.listdir(os.getcwd()):
                                    os.remove(f'{os.getcwd()}/{files}')

                                    # Change directory one lvl up to..
                                    os.chdir(os.path.dirname(os.getcwd()))

                                # ..delete chosen folder itself.
                                os.rmdir(f'{os.getcwd()}/{delDir[folderNr]}')

                                # Show Deleting Animation.
                                loadingAnimation(
                                    f'DELETING \'{delDir[folderNr]}\'.. ', None, 15, .05)

                                keepDirTreeUp()
                                startMenu()
                                break
                            elif answer == 2:
                                keepDirTreeUp(
                                    None, f'{delDir[folderNr]}')

                                # Creates a dict of files inside current working directory
                                delFile = {}
                                for num, files in enumerate(os.listdir(os.getcwd()), 1):
                                    delFile[num] = files
                                    print(str(num) + '. ' + files)

                                # If there are more the 5 file in directory, speed up animation.
                                if len(delFile) > 5:
                                    vector = 10     # Used for nr animation dispay
                                    time = .01      # Used for systime.sleep between animations
                                else:
                                    vector = 15     # Used for nr animation dispay
                                    time = .05      # Used for systime.sleep between animations

                                while True:
                                    try:
                                        # If there's only 1 file in the directory
                                        if len([f for f in os.listdir(os.getcwd())]) == 1:
                                            fileNr = 1
                                            answer = input(
                                                f'DELETE \'{delFile[fileNr]}\'? (Y/N) :> ').upper()
                                        else:
                                            # When there are more then one file in the directory
                                            try:
                                                fileNr = int(input(
                                                    '\nDelete which file(s)?\n--Type \'0\' for All--\n\n:> '))
                                                keepDirTreeUp(
                                                    None, f'{delDir[folderNr]}')
                                            except ValueError:
                                                fileNr = 0

                                            if fileNr == 0:
                                                for num, file in delFile.items():

                                                    # Animation function
                                                    loadingAnimation(
                                                        f'DELETING.. \'{delFile[num]}\'.. ', None, vector, time)

                                                    # Removing files from the directory. Via this for loop, removes them all.
                                                    os.remove(
                                                        os.getcwd() + '/' + f'{file}')
                                                    keepDirTreeUp(
                                                        None, f'{delDir[folderNr]}')
                                                
                                                # Change current working directory to My_Exam folder.
                                                os.chdir(os.path.dirname(os.getcwd()))
                                                keepDirTreeUp()

                                                print(f'\nAll files has been deleted!')
                                                systime.sleep(5)

                                                # Back to Menu                                               
                                                startMenu()
                                            else:
                                                keepDirTreeUp(
                                                    None, f'{delDir[folderNr]}')

                                                answer = input(
                                                    f'\nDELETE \'{delFile[fileNr]}\'? (Y/N) :> ').upper()

                                                if answer in answerNo:
                                                    keepDirTreeUp(
                                                        None, f'{delDir[folderNr]}')
                                                    continue
                                                else:

                                                    keepDirTreeUp(
                                                        None, f'{delDir[folderNr]}')
                                                    os.remove(
                                                        f'{os.getcwd()}/{delFile[fileNr]}')
                                                    # Animation function
                                                    loadingAnimation(
                                                        f'DELETING.. \'{delFile[num]}\'.. ', None, vector, time)

                                        # keepDirTreeUp(
                                        #     None, f'{delDir[folderNr]}')

                                        # Program Flow
                                        if answer in answerNo:
                                            keepDirTreeUp(
                                                None, f'{delDir[folderNr]}')
                                            continue
                                        elif answer in answerYes:
                                            keepDirTreeUp(
                                                None, f'{delDir[folderNr]}')

                                            # Show Deleting Animation.
                                            loadingAnimation(
                                                f'DELETING \'{delFile[fileNr]}\'.. ', None, 15, .05)

                                            # Removing file
                                            os.remove(
                                                os.getcwd() + '/' + f'{delFile[fileNr]}')
                                            keepDirTreeUp(
                                                None, f'{delDir[folderNr]}')
                                            
                                            print(
                                                f'\n\'{delFile[fileNr]}\' has been deleted!\n\nNOW WHAT?')
                                            startMenu()
                                            break

                                    except ValueError:
                                        keepDirTreeUp()
                                        print('This the one')
                                        systime.sleep(10)
                                        continue

                    except ValueError:
                        keepDirTreeUp()
                        print('This the two')
                        systime.sleep(10)
                        continue

        except ValueError:
            keepDirTreeUp()
            print('This the three')
            systime.sleep(10)
            continue

    return answer


def keepDirTreeUp(dirPath=None, dirName=None):
    ''' Shows Directory Tree to User '''

    sys_clear()

    if dirPath is None:
        dirPath = os.getcwd()

    if dirName is None:
        print('\nYour Directory Tree\n')
    else:
        print(f'\nDirectory Tree: \'{dirName}\'\n')

    print('-' * (len([f for f in os.listdir(dirPath)]) + 6))
    ##########################################################
    #  Credits to User Adam on StackOverFlow. !Link Below!   #
    ##########################################################
    paths = DisplayablePath.make_tree(Path(dirPath))         #
    for path in paths:                                       #
        print(path.displayable())                            #
    ##########################################################
    print('-' * (len([f for f in os.listdir(dirPath)]) + 6) + '\n')


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
