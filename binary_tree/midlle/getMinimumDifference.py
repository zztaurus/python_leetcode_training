
# Definition for a binary tree node.
# 530 二叉树的绝对最小差值

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self):
        self.pre = None
        self.ans = 10 ** 5

    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.pre is not None:
                self.ans = min(self.ans, abs(root.val - self.pre))
            self.pre = root.val
            dfs(root.right)

        dfs(root)
        return self.ans




