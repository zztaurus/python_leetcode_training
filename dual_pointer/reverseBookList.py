

# LCR 123 图书整理1

def reverseBookList(head):
    """
    :type head: Optional[ListNode]
    :rtype: List[int]
    """

    return reverseBookList(head.next) + [head.val] if head else []


def reverseBookList_V2(head):
    if not head:
        return []
    stack = []
    while head:
        stack.append(head.val)
    return stack[::-1]
