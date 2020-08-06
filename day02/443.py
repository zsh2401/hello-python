nums = [1231,6,12,5,9,56,5675]
nums2 = nums
print(nums)
print(nums2)
nums.append(2401)

print(len(nums))
print(len(nums2))

copiedNums = nums[:]
copiedNums.append(1937)

print(len(copiedNums))
print(len(nums2))