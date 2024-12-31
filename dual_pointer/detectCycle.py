

# 142 环形链表II

"""

根据：

f=2s （快指针每次2步，路程刚好2倍）

f = s + nb (相遇时，刚好多走了n圈）

推出：s = nb

从head结点走到入环点需要走 ： a + nb， 而slow已经走了nb，那么slow再走a步就是入环点了。

如何知道slow刚好走了a步？ 从head开始，和slow指针一起走，相遇时刚好就是a步

"""

def detectCycle(head):

    slow, fast = head, head
    while True:
        if not (fast and fast.next): return
        slow = slow.next
        fast = fast.next.next
        if slow == fast: break

    ptr = head
    while ptr != slow:
        ptr = ptr.next
        slow = slow.next

    return ptr







