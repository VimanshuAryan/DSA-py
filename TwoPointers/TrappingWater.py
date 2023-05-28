# 42 Trapping rainwater 
# my first hard question
#o(n) time o(n) memory
# input array 
# create a maxleft array and maxright array
# water units trapped = min(L,R) - height[i] at every instant and round up to zero

#O(1) memory - optimal

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    res = 0
    l,r = 0, len(height) -  1
    maxLeft, maxRight = height[l], height[r]

    while l < r:

        if maxLeft < maxRight:
            l += 1
            maxLeft = max(maxLeft, height[l])
            res += (maxLeft - height[l])
        else:
            r -= 1
            maxRight = max(maxRight, height[r])
            res += (maxRight - height[r]) 
    return res