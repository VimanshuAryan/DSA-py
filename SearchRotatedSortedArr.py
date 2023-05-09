# Search in Rotated Sorted Array
# 33 medium facebook

def search(nums, target):
    l,r = 0,len(nums)-1

    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif (nums[m] >= nums[l] and target < nums[m] and nums[l] <= target) or not (nums[m] <= nums[r] and target > nums[m] and target <=nums[r]):
            r = m-1
        else:
            l = m+1
    return -1