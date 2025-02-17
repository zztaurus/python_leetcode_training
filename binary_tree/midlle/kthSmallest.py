
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self):
        self.res = 0
        self.rank = 0

    def kthSmallest(self, root, k):

        self.traverse(root, k)
        return self.res

    def traverse(self, root, k):
        if not root:
            return
        self.traverse(root.left, k)
        self.rank += 1
        if self.rank == k:
            self.res = root.val
        self.traverse(root.right, k)







