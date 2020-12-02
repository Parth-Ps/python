num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fun_gen(num):
    for n in num:
        yield n * n


my_gen = fun_gen(num)

for i in my_gen:
    print (i)

    
# my_gen = (n*n for n in num)
# for i in my_gen:
#     print i
# my_list = []
# for n in num:
#     my_list.append(n)
# print my_list

# my_list = [n for n in num]
# print my_list

# my_list = [n for n in num if n % 2 == 0]
# print my_list

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print my_list


# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print my_list

# names = ['Bruce', 'clark', 'peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print my_dict

# my_dict = {name: hero for name, hero in zip(names, heros)}
# print my_dict
