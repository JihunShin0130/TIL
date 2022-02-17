# 내 생각
"""
nums = [1, 5, 77, 26 ,33, 2, 6, 16, 55]

nums.sort()

min_num = nums[0]

print(min_num)
"""

# 제약조건 => 0-99

nums = [1, 5, 77, 26 ,33, 2, 6, 16, 55]

max_num = -1
min_num = nums[0]
for number in nums:
    if max_num < number:
        max_num = number
    if min_num > number:
        min_num = number

print(max_num)
print(min_num)
