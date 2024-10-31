

def reverseBookList(head):
    """
    :type head: Optional[ListNode]
    :rtype: List[int]
    """
    return self.reverseBookList(head.next) + [head.val] if head else []



def reverseBookList_V2(head):
    if not head:
        return []
    stack = []
    while head:
        stack.append(head.val)
    return stack[::-1]
