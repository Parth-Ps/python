import os

os.chdir('/home/ryuk/Documents/python/Automation/Files')

print(os.getcwd())
for i in os.listdir():
    file_name, f_ext = os.path.splitext(i)
    # print(file_name.split('-'))
    f_title, f_course, f_num = file_name.split('-')
    # print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
    # for Removing white spaces in file name
    f_title = f_title.strip()
    f_course = f_course.strip()
    # .zfill() method turn number to 2 digit number
    f_num = f_num.strip()[1:].zfill(2)
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    print(new_name)
    os.rename(i, new_name)
