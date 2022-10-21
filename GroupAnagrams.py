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

        res[tuple(count)].append(s)

    return res.values()

print(group(strs))