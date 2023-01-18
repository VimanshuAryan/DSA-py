# 150 
# stack
# Reverse Polish Notation
# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
def rvn(tokens):
    stack = []
    res = 0
    for n in tokens:
        if n not in '+-*/':
            stack.append(int(n))
        else:
            if n == '+':
                res = stack.pop() + stack.pop()              
            elif n == '-':
                res = stack.pop(-2) - stack.pop()
            elif n == '*':
                res = stack.pop() * stack.pop()               
            else:
                res = int (stack.pop(-2) / stack.pop())
            stack.append(res)
    return stack.pop()
print(rvn(tokens))

def rpn(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
    return stack[0]