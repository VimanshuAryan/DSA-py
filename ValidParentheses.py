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

def valid(s):
    stack = []
    pairs = ['()','[]','{}']

    for paran in s:
        if stack and paran in '}])':
            pair = stack.pop() + paran
            print(pair)
            if pair not in pairs:
                return False
        else:
            stack.append(paran)
    return stack ==[]

s = "["
print(valid(s))

