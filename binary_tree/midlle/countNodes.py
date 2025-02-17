
# Definition for a binary tree node.

# 222 完全二叉树的节点个数

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        """
        if root is None:
            return 0
        left  = countLevel(root.left)
        right = countLevel(root.right)
        if left == right:
            return self.countNodes(root.right) + (1 << left)
        else:
            return self.countNodes(root.left) + (1 << right)


def countLevel(node):
    # 因为二叉树是完全二叉树，所以可以通过不断搜索左子树来计算二叉树高度
    level = 0
    while node is not None:
        level += 1
        node = node.left
    return level


