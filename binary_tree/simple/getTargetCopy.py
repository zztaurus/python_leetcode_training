
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        if original is None:
            return None
        if original == target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left is not None:
            return left
        return self.getTargetCopy(original.right, cloned.right, target)



class Solution2:

    def getTargetCopy(self, original, cloned, target):

        pass




