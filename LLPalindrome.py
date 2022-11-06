# 234 Palindrome Linked List

def palindrome():

    # get to the middle
    fast = slow = head 
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse the second half
    prev = None
    while slow:

        next = slow.next

        slow.next = prev
        prev = slow

        slow = next
    
    # check if reversed == actual
    while head and prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    return True
