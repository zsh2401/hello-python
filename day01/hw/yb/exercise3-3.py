'''
Name:YB
Time:2020.8.2
'''

#3-8
#随机5个地方
places = ['KunMing', 'ChengDu', 'ShangHai', 'BeiJing', 'GuiLing']
print(places)

#排序，不改变原来变量
sortedplaces = sorted(places)
print(sortedplaces)

#核实没有改变变量
print(places)

#反排序并且不修改变量
sortedplaces.reverse()
print(sortedplaces)

#核实没有修改变量
print(places)

#改变变量，反排序
places.reverse()
print(places)

#再次改变，和最初一样
places.reverse()
print(places)

#修改正常排序
places.sort()
print(places)

#修改反排序
places.reverse()
print(places)
print("\n")

#3-9
names = ['YB', 'LHL', 'ZSH2401']
lenght = len(names)
print(lenght)
print("\n")

#3-10
nums = [5,6,3,0]

#打印列表
print(nums)

#访问元素
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])

#使用元素
msg = "I have " + str(nums[0]) +  " fingers"
print(msg)

#修改元素
nums[0] = 1
print(nums)

#添加，插入，删除元素
nums.append(1)
print(nums)

nums.insert(2,4)
print(nums)

del nums[-2]
print(nums)

#弹出
popnums = nums.pop(1)
print("I have " + str(popnums) + " RMB")
print(nums)

#根据值删除元素
nums.remove(1)
print(nums)

#临时排序
sortednums = sorted(nums)
print(sortednums)
print(nums)

#永久性排序
nums.sort()
print(nums)

#反排序
nums.reverse()
print(nums)

#确定长度
lenght = len(nums)
print(lenght)






