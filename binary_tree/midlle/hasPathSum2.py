# Definition for a binary tree node.
# 113. 路径总和 II

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        遍历思维

        基于深度优先搜索, 使用回溯法，寻找所有路径
        """

        def dfs(node, current_path, current_sum):
            if not node:
                return

            # 进入递归的时候要在 path 列表添加节点，
            current_path.append(node.val)
            current_sum += node.val

            # Check if it's a leaf node and the current sum equals targetSum
            if not node.left and not node.right and current_sum == targetSum:
                # Append a copy of the current path to the result
                result.append(list(current_path))

            # Continue the search on the left and right children
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)

            # 结束递归的时候在 path 列表删除节点，类似 回溯算法。
            current_path.pop()

        result = []
        dfs(root, [], 0)
        return result


class Solution2(object):

    def pathSum(self, root, targetSum):
        """
        分解思维:

        计算以 root 为根的二叉树中和为 sum 的路径，不就可以分解成计算以 root.left, root.right 为根的二叉树中所有和为 sum - root.val 的路径，然后再加上 root 节点吗？
        """

        result = []
        if not root:
            return result

        if root.left == None and root.right == None and root.val == targetSum:
            return [[root.val]]

        left_answers = self.pathSum(root.left, targetSum - root.val)
        right_answers = self.pathSum(root.right, targetSum - root.val)

        # 左右子树的路径加上根节点，就是和为 targetSum 的路径
        for answer in left_answers:
            # 因为底层使用的是 LinkedList，所以这个操作的复杂度是 O(1)
            answer.insert(0, root.val)
            result.append(answer)

        for answer in right_answers:
            # 因为底层使用的是 LinkedList，所以这个操作的复杂度是 O(1)
            answer.insert(0, root.val)
            result.append(answer)

        return result





