# Sliding window maximum
# 239

nums = [1,3,-1,-3,5,3,6,7]
k = 3

#Gives the right solution but time limit exceeded
def window(nums,k):
    
    res = []
    window = []

    #sliding window initialize
    l=0
    for r in range(k, len(nums)+1):

    #calc max value and append it to res
        window = sorted(nums[l:r])
        
        res.append(window[-1])
        
    #inc r ptr, pop l ptr value, inc l ptr
        l += 1
    return res
print(window(nums,k))

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque 
        output = []
        q = deque()
        l,r = 0,0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output



