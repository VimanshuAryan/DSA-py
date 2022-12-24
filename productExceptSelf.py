# 238

nums = [1,2,3,4]

def productExceptSelf(nums):
    # res = [1,1,1,1]
    res = [1] * len(nums)
    prefix = 1
    postfix = 1
    
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        # print(res, prefix)
    
    for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

print(productExceptSelf(nums))