# from operator import attrgetter
#
#
# class Employee():
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def __repr__(self):
#         return '({},{},${})'.format(self.name, self.age, self.salary)
#
#
# e1 = Employee('Carl', 37, 70000)
# e2 = Employee('sarah', 20, 80000)
# e3 = Employee('John', 50, 90000)
#
# employee = [e1, e2, e3]
#
#
# # def e_sort(emp):
# #     return emp.salary
#
#
# # reverse = True
# s_employee = sorted(employee, key=attrgetter('age'))
# # s_employee = sorted(employee, key=lambda e: e.age)
#
# print(s_employee)
person = {'name': 'Jean', 'age': 67}
list = ['Peter', 34]

# sentence = 'Myself ' + person['name'] + ' age : ' + str(person['age'])
# sentence = 'My name is {} age :{} .'.format(person['name'], person['age'])
# print(sentence)
sentence_list = 'Dear {0[0]} Your Id is {0[1]}'.format(list)
sentence = 'I am {0} and age is {1}'.format(person['name'], person['age'])
sentence = 'MySelf {0[name]} and age is {0[age]}'.format(person)
print (sentence)
print(sentence_list)

person_list = {'name': 'Wade', 'roll': 36}
say = 'Listen {name} Your Enroll is {roll}'.format(**person_list)
print (say)

for i in range(1, 13):
    says = 'The value is : {:02}'.format(i)
    print(says)
pi = 3.14159265
pi = 'Value equal to {:.3f}'.format(pi)
print pi
