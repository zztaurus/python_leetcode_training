from lib2to3.btm_utils import reduce_tree

# Definition for a binary tree node.

# 236. 二叉树的最近公共祖先

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):

        if not root or root == p or root == q:
            return root

        # Recurse on the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, root is the LCA
        if left and right:
            return root

        # Otherwise, return the non-null child
        return left if left else right




