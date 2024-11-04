

# 面试题 02.01. 移除重复节点

def removeDuplicateNodes(head):

    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    pre, cur = None, head
    visited = set(head.val)

    while cur:
        if cur.val not in visited:
            visited.add(cur.val)
            pre = cur
        else:
            pre.next = cur.next
        cur = cur.next
    return head
