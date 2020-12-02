# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i * i)
#     return result


# my_nums = square_numbers([1, 2, 3, 4, 5])

# List comprehension method
# my_nums = [x * x for x in [1, 2, 3, 4, 5]]
# print(my_nums)

# ...................TO CHANGE THE FUNCTION INTO GENERATORS..............
# It yield the result one at a time.Dont hold the result in a memory.


# def square_numbers(nums):
#     for i in nums:
#         yield i * i


# my_nums = square_numbers([1, 2, 3, 4, 5])
# for num in my_nums:
#     print(num)
