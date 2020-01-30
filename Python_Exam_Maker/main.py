import base

# Create a Main Folder
parent_Folder_Path = base.createMain()

# Menu ()
menuOutput = base.startMenu()

# Create a Exam Folder and File
exam_Folder_Name, exam_Folder_Path = base.createExam(parent_Folder_Path)

# !! Currently Working On !!
base.fileHandeling(menuOutput)