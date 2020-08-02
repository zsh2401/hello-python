# 创建
nums = [1,2,3,4,5,6,10,9,8,7]
print(nums)

# 设置已存在位置的值
nums[-2] = 2401
print(nums);

# 在nums的末尾添加元素： 343
nums.append(7 ** 3);
print(nums);

# 在nums的0下标位置插入元素：2401
nums.insert(0,7 ** 4);
print(nums);

# 删除下标为0的元素 （根据下标删除）
del nums[0]
print(nums);

# 删除nums中所有为10的元素（根据内容删除）
nums.remove(10);
print(nums);


'''
将某个元素弹出
什么意思？
获取指定的元素
并将其从原本的列表中移除
poped = nums[-1]
del nums[-1]
'''
poped = nums.pop(-1) # 不传入参数，默认-1，也可传入其他合法的下标数字，以弹出指定位置的元素
print(poped); #
print(nums); #
