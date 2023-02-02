# 344 Reverse String in O(1) memory no extra memory
s = ["h","e","l","l","o"]
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0, len(s)-1
        
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l+=1
            r-=1
        return s
# reverse a string without affecting 0-9
def reverse(st):
    temp = [""] * len(s)
    x=0
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            temp[x] = s[i]
            x+= 1
    rev(temp,0,x)
    lst = list(s)
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            lst[i] = temp[x]
            x+= 1
    revStr = ""
    for i in range (len(s)):
        revStr += lst[i]


