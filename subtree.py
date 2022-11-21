# 572 subtree of another tree

def subtree(root, subroot):
    if not subroot:
        return True
    if not root:
        return False
    if sametree(root, subroot):
        return True
    return subtree(root.left, subroot) or subtree(root.right, subroot)

def sametree(p,q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return sametree(p.left, q.left) and sametree(p.right, q.right)
