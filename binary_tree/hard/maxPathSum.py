# Definition for a binary tree node.

# 124. 二叉树中的最大路径和


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.res = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        self.oneSidePathSum(root)
        return self.res


    # 定义：计算从根节点 root 为起点的最大单边路径和
    def oneSidePathSum(self, root):

        if root is None:
            return 0

        left_max_sum = max(0, self.oneSidePathSum(root.left)) # 以左子节点为起点的最大单边路径和
        right_max_sum = max(0, self.oneSidePathSum(root.right)) # 以右子节点为起点的最大单边路径和
        # 后序遍历位置，顺便更新最大路径和
        path_max_sum = root.val + left_max_sum + right_max_sum
        self.res = max(self.res, path_max_sum)
        # 实现函数定义，左右子树的最大单边路径和加上根节点的值
        # 就是从根节点 root 为起点的最大单边路径和
        return max(left_max_sum, right_max_sum) + root.val

