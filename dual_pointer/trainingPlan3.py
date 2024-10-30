


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """

    """
        链表A和链表B公共部分长度为c, 链表A单独部分为 a, 链表B 单独部分为 b, 则有 a + (b - c) = b + (a - c)
    """

    A, B = headA, headB
    while A != B:
        A = A.next if A else headB
        B = B.next if B else headA
    return A

