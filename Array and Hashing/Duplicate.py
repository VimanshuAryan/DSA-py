# 217 
# Given an integer array nums, return true if any value appears at least twice in the array
# and return false if every element is distinct.
nums = [1,2,3,1]
def containesDuplicate(nums):

    dict = {}

    for n in nums:
        if n not in dict:
            dict[n] = 1
        else:
            return True
    return False

print(containesDuplicate(nums))

def duplicate(nums):

    return len(set(nums)) != len(nums)
print(duplicate(nums))