#108 

def func():
    
    def helper(l,r):

        if l>r:
            return 
        
        m = l+r //2
        root = treenode(m)

        helper(l,m-1)
        helper(m+1,r)

        return root
    
    return helper(0,len(nums) - 1)