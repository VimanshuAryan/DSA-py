#inorder recursion

def inorder(root):

    res = []
    if root:

        inorder(root.left)
        res.append(root)
        inorder(root.right)

    return res

inorder(root)

#preorder recursion

def preorder(root):

    res = []
    if root:

        res.append(root)
        preorder(root.left)        
        preorder(root.right)

    return res

preorder(root)

#postorder recursion

def postorder(root):

    res = []
    if root:

        postorder(root.left)        
        postorder(root.right)
        res.append(root)

    return res

postorder(root)

