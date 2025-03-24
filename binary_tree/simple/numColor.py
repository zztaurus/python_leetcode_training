


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numColor(self, root):
        s = set()
        def dfs(root):
            if root is None:
                return
            s.add(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return len(s)



