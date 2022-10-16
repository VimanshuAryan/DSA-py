# 20 
# Stack question

s = "()[]{}{"
stack = []
hashmap = dict(('()', '[]', '{}'))

for p in s:
    if p in '([{':
        stack.append(p)
    elif len(stack) == 0 or p!= hashmap[stack.pop()]:
        print(False) 
print(len(stack) == 0)


