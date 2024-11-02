

# LCR 123 图书整理1

def reverseBookList(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: List[int]
    """

    return self.reverseBookList(head.next) + [head.val] if head else []

