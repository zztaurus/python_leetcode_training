
# Definition for a binary tree node.

# 563 二叉树的坡度


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self):
        self.res = 0

    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.calculateTilt(root)
        return self.res

    def calculateTilt(self, root):

        if not root:
            return 0

        left_Sum = self.calculateTilt(root.left)
        right_Sum = self.calculateTilt(root.right)

        self.res += abs(left_Sum - right_Sum)
        total_sum = left_Sum + right_Sum + root.val
        return total_sum






