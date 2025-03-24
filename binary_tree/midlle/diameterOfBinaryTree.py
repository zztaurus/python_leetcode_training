# Definition for a binary tree node.
# 543. 二叉树的直径


# 所谓二叉树的直径，就是左右子树的最大深度之和，那么直接的想法是对每个节点计算左右子树的最大高度，得出每个节点的直径，从而得出最大的那个直径。


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root):
        self.depth(root)
        return self.ans

    def depth(self, node):
        if node is None:
            return 0  # 访问到空节点了，返回0
        L = self.depth(node.left)  # 左儿子为根的子树的深度
        R = self.depth(node.right)  # 右儿子为根的子树的深度
        self.ans = max(self.ans, L + R)  # 计算d_node即L+R+1 并更新ans
        return max(L, R) + 1  # 返回该节点为根的子树的深度