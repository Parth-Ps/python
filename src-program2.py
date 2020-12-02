# for sum of negative number
given_list = [5, 4, 3, 2, 1, -3, -4, -5]

total = 0
j = len(given_list) - 1
while given_list[j] < 0:
    total += given_list[j]
    j -= 1
print("sum of negative number is : ", total)

# for sum of positive number
a = [5, 4, -2, -3]

total1 = 0
for i in range(len(a)):
    if a[i] > 0:
        total1 += a[i]
        i += 1
print("Sum of all negative number is : ", total1)

# pop the negative number
b = [1, 2, 3, 4, -5, 0, -4, -3, -2, -1, 6, 7, 8, 9]

for c in range(len(b)):
    if b[c] > 0:
        print("Display positive Number : ", c, "at address", b[c])
        c += 1
