# 704 Binary Search

def search(nums, target):
    l,r = 0, len(nums)-1

    while l <= r:

        m = (l+r) // 2 # or l+((r-l)//2) to prevent overflow

        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m-1
        else:
            return m
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(search(nums,target))

def binary(nums,target):
    l,r = 0, len(nums)-1
    target= target
    def recursion(nums, target,l,r):
        m = (l+r)//2
        if l > r:
            return -1
        elif nums[m] == target:
            return m
        elif nums[m] > target:
            return recursion(nums,target,l,m-1)
        elif nums[m] < target:
            return recursion(nums,target,m+1,r)
    return recursion(nums, target,l,r)
print(binary(nums,target))

    