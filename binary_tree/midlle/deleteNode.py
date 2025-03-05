
# Definition for a binary tree node.
# 450 删除二叉搜索树中的节点

"""

case 1： A 恰好是末端节点，两个子节点都为空，那么它可以当场去世了：

case 2:  A 只有一个非空子节点，那么它要让这个孩子接替自己的位置：

case 3:  A 有两个子节点，麻烦了，为了不破坏 BST 的性质，A 必须找到左子树中最大的那个节点或者右子树中最小的那个节点来接替自己，我的解法是用右子树中最小节点来替换：

"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):

        if root is None:
            return  None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # 这两个 if 把情况1和情况2都一起处理了
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right

            min_node = self.findMin(root.right)
            root.right = self.deleteNode(root.right, min_node.val)
            # 用右子树最小的节点替换 root 节点
            min_node.left = root.left
            min_node.right = root.right
            root = min_node
        return  root


    def findMin(self, node):
        while node.left:
            node = node.left
        return node

