magicians = ['alice', 'david', 'carolina']
#print(magicians)

#for magician in magicians:
#    print(magician)

#for value in range(1, 101):
#    print(value)

oneToHigh = list(range(1, 1000001))
#for value in oneToHigh:
#    print(value)

#print(sum(oneToHigh))

odd_numbers = list(range(1, 21, 2))
#for value in odd_numbers:
#    print(value)

multiple_of_3 = list(range(3, 31, 3))
#for value in multiple_of_3:
#    print(value)
squares = []
cubes = list(range(1, 11))
'''for value in cubes:
    square = value**2
    squares.append(square)

print(squares)
'''
squares = [value**2 for value in cubes]
#print(squares)

oneToTwenty = list(range(1, 21))
#for value in oneToTwenty:
#    print(value)
#for value in oneToTwenty[0:4]
#    print('First 3 items in this list are ' + value)
'''
#SLICE
print('First 3 items in list are \n')
print(oneToTwenty[0:4])

print('3 items in the middle of the list are ')
print(oneToTwenty[6:10])

print('the last 3 items in the list are ')
print(oneToTwenty[-3:])
'''

'''
COPY A LIST
'''
'''
pizza = ['pepperoni', 'sausage', 'plain', 'chicken']
print(pizza)
pizza_copy = pizza[:]
pizza_copy.append('margarita')
print(pizza_copy)
'''
'''
TUPLE
'''
foods = ('carrot', 'spaghetti', 'chicken', 'coconuts', 'beets')
for value in foods:
    print(value)

print('\n')
#foods[2] = 'lettuce'

foods = ('carrot', 'pasta', 'chicken', 'quinua', 'beets')
for value in foods:
    print(value)
