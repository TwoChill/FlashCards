import base
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

# Create a Main Folder
main_Folder_Name, main_Folder_Path = base.createMain()

# !! Currently Working On !!
# Menu
menuOption = base.startMenu(main_Folder_Path)
