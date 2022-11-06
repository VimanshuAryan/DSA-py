# 283
# Move zeroes

nums = [0,1,0,3,12]
def move(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            x = nums.pop(i)
            nums.append(x)
    print(nums)

move(nums)