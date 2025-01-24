
# Definition for a binary tree node.

# LCR 144. 翻转二叉树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:

    def flipTree(self, root):
        if root is None:
            return root
        left = self.flipTree(root.left)
        right = self.flipTree(root.right)
        root.left = right
        root.right = left
        return root


class Solution2:

    def flipTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            # 交换左右节点
            node.left, node.right = node.right, node.left
        return root



