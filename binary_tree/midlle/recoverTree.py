from IPython.core.inputsplitter import num_ini_spaces


# 99. 恢复二叉搜索树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        nums = []
        self.inorder(root, nums)
        x, y = self.findtwoSwaped(root, nums)
        self.recover(root, 2, x, y)

    def inorder(self, root, nums):
        if root is None:
            return
        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)
        return nums

    def findtwoSwaped(self, nums):
        n = len(nums)
        index1, index2 = -1, -1
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                index2 = i + 1
                if index1 == -1:
                    index1 = i
                else:
                    break
        x, y = nums[index1], nums[index2]
        return x, y

    def recover(self, root, count, x, y):
        if root is not None:
            if root.val == x or root.val == y:
                root.val = y if root.val == x else x
                count -= 1
                if count == 0:
                    return
            self.recover(root.left, count, x, y)
            self.recover(root.right, count, x, y)




