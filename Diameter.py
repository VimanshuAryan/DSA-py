# 543 diameter of a binary tree


def diameter(root):

    res = [0]

    def dfs(root):
        if not root:
            return -1 # for formula to work out
        left = dfs(root.left) # height of left sub tree
        right = dfs(root.right) # height of right sub tree

        res[0] = max(res[0],2 + left + right) # diameter formula
        return 1 + max(left,right) # return max height
    dfs(root)
    return res[0]
