# 160 intersection of two LL

def intersection():

    l1, l2 = headA, headB

    while l1 != l2:
        
        # make both the pointers traverse both the LL 
        # and the first intersection will be the req node
        # if no intersection f() will return null
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA 

    return l1