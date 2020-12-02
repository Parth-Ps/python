# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#  ......  Copy list to another...
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# my_list = []
# for n in nums:
#     my_list.append(n * n)
# print(my_list)

# my_list = [n * n for n in nums]
# print(my_list)

# using a map + lambda
# my_list = map(lambda n: n * n, nums)
# print(my_list)

# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)

# my_list = filter(lambda n: n % 2 == 0, nums)
# print(my_list)


# my_list = []
# for letter in 'abcd':
#     for num in nums:
#         my_list.append((letter, num))
# print(my_list)

# my_list = [(letter, num) for letter in 'abcd' for num in range(1, 5)]
# print(my_list)

# names = ['Bruce', 'Clark', 'Peter', 'Logan']
# heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine']

# print(zip(names, heroes))

# create dictories from two list..
# my_dict = {}
# for name, hero in zip(names, heroes):
#     my_dict[name] = hero
# print(my_dict)

# for i, j in my_dict.items():
#     print(i + " -> " + j)

# my_dict = {name: hero for name, hero in zip(names, heroes)}
# print(my_dict)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_set = set()
# for n in nums:
#     my_set.add(n)
#     print(n)

# my_set = {n for n in nums}
# print(my_set)


# Generator Expressions

# I want to yield n*n for each in 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def gen_func(nums):
#     for n in nums:
#         yield n * n


# my_gen = gen_func(nums)

# for i in my_gen:
#     print(i)


my_gen = (n * n for n in nums)

for i in my_gen:
    print(i)
