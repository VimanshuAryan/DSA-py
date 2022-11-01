# binary tree inorder traversal
# 94 - iteration solution

def inorder(root):

    res = []
    stack = []
    # pointer cur
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val) 
        cur = cur.right
    
    return res