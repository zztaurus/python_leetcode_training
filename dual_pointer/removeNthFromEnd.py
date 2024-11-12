
# 19. 删除链表的倒数第N个节点

def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy

    # Move fast ahead by n+1 steps to maintain the gap
    for _ in range(n + 1):
        fast = fast.next

    # Move both slow and fast until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    # Skip the node to be deleted
    slow.next = slow.next.next

    # Return the head of the modified list
    return head

