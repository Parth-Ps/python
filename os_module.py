# import os
# # from datetime import datetime
# print (os.getcwd())
# os.chdir('/home/rhuk/Documents/python')
# print (os.getcwd())
# # path = '/home/rhuk/Documents/python'
# # file = os.listdir(path)
# # for file_1 in file:
# #     print file_1
# # os.mkdir
# # os.rmdir('Tame')
# # mod_time = os.stat('os_module.py').st_mtime
# # print (datetime.fromtimestamp(mod_time))

# # for dirpath, dirname, filename in os.walk('/home/rhuk/Documents/python'):
# #     print('Current Path:', dirpath)
# #     print('Directories', dirname)
# #     print('Files', filename)
# #     print()
# # print(os.environ.get("HOME"))

# file_path = os.path.join(os.environ.get("HOME"), 'test_test.txt')
# print(file_path)
# print(dir(os.path))

import os
from datetime import datetime

# print(dir(os))  # display attributes and mothod of os within the module..

# print(os.getcwd())

os.chdir('/home/ryuk/Documents/')  # change  current working directory

# print(os.getcwd())

# print(os.listdir())  # display files and folder on current working directory


# os.mkdir("Demo_folder")  # it only create single level folder and files

# It also create internal level folder ex:- /Demo/newFolder.This create folder Demo and then inside it create newFolder.
# os.makedirs('Demo/New_Folder')

# os.rmdir()  # It delete exactly one folder not sub folders
# os.removedirs()  # It delete sub folder including main folder.

# os.rename(" Orginal file name", "update file name ")

# To get information about files and folder

mod_time = os.stat('demo.txt').st_mtime
# print("The time is {:%B %d, %Y} ".format(datetime.fromtimestamp(mod_time)))

# print(datetime.fromtimestamp(mod_time))

# for finding files and directories on current location
# for dirpath, dirnames, filenames in os.walk('/home/ryuk/Documents/javascript'):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', dirnames)
#     print()

# To display Enviorment variable
# print(os.environ.get('HOME'))
# ........It create folder in Home directories..........
# ls = os.environ.get('HOME')
# print(os.getcwd())

# os.chdir(ls)
# print(os.getcwd())
# os.mkdir('sample.txt')

print(os.getcwd())
# file_path = os.path.join(os.environ.get('HOME'), 'tex.txt')
# print(file_path)

# print(os.path.split('/tmp/test.txt'))  # It split basename and dirname
# print(os.path.exists('/tmp/test.txt'))  # Check for existennce/tmp/test.txt'
# print(os.path.isdir('/tmp/wdwd'))
# print(os.path.isfile('/tmp/wdwd'))
# print(os.path.splitext('/tmp/test.txt'))  # To split extension

print(dir(os.path))
