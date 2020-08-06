'''
Time:2020.8.6
Name:YB
'''
names = ['YB', 'LHL', 'ZSH']

#创建副本
friend_names = names[:]

#原来中加入一个元素
names.append('YH')

#副本中加入一个元素
friend_names.append('MY')

#核实列表不同
for name in names:
    print("My friends are : " + name)
for friend_name in friend_names:
    print("My friend's friends are :" + friend_name)
