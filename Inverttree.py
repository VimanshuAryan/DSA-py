# 226 
# invert binary tree

def invert(root):

    if not root:
        return 0

    temp = root.right
    root.right = root.left
    root.left = temp 

    invert(root.right)
    invert(root.left)
    
    return root
