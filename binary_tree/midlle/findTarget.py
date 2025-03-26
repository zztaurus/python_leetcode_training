
# Definition for a binary tree node.

# 653. 两数之和 IV - 输入二叉搜索树


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        arr = self.traverse(root)
        i, j = 0, len(arr) - 1
        while i < j:

            if arr[i] + arr[j] < k:
                i = i + 1
            elif arr[i] + arr[j] > k:
                j = j - 1
            else:
                return True

        return False



    def traverse(self, root):

        res = []
        if not root:
            return res

        res.extend(self.traverse(root.left))
        res.append(root.val)
        res.extend(self.traverse(root.right))

        return res

