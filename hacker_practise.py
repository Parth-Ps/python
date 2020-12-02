'''
student = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Bakriti', 41]]

second_highest = sorted(list(set([marks for name, marks in student])))[1]
print('\n'.join([a for a, b in sorted(student) if b == second_highest]))

# print(i, " | ", j)
'''
#combo = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x == y]

# print(combo)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in matrix:
    print(i)
print("---------------------")
x = list(zip(*matrix))
for i in x:
    print(i)
# square = list(map(list(zip(*matrix), matrix)))
# print(square)
