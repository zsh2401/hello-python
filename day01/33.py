cars = ["bmw","audi","toyota","subaru"]
print("Sources list:\n"+ str(cars));

cars.sort();
print(cars);

nums = [10,9,8,7,6]
sortedNums = sorted(nums); # 6 7 8 9 10
print(str(nums) + "\n" + str(sortedNums));

sortedNums.reverse();
print(sortedNums);

nums2 = [1,3,32,122,7,8,12123,1287869]

nums2.sort()
nums2.reverse()

#nums2.reverse();
# A : 1287869 12123 122 32 8 7 3 1
# B : 1287869 12123 8 7 122 32 3 1

# Error
nums2[len(nums2)]
#x = len(nums2) + 5
