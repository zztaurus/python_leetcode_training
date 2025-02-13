
#

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sortedListToBST(self, head):

        # 链表相较于数组失去了基于下标随机访问的特性，所以可以将链表转换为数组, 基于数组来构建二叉树

        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.build(array, 0, len(array) - 1)

    def build(self, array, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(array[mid])
        root.left = self.build(array, left, mid - 1)
        root.right = self.build(array, mid + 1, right)
        return root

class Solution2:

    def sortedListToBST(self, head):

        # 通过找到链表的中间节点来构造二叉树

        return self.build(head, None)

    def build(self, begin, end):
        if begin == end:
            # 因为是左闭右开区间，所以现在已经成空集了
            return None
        mid = self.getMid(begin, end)
        root = TreeNode(mid.val)
        root.left = self.build(begin, mid)
        root.right = self.build(mid.next, end)
        return root

    def getMid(self, begin, end):
        slow, fast = begin, begin
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        return slow

