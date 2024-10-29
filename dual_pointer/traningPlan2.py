


# 双指针思路与算法：
#
# 快慢指针的思想。我们将第一个指针 fast 指向链表的第 cnt+1 个节点，第二个指针 slow 指向链表的第一个节点，此时指针 fast 与 slow 二者之间刚好间隔 cnt 个节点。
#
#               此时两个指针同步向后走，当第一个指针 fast 走到链表的尾部空节点时，则此时 slow 指针刚好指向链表的倒数第cnt个节点。
#
#    我们首先将 fast 指向链表的头节点，然后向后走 cnt 步，则此时 fast 指针刚好指向链表的第 cnt+1 个节点。
#
#    我们首先将 slow 指向链表的头节点，同时 slow 与 fast 同步向后走，当 fast 指针指向链表的尾部空节点时，则此时返回 slow 所指向的节点即可。




def trainingPlan(head, cnt):
    """
    :type head: Optional[ListNode]
    :type cnt: int
    :rtype: Optional[ListNode]
    """

    fast, slow = head, head

    for i in range(cnt):
        fast = fast.next

    # while fast and cnt > 0:
    #     fast = fast.next
    #     cnt -= 0

    while fast:  # 注意，当fast节点为空(最后一个节点的下一个节点)时才找到响应的倒数节点
        fast = fast.next
        slow = slow.next

    return slow




if __name__ == '__main__':

