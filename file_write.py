filename = 'write.txt'

#the 'w' as a parameter will erase contents when you open file, so be careful
'''
with open(filename, 'w') as file_object:
    file_object.write('i love programming baby')
'''

#append mode 'a'
'''
with open(filename, 'a') as file_object:
    file_object.write('i love programming baby \n')
    file_object.write('it really gets me going\n')
'''

while True:
    name = input('what is your name')
    with open('guest.txt', 'a') as file_object:
        file_object.write(name + '\n')
        print('hello ' + name + ' you have been added to our guestlist')
