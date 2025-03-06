# Definition for a binary tree node.

# 508 出现次数最多的子树元素和

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.sum_to_count = {}

    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return self.sum_to_count

        max_count = max(self.sum_to_count.values(), default=0)
        res = [key for key, count in self.sum_to_count.items() if count == max_count]
        return res


    def dfs(self, root):

        if not root:
            return 0
        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)
        root_sum = root.val + left_sum + right_sum

        # postorder traversal position, record the frequency of the subtree sum
        self.sum_to_count[root_sum] = self.sum_to_count.get(root_sum, 0) + 1
        return root_sum

