from pathlib import Path
import base
import os

# Listdr will let you know everything that is in a directory.
from os.path import isfile, join
from os import listdir

base.sys_clear()

fileExtention = '.txt'
filePath = str(Path(__file__).absolute())
fileExt = filePath[len(filePath) - 3:]
directoryPath = os.path.dirname(os.path.abspath(__file__))
scriptName = filePath[(len(directoryPath) + 1):-len(fileExtention)]
parentPath = os.path.abspath(os.path.join(directoryPath, os.pardir))
parentPath2 = os.path.abspath(os.path.join(parentPath, os.pardir))
parentName = parentPath[(len(parentPath2) + 1):]
directoryPathName = directoryPath[(len(parentPath) + 1):]
examFolder = directoryPath + '/' + os.listdir(directoryPath)[-1]
dirList = [f for f in os.listdir(directoryPath)]
parentPathName = parentPath[(len(parentPath2) + 1):]
chd = os.chdir(f'{base.getScriptInfo(Path(__file__))[3]}')
dirList2 = [f for f in dirList]
now = os.getcwd()




print('filePath:\t', filePath)
print('fileExtention:\t', fileExtention)
print('directoryPath:\t', directoryPath)
print('scriptName:\t', scriptName)
print('parentPath', parentPath)
print('parentPath2', parentPath2)
print('parentPathName:', parentPathName)
print('directoryPathName:', directoryPathName)
print('examfolder', examFolder)
print('dirList', dirList)
print('dirList2', dirList2)
print('now', now)


# Makes a string of this file's filepath.
filePath = str(Path(__file__).absolute())

# Gets the file extention as a string (via string slicing).
fileExtention = filePath[len(filePath) - 3:]

# Gets the directoryPath as a string.
directoryPath = str(os.path.dirname(os.path.abspath(__file__)))


#######################################################################################################
