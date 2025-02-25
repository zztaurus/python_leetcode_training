
# Definition for a binary tree node.

# 437. 路径总和 III

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self):
        self.ans = 0
        self.cnt = {0: 1}

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # Use a regular dictionary with a default value

        def dfs(node, current_sum):
            nonlocal ans
            if node is None:
                return

            # Update the current path sum
            current_sum += node.val

            # Check if there is a prefix sum that matches the target
            self.ans += self.cnt.get(current_sum - targetSum, 0)

            # Update the count of the current path sum
            self.cnt[current_sum] = self.cnt.get(current_sum, 0) + 1

            # Recurse into the left and right children
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # Backtrack: remove the current path sum count
            self.cnt[current_sum] -= 1

        dfs(root, 0)
        return self.ans


