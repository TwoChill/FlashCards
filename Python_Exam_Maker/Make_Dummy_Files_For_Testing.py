import os

# Change to directory of this file.
ThisFilesPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(ThisFilesPath)

NewFileName = 'Test_For_Delete_Option_3'

try:
    os.mkdir(NewFileName)

    # Number of dummy-files
    num = 25

    for i in range(1, num):
        with open(f'{i}.py', 'w+', encoding="utf-8") as f:
            string = 'print'
except FileExistsError:
    pass


print('Dummy Files Made!')
