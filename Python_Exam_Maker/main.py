import base

# Create a Main Folder
parent_Folder_Path = base.createMain()

# !! Currently Working On !!
# Menu
menuOption = base.startMenu()

# # Create a Exam Folder and File
# exam_Folder_Name, exam_Folder_Path = base.createExam(parent_Folder_Path)

#
# base.fileHandeling(menuOption)

##################################################
######## To create more files for testing ########
##################################################

# import os

# os.chdir(f'{os.getcwd()}/My_Exams/3')

# num = 101
# for i in range(1, num):
#     with open(f'{i}.py', 'w+', encoding="utf-8") as f:
#         string = 'print'
