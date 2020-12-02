import os

os.chdir('Files')
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_num, f_course = file_name.split('-')

    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    new_name = '{}-{}{}'.format(f_num, f_course, file_ext)

    os.rename(f, new_name)
