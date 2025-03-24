
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def addOneRow(self, root, val, depth):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :type depth: int
        :rtype: Optional[TreeNode]
        """

        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode

        def dfs(node, d):
            if node is None:
                return
            if depth == d - 1:
                old_left = node.left
                old_right = node.right
                node.left = TreeNode(val, old_left, None)
                node.right = TreeNode(val, None, old_right)
            else:
                dfs(node.left, d + 1)
                dfs(node.right, d + 1)


        dfs(root, 1)
        return root