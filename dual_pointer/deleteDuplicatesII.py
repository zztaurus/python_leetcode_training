

# 82 删除排序链表中的重复元素 II

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicatesII(head):
    dummy = ListNode(0, head)
    cur = dummy
    while cur.next and cur.next.next: # cur 指向当前的非重复数据
        if cur.next.val == cur.next.next.val:
            # 当前已出现重复，寻找下一个数据
            val = cur.next.val
            while(cur.next & cur.next.val == val):
                cur.next = cur.next.next
        else:
            # 删除数据
            cur = cur.next

    return dummy.next # head




