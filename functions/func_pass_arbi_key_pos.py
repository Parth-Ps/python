def student_info(* arg, **krg):
    print(arg)
    print(krg)


course = ['math', 'phy', 'chem']
info = {'name': 'Misa', 'age': 20}

student_info(*course, **info)
