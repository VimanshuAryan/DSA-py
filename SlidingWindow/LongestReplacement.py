# # sliding window
# # 424 longest repeating character replacement
# # O(26*n) time => O(n) but it still can be optimized further

s = "ABAB" 
k = 2
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
ans = Solution()
print(ans.characterReplacement("ABAB", 2))

# Optimized further to straight O(n) without using hashmap

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res

s = "ABBB"
k = 2

# I'm always assuming that the first letter is the letter with highest freq and thus other letters need change.
# That assumption is baseless and what will I do when the 1st letter needs to be changed
# The code needs to check what letter needs to be replaced
# s ="ABBB" doesnt work

# def substring(s,k):
#     l,res = 0,0
    
#     for r in range(len(s)):
#         if s[l] != s[r] and k>0:
#             k -=1
#         elif s[l] != s[r] and k==0:
#             l = r
#         res = max(res,r - l + 1)
#         r+=1
#         print(res)
#     return res

# print(substring(s,k))
