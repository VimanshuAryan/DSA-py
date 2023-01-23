# stack backtracking 
# 22 Generate Paranthesis

def genp(n):
    stack = []
    res = []

    def backtrack(openN, closedN):

        if openN == closedN == n:
            res.append("".join(stack))

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop() #why pop
        
        if closedN < openN :
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
    
    backtrack(0,0)
    return res