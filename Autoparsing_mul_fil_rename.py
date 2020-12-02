import os

os.chdir('/home/rhuk/Documents/python/Autoparsing_rename_multiple_file')
print(os.getcwd())
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    f_title, f_course, f_num = file_name.split('-')

    # f_title = f_title.strip()
    # f_course = f_course.strip()
    # f_num = f_num.strip()

    new_name = '{} {}{}'.format(f_num[1:].zfill(2), f_course, file_ext)
    os.rename(f, new_name)
