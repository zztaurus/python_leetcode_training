import math


# Definition for a binary tree node.

# 111 二叉树的最小深度


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1(object):

    def __init__(self):
        self.minimumDepth = float('inf')
        self.currentDepth = 0

    def minDepth(self, root):
        if root is None:
            return 0
        self.traverse(root)
        return self.minimumDepth

    def traverse(self, root):
        if root is None:
            return

        # 做选择：在进入节点时增加当前深度
        self.currentDepth += 1

        # 如果当前节点是叶子节点，更新最小深度
        if root.left is None and root.right is None:
            self.minimumDepth = min(self.minimumDepth, self.currentDepth)

        self.traverse(root.left)
        self.traverse(root.right)

        # 撤销选择：在离开节点时减少当前深度
        self.currentDepth -= 1


class Solution2(object):

    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        minimumDepth = float('inf')
        if root.left:
            minimumDepth = min(minimumDepth, self.minDepth(root.left))

        if root.right:
            minimumDepth = min(minimumDepth, self.minDepth(root.right))

        return minimumDepth + 1

"""
    对于DFS算法, 需要遍历完树的所有节点才能确定二叉树的最小深度
"""


class Solution3(object):

    def minDepth1(self, root):

        if not root:
            return 0

        queue = [root]
        depth = 1
        while queue:
            sz = len(queue)
            for _ in range(sz):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth

"""

    由于 BFS 逐层遍历的逻辑，第一次遇到目标节点时，所经过的路径就是最短路径，算法可能并不需要遍历完所有节点就能提前结束。
    
    DFS 遍历当然也可以用来寻找最短路径，但必须遍历完所有节点才能得到最短路径。
    
    从时间复杂度的角度来看，两种算法在最坏情况下都会遍历所有节点，时间复杂度都是 O(N)，但在一般情况下，显然 BFS 算法的实际效率会更高。
    
    所以在寻找最短路径的问题中，BFS 算法是首选。

"""