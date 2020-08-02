'''
Name:YB
Time:2020.8.2
'''

#3-4 Name
names = ['YB' , 'LHL' , 'ZSH2401']

print(str(names) + " can come")

#3_5 Replace
print(names[0] + " can't come")

names[0] = 'YH'
print(str(names) + " can come" )

#3-6 Add
print("I found a big table")

names.insert(0 , 'MY')
names.insert(2, 'HXY')
names.append('TMC')

print(str(names) + " can come")

#3-7
print("only two people to come")
firstname = names.pop(0)
secondname = names.pop(0)
thirdname = names.pop(0)
fourthname = names.pop(0)

print(firstname + " can't come")
print(secondname + " can't come")
print(thirdname + " can't come")
print(fourthname + " can't come")
print(names[0] + " can come")
print(names[1] + " can come")

del names[0]
del names[0]

print(names)