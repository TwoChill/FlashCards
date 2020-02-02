import base
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

# Create a Main Folder
parent_Folder_Name, parent_Folder_Path = base.createMain()

# !! Currently Working On !!
# Menu
menuOption = base.startMenu(parent_Folder_Path)
