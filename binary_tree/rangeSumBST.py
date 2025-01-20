
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def rangeSumBST(self, root, low, high):

        if not root:
            return 0

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)



class Solution2:


    def rangeSumBST(self, root, low, high):

        if not root:
            return 0
        res = 0
        queue = [root]
        while queue:
            node = queue.pop(0)
            if low <= node.val <= high:
                res += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res






