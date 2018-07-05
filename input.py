'''message = input('how many pe0ple are in your dinner group? ')
message = int(message)

if message > 8:
    print('youll have to wait for a table')
else:
    print('come right in!')
    '''
'''
active = True

while active:
    topping = input('Enter a pizza topping that you would like: ')
    if topping != 'quit':
        print('ok well add ' + topping)
    else:
        print('BYE')
        break
'''

sandwich_orders = ['ruben', 'pastrami', 'chicken', 'pastrami', 'roast beef', 'pastrami']
'''
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('current order is ' + current_sandwich)
    finished_sandwiches.append(current_sandwich)

print('finished sandwiches ' + str(finished_sandwiches))
print('sandwich orders ' + str(sandwich_orders))
'''
'''
print('the deli has run out of pastrami ')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
'''
polling_active = True
responses = {}

while polling_active:
    name = input('what is your name ')
    response = input('where would you like to go ')

    responses[name] = response

    if name == 'quit':
        polling_active = False
print(responses)
