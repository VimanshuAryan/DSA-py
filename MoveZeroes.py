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

# quick sort algo

def move2(nums):

    l = 0

    for r in range(len(nums)):
        if nums[r] != 0:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
    return nums

print(move2(nums))