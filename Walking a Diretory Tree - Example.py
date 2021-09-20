import os

folder = 'C:\\Users\\Bruna Ramos\\Downloads'

for folderName, subfolders, filenames in os.walk(folder):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + 'are: ' + str(subfolders))
    print('The filenames in ' + folderName + 'are: ' + str(filenames))
    print()
