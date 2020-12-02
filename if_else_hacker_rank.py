N = 22
if N % 2 == 0:
    if N in range(2, 5) or N > 20:
        print("Not Weird")
    elif N in range(6, 20):
        print("Weird")
else:
    print("weird")
