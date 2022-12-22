# 128 medium google

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its start of a sequence, don't do anything otherwise
            if (n-1) not in numSet:
                length = 0
                while (length + n) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest