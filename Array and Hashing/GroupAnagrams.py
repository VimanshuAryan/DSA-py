# 49
# Group Anangrams
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
def group (strs):

    res = defaultdict(list)

    for s in strs:

        count = [0] * 26

        for c in s:

 # The ord() function returns the number representing the unicode code of a specified character.

            count[ord(c) - ord('a')] += 1
            
        # list count is not hashable hence tuple(count)
        # res[tuple(count)] = s will store only one value per key hence append
        # we are appending to the list which is used as a value in dict, we're not appending to the dict directly.
        
        res[tuple(count)].append(s)

    return res.values()

print(group(strs))

