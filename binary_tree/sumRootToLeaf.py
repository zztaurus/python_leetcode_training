
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sumRootToLeaf(self, root):

        res = []
        leaves = []
        sum = 0

        def dfs(root, leaves):

            if not root:
                res.append(leaves)

            leaves.append(root.val)

            if root.left:
                dfs(root.left, leaves)

            if root.right:
                dfs(root.right, leaves)

        for str in res:
            #累加二进制的和

        return sum




