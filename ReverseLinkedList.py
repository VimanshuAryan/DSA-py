# 206 reverse a LL
# No implementation of LL hence does not run on terminal

head = [1,2,3,4,5]

def reverse(head):
    # two pointers curr and prev
    curr, prev = head, None

    while curr:
        # temp var to store curr.next
        next = curr.next
        # switch pointer to prev
        curr.next = prev
        # increase curr and prev to traverse LL
        prev = curr
        curr = next
    return prev

print(reverse(head))
