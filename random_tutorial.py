import random

# value = random.randint(1, 10)
# value = random.uniform(1, 10)

# greeting = ['Hi', 'Hello', 'listen', 'Hey', 'Dear']
# value = random.choice(greeting)
# print(value + ', Warrior')

deck = list(range(1, 52))
# random.shuffle(deck)
hand = random.sample(deck, k=5)
print (hand)
