
# Definition for a binary tree node.

# 226 翻转二叉树

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def invertTree(self, root):
        """
           递归方式
        """
        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

    def invertTree2(self, root):
        """
           迭代方式
        """
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root

