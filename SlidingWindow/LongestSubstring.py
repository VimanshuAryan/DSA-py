#3 longest substring
# optimal soln

def long(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):

        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
            
        charSet.add(s[r])
        res = max(res, r-l+1)
    return res

# def long(s):
#     dict = {}
#     l,r = 0,0
#     res = 0

#     while r < len(s): 

#         if s[r] in dict:
#             l = r
#             dict.clear()

#         dict[s[r]] = 1
#         res = max(res, r-l+1)
#         r += 1
#     return res
# s = "abcabcbb"
# t = 'bbbb'
# u = " "
# # absolutely can not work for this testcase. The sliding window method is superior because of cases like this"
# v = "dvdf" 
# print(long(v))