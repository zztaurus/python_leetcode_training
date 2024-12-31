
# 148 排序链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):

    if not head or not head.next:
        return head

    # 分隔链表

    def split(head):
        slow, fast = ListNode(next=head), ListNode(next=head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid

    # 合并链表
    def merge(l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    # Split the list into two halves
    left, right = split(head)

    # Recursively sort each half
    left = sortList(left)
    right = sortList(right)

    # Merge the sorted halves
    return merge(left, right)


def printList(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(1)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    head = sortList(a)
    print("head: ", head.val)
    printList(head)



