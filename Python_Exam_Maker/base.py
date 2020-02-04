import os
from os.path import isfile, join
import sys
import time as systime
import random
import platform
from pathlib import Path
import shutil

answerNo = ('N', 'NO', 'NEE')
answerYes = ('Y', 'YES', 'J', 'JA')
menuOption_Back = ('B', 'BACK', 'RETURN')
menuOption_Quit = ('Q', 'QUIT', 'STOP')
selectAll = ('A', 'ALL', 'EVERYTHING',
             'SELECT EVERYTHING', 'SELECT ALL', 'SELECT A')
exam_Folder_Name = None
subFolder = False
bottomPrintStatement_1 = 'Which \'Directory\' do you want to delete?\n'
bottomPrintStatement_2 = 'Create Exam Folder\n'
bottomPrintStatement_3 = ''
bottomPrintStatement_4 = f'Create sub-folder in \'{exam_Folder_Name}\'? (Y/N) :> '
bottomPrintStatement_5 = 'DELETE ALL FILES AND DIRECTORIES'


def startMenu(main_Folder_Path, quitOption=False):
    ''' Display Main Menu'''
    # Always's change to My_Exam's directory when Main Menu function is called
    os.chdir(f'{os.path.dirname(Path(__file__))}/My_Exams')

    # Keep Directory Tree and Clear Screen
    keepDirTreeUp(None, None, 'Menu\n')

    menuOptions = ['Create Folders', 'Rename Rename', 'Delete Folders',
                   'Create a New Exam File', 'Rename an Exam File', 'Delete an Exam File', 'Quit']

    # Print a numbered list of menu options on screen.
    for num, item in enumerate(menuOptions, 1):
        if item in menuOptions[-1:]:
            print('\n' + str(num) + '. ' + item)
        else:
            print(str(num) + '. ' + item)

    try:
        if quitOption == False:
            menuOption = int(input("\n:> "))
        else:
            # Won't stop to get an input; function loadingAnimation called, quits program.
            menuOption = 0

        # Control's functions for each menuOption's
        fileHandeling(menuOption, main_Folder_Path, '')
    except ValueError:

        # Keep Directory Tree and Clear Screen
        keepDirTreeUp()
        print('That\'s not what I expected. Try Again')
        systime.sleep(3)

        # Back to Main Menu
        startMenu(main_Folder_Path, quitOption=False)

    return menuOption, main_Folder_Path


def fileHandeling(menuOption, main_Folder_Path, examFolderName):
    ''' Handels everything to do with files '''

    if menuOption == 1:
        createExam(os.getcwd(), subFolder)
    elif menuOption == 2:
        pass
    elif menuOption == 3:
        deleteExam(menuOption, main_Folder_Path)
    elif menuOption == 4:
        pass
    elif menuOption == 5:
        pass
    elif menuOption == 6:
        pass
    elif menuOption == 7 or menuOption in menuOption_Quit:

        # Keep Directory Tree and Clear Screen
        keepDirTreeUp()

        # Load Quiting Animation because of quitOPtion = True
        startMenu(main_Folder_Path, quitOption=True)

        # Built-in print statement has a 'newline' built in which is used for replacing ':>' on screen.
        print('')
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
        main_Folder_Name = 'My_Exams'
        os.mkdir(f'{main_Folder_Name}')
    except FileExistsError:
        pass

    # Change directory to My_Exams
    os.chdir(os.getcwd() + '/' + main_Folder_Name)

    # Save directory path
    main_Folder_Path = os.getcwd() + '/' + main_Folder_Name

    return main_Folder_Name, main_Folder_Path


def createExam(getcwd, subfolder):
    ''' Create child folder and exam file '''

    # Change temporarily to another working directory. To display correct Directory Tree while creating subfolders.
    os.chdir(getcwd)

    try:
        while True:
            # Keep Directory Tree and Clear Screen
            keepDirTreeUp(getcwd, None, None)

            # !!! CREATE BACK OPTION and error handling with space
            if subfolder is True:
                exam_Folder_Name_2 = input('Sub-Folder Name? :> ')
            else:
                exam_Folder_Name_2 = input('Exam Folder Name? :> ')

            # Replaces whitespaces with underscores
            if ' ' in exam_Folder_Name_2:
                exam_Folder_Name_2 = exam_Folder_Name_2.replace(' ', '_')

            # Keep Directory Tree and Clear Screen
            keepDirTreeUp(getcwd, None, None)

            answer = input(
                f'Is \'{exam_Folder_Name_2}\' correct? (Y/N) :> ').upper()

            # To correctly show directory name in  Directory Tree: ***
            exam_Folder_Name = exam_Folder_Name_2

            if answer in answerNo:

                # Keep Directory Tree and Clear Screen
                keepDirTreeUp(getcwd, exam_Folder_Name, bottomPrintStatement_2)

                continue
            elif answer in answerYes:

                # Makes new Exam Directory
                os.mkdir(f'{exam_Folder_Name}')

                # # Change to new directory IF USR WANTS TO CREATE QandA IMIDITLY (def createQA)
                # os.chdir(f'{os.getcwd()}/{exam_Folder_Name}')
                # print('>> CWD:', os.getcwd())
                # systime.sleep(10)

                # Keep Directory Tree and Clear Screen
                keepDirTreeUp(getcwd, exam_Folder_Name, bottomPrintStatement_2)

                # Create sub-folder?
                createSubFolder(getcwd, exam_Folder_Name,
                                bottomPrintStatement_2)

                # Back to Main Menu
                startMenu(os.getcwd())
                break
            else:
                # Keep Directory Tree and Clear Screen
                keepDirTreeUp(None, None, bottomPrintStatement_2)

                print('That\'s not a correct answer!')
                systime.sleep(3)

                # Keep Directory Tree and Clear Screen
                keepDirTreeUp(None, None, bottomPrintStatement_2)

                continue

        exam_Folder_Path = f'{os.getcwd()}/{exam_Folder_Name}'
        print('>>> This is exam folder path:', exam_Folder_Path)
        systime.sleep(10)

        return exam_Folder_Name, exam_Folder_Path

    except FileExistsError:
        ''' Adds a randomnumber to existing folder name '''
        randomnr = str(random.randint(2, 100))

        try:
            # Create new 'duplicate' exam_Folder_Name
            os.mkdir(f'{exam_Folder_Name}_{randomnr}')
        except FileExistsError:
            randomnr += randomnr
            os.mkdir(f'{exam_Folder_Name}_{randomnr}')

        exam_Folder_Path = f'{os.getcwd}/{exam_Folder_Name}'

        # Ask usr to create a sub-folder
        createSubFolder(os.getcwd(), exam_Folder_Name, bottomPrintStatement_2)

        # Back to Main Menu
        startMenu(os.getcwd(), quitOption=False)

        return exam_Folder_Name, exam_Folder_Path

# menuOption will be used when splitting up DeleteFolder and Files


def deleteExam(menuOption, main_Folder_Path):
    ''' Delete Exam Folder '''

    # Keep Directory Tree and Clear Screen
    keepDirTreeUp(None, None, bottomPrintStatement_1)

    while True:
        try:
            # If My_Exam folder is empty..
            if len(os.listdir(os.getcwd())) == 0:

                # Show Searching Animation.
                loadingAnimation('Searching...', None, 15, .05)

                # Keep Directory Tree and Clear Screen
                keepDirTreeUp(None, None, bottomPrintStatement_1)

                print('No Exam(\'s) found!')
                systime.sleep(5)

                # Back to Main Menu
                startMenu(main_Folder_Path, quitOption=False)

            # If there's only 1 directory to remove
            elif len(os.listdir(os.getcwd())) == 1:

                folderName = [f for f in os.listdir(os.getcwd())]

                while True:
                    answer = input(
                        f'DELETE DIRECTORY: \'{folderName[0]}\'? (Y/N) :> ').upper()

                    if answer in answerNo:
                        keepDirTreeUp()
                        # Back to Main Menu
                        startMenu(os.getcwd(), quitOption=False)
                    elif answer in answerYes:
                        keepDirTreeUp()

                        answer = input(
                            f'ARE YOU SURE ABOUT DELETING: \'{os.listdir(os.getcwd())[0]}\'? (Y/N) :> ').upper()
                        if answer in answerNo:

                            # Keep Directory Tree and Clear Screen
                            keepDirTreeUp()

                            # Back to Main Menu
                            startMenu(os.getcwd())
                        elif answer in answerYes:

                            # Keep Directory Tree and Clear Screen
                            keepDirTreeUp()

                            # Removes directory and all files in them.
                            shutil.rmtree(os.getcwd())
                            break
                    else:
                        # Keep Directory Tree and Clear Screen
                        keepDirTreeUp()
                        continue

            else:
                # Create a dictionary and prints a list of folders inside current working directory.
                delDir = {}
                count = 1
                for num, item in enumerate(os.listdir(os.getcwd()), 1):
                    delDir[num] = item
                    print(str(num) + '. ' + "'" + item + "'")
                    count += 1

                # Delete ALL option
                print('\n' + str(count) + '. ' +
                      'DELETE ALL FILES AND FOLDERS')

                # Print Back option on screen.
                count += 1
                print('\n' + str(count) + '. ' + 'Back')

                while True:
                    try:
                        folderNr = int(input('\n:> '))

                        # If folderNr in range of the number of folders..
                        if folderNr in range(1, (len(delDir)) + 2):

                            # Change working directory to user's chosen path.

                            # If folderNr doesn't correspondent with a folder in the list
                            if (len(delDir) + 2) > folderNr < len(delDir):
                                os.chdir(f'{os.getcwd()}/{delDir[folderNr]}')

                            # Create dictionary of files in current working directory.
                            # Else delfile is a empty dict
                            delFile = {}
                            for num, files in enumerate(os.listdir(os.getcwd()), 1):
                                delFile[num] = files

                            # If there are more the 5 file in directory, speed up animation.
                            if len(delFile) > 5:
                                vector = 10     # Used for nr animation dispay
                                time = .01      # Used for systime.sleep between animations
                            elif len(delFile) > 10:
                                vector = 5     # Used for nr animation dispay
                                time = .01      # Used for systime.sleep between animations
                            else:
                                vector = 15     # Used for nr animation dispay
                                time = .05      # Used for systime.sleep between animations

                            # When ALL option is chosen
                            if folderNr == (count - 1):

                                # Keep Directory Tree and Clear Screen
                                keepDirTreeUp(
                                    None, None, bottomPrintStatement_5)

                                # Creates a dict of files inside current working directory
                                for num, files in delFile.items():
                                    print(f'{num}. \'{files}\'')

                                while True:

                                    # When there are more then one file in the directory
                                    fileNr = input(
                                        '\n' + bottomPrintStatement_5 + '? (Y/N) :> ').upper()
                                    if fileNr in answerNo:

                                        # Back to Main Menu
                                        startMenu(
                                            os.getcwd(), quitOption=False)

                                    elif fileNr in answerYes:

                                        # Keep Directory Tree and Clear Screen
                                        keepDirTreeUp(
                                            None, None, bottomPrintStatement_5)

                                        for num, file in delFile.items():

                                            # Show Deleting Animation.
                                            loadingAnimation(
                                                f'DELETING.. \'{delFile[num]}\'.. ', None, vector, time)

                                            # Removing directories and subdirectories
                                            shutil.rmtree(
                                                f'{os.getcwd()}/{file}')

                                            # Keep Directory Tree and Clear Screen
                                            keepDirTreeUp(
                                                None, None, bottomPrintStatement_5)

                                        # Keep Directory Tree and Clear Screen
                                        keepDirTreeUp(
                                            None, None, bottomPrintStatement_5)

                                        print(f'All files has been deleted!')
                                        systime.sleep(3)

                                        # Back to Main Menu
                                        startMenu(main_Folder_Path)
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
                                            main_Folder_Path)

                            # If chosen folder is NOT empty
                            folderNotEmpty = len(
                                [f for f in os.listdir(os.getcwd())])

                            if folderNotEmpty > 0:
                                print(
                                    f'\nDirectory: \'{delDir[folderNr]}\' is not empty!\n')

                                systime.sleep(3)

                                # Keep Directory Tree and Clear Screen
                                keepDirTreeUp(
                                    None, f'{delDir[folderNr]}', bottomPrintStatement_1)

                                # !!! Next answer should be a list created by a for loop wich also inclueds subfolders in list.
                                try:
                                    while True:
                                        # !!! put error tracebakc in except two,
                                        # !!! make a for loop to print and append string to  lst based on folders in map
                                        # !!! maby make a function that will check if theres more dirs and will create and append more lists..
                                        # Keep the last item in the list 'Back'
                                        lst = [
                                            f'Delete Directory: \'{delDir[folderNr]}\'?', 'Delete Files?', 'Back']

                                        # Print a numbered list on screen.
                                        for num, item in enumerate(list, 1):
                                            if item in lst[-1:]:
                                                print(
                                                    '\n' + str(num) + '. ' + item)

                                            else:
                                                print(str(num) + '. ' + item)
                                        answer = int(':> ')
                                        if answer == 1:

                                            # Keep Directory Tree and Clear Screen
                                            keepDirTreeUp(
                                                None, f'{delDir[folderNr]}')

                                            # Delete's files in chosen folder first.
                                            for files in os.listdir(os.getcwd()):
                                                os.remove(
                                                    f'{os.getcwd()}/{files}')

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
                                            startMenu(main_Folder_Path,
                                                      quitOption=False)
                                            break
                                        else:
                                            # Keep Directory Tree and Clear Screen
                                            keepDirTreeUp()

                                            print(
                                                '>> THIS SECTION HAS BEEN MOVED !!')

                                            # Back to Main Menu
                                            startMenu(main_Folder_Path,
                                                      quitOption=False)

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

                                        # Back to Main Menu
                                        startMenu(
                                            os.getcwd(), quitOption=False)
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
                                            f'\'{delDir[folderNr]}\' has been deleted!')

                                        systime.sleep(5)

                                        # Back to Main Menu
                                        startMenu(main_Folder_Path,
                                                  quitOption=False)
                                        break
                        else:
                            # Keep Directory Tree and Clear Screen
                            keepDirTreeUp()
                            print('>> Helaas')
                            systime.sleep(10)
                            # Back to Main Menu
                            startMenu(main_Folder_Path, quitOption=False)

                    except ValueError:

                        # Back to Main Menu
                        startMenu(main_Folder_Path, quitOption=False)
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


def createSubFolder(getcwd, examFolderName, bottomPrintStatement_NR):
    ''' Creates a new directory in current working directory '''

    while True:
        # Keep Directory Tree and Clear Screen
        keepDirTreeUp(getcwd, None, bottomPrintStatement_NR)

        answer = input(
            f'Create sub-folder in \'{examFolderName}\'? (Y/N) :> ').upper()

        if answer in answerNo:
            break
        elif answer in answerYes:
            # Call function: createExam with only a change in current working directory
            getcwd = f'{os.getcwd()}/{examFolderName}'

            # Create a new sub-folder
            createExam(getcwd, True)

            # Ask again
            continue
        else:
            # Keep Directory Tree and Clear Screen
            keepDirTreeUp(getcwd, examFolderName, bottomPrintStatement_NR)

            print('That\'s not a valid answer!')
            systime.sleep(3)

            continue


def keepDirTreeUp(dirPath=None, dirName=None, bottomStatement=None):
    ''' Shows Directory Tree to User with or without the Directory Name and/or printstatement at the bottom'''

    sys_clear()

    if dirPath is None:
        dirPath = os.path.dirname(Path(__file__)) + '/My_Exams'

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

    # If string, print string, else if function, call function.
    if type(bottomStatement) == 'str':
        print(bottomStatement)
    else:
        bottomStatement


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
