# 104
# recursion

def maxdepth(root):

    if not root:
        return
    
    return 1 + max(maxdepth(root.left), maxdepth(root.right))

# iterative bfs using queue

def bfsdepth(root):

    if not root:
        return 0

    q = [root]
    level = 0

    while q:
        for i in range (len(q)):
            node = q.pop(0)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        level += 1
    
    return level

# iterative dfs using stack

def dfsdepth(root):
    # use double arrays because cannot unpack non iterable int object
    stack = [[root, 1]]
    res = 0

    while stack:
        
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res