from wsgiref.util import request_uri


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calculateDepth(self, root):

        if not root:
            return 0
        return 1 + max(self.calculateDepth(root.left), self.calculateDepth(root.right))


class Solution:
    def calculateDepth(self, root):

        if not root: return 0
        queue, depth= [root], 0
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            depth += 1

        return depth



