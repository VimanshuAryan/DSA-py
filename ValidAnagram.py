# 242 
# Hashmap

s = "anagram"
t = "nagaram"

dict = {}

if len(s) != len(t):
    print(False)

for letter in s:
    if letter not in dict:
        dict[letter] = 1
    else:
        dict[letter] += 1

for letter in t:
    if letter in dict:
        dict[letter] -= 1
    else:
        print(False)
for key in dict:
    if dict[key] != 0:
        print(False)
print(True)