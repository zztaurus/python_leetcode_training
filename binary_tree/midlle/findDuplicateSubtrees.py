
# Definition for a binary tree node.
# 652. 寻找重复的子树

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    """

    如果你想知道以自己为根的子树是不是重复的，是否应该被加入结果列表中，你需要知道什么信息？

        你需要知道以下两点：

            1、以我为根的这棵二叉树（子树）长啥样？

            2、以其他节点为根的子树都长啥样？

    """

    def __init__(self):
        self.memo = {}
        self.res = []

    def findDuplicateSubtrees(self, root):

        self.traverse(root)
        return self.res

    def traverse(self, root):

        if root is None:
            return "#"

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        subTree =  str(root.val) + "," + left + "," + right
        freq = self.memo.get(subTree, 0)
        if freq == 1:
            self.res.append(root)
        self.memo[subTree] = freq + 1
        return subTree



