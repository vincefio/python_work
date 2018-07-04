print('hello python world!')

name = 'Vince fiorilli'
print(name.title() + '!')

nameList = ['Vince', 'Chris', 'Carol', 'Joe']

#print(nameList[0])
#print(nameList[1])
nameList[0] = 'Superman'
print(nameList)

cantCome = 'Chris'
nameList.remove(cantCome)
print(nameList)

nameList.insert(2, 'cookoo')
print(nameList)

nameList.pop()
print(nameList)

print('length ' + str(len(nameList)))
