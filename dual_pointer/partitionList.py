

# 86 分隔链表


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, k):
    SmallHead= ListNode(0, None)
    LargeHead = ListNode(0, None)

    SmallCur = SmallHead
    LargeCur = LargeHead

    cur = head
    while cur:
        if cur.next.val < k:
            SmallCur.next = cur
            SmallCur = SmallCur.next
        else:
            LargeCur.next = cur
            LargeCur = LargeCur.next
        cur = cur.next
    SmallCur.next = LargeHead.next
    LargeCur.next = None
    return SmallHead.next




