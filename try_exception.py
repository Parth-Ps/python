# try:
#     f = open('curruptfile.txt')
#     # if f.name == 'currupt_file.txt':
#     #     raise Exception
# except IOError as e:
#     print('First!')
# except Exception as e:
#     print('Second')
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Executing Finally...")

# print('End of program')


try:
    f = open('testfile.txt')
except Exception:
    print('File Doesn\'t exist')
