

# 61 旋转链表


def rotateRight(head, k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """

    """
    新链表的最后一个节点为原链表的第 (n−1)−(k % n) 个节点（从 0 开始计数）。
    
    闭合为环，然后从指定位置断开
    
    我们首先计算出链表的长度 n，并找到该链表的末尾节点，将其与头节点相连。这样就得到了闭合为环的链表。
    
    然后我们找到新链表的最后一个节点（即原链表的第 (n−1)−(kmodn) 个节点），将当前闭合为环的链表断开，即可得到我们所需要的结果。

    当链表长度不大于 1，或者 k 为 n 的倍数时，新链表将与原链表相同，我们无需进行任何处理。
    
    """

    if k == 0 or not head or not head.next:
        return head

    n = 1
    cur = head
    while cur.next:
        cur = cur.next
        n += 1
    cur.next = head
    step = n - 1 - ( k % n)

    rtr = head
    while step > 0:
        rtr = rtr.next
        step -= 1

    r_head = rtr.next
    rtr.next = None

    return r_head








