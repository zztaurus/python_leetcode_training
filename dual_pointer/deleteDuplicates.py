
'''

给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次。 返回已排序的链表。

删除列表中的重复元素

'''


def deleteDuplicates(head):
    slow, fast = head, head
    while(fast is not None):
        if fast.val != slow.val:
            slow.next = fast
            slow = slow.next # slow ++
        fast = fast.next # fast ++
    slow.next = None
    return head




