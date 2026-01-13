#1 Remove duplicates (preserve order)
lst = [1,2,2,3,1,4]
res = []
for x in lst:
    if x not in res:
        res.append(x)
print(res)
#----------------------------------

#-2 Find 2nd / 3rd largest
nums = [15, 50, 5, 9, 20]
nums = sorted(set(nums), reverse=True)
print(nums[2])   # 3rd largest
#----------------------------------

# 3- Move all zeros to end
arr = [0,1,0,3,12]
result = [x for x in arr if x != 0] + [0]*arr.count(0)
print(result)
#------------------------------------------
# 4 Flatten nested list (single level)

data = [1, 2, [3, 4], 5, [6, 7, 8]]
result = []

for item in data:
    if isinstance(item, list):
        result.extend(item)
    else:
        result.append(item)

print(result)

#-------------------------------------------------
# 5 Even and odd numbers

nums = [1,2,3,4,5,6]
even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if x % 2 != 0]
print(even, odd)

#-----------------------------------------------

# 6 - Check list palindrome

  lst = [1,2,3,2,1]
print(lst == lst[::-1])

#---------------------------------
























