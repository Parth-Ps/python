# def factorial(n):
#     ''' return n!'''
#     return 1 if n < 2 else n * factorial(n - 1)


# print(factorial(10))

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)
plt.plot(x, np.sin(x))
plt.show()