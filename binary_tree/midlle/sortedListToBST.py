
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

