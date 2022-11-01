# 101 symmetric tree 
# 100 Same tree 
# recursion

def checker(L, R):

    if not L and not R:
        return True
    if not L or not R or L.val != R.val:
        return False 
    return checker(L.left, R.right) and checker(L.right, R.left)

def symmetry(root):

    if not root:
        return True
    
    return checker(root.left,root.right)