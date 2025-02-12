# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrderBottom(self, root):
        levels = []
        if not root:
            return levels

        queue = [root]
        while queue:
            sub_levels = []
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                sub_levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(sub_levels)

        return levels[::-1]


