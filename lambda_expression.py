def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(45)
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]
pairs.sort(key=lambda pair: pair[1], reverse=True)
print(pairs)
