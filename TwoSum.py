#1 Two Sum
# O(n)

nums = [2,7,11,15]
target = 9

dict = {}
#initializing the hashmap
for i in range(len(nums)):
    dict[nums[i]] = i

for i in range(len(nums)):
    req = target - nums[i]
    
    if req in dict and dict[req] != i:
        print ([i, dict[req]])

#neetcode version

dict = {}
for i, n in enumerate(nums):
    req = target - n
    if req in dict:
        print([i, dict[req]])
    dict[n] = i
