
# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.memo = {}


    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None:
            return 0

        if root in self.memo:
            return self.memo[root]

        do_it = root.val + (0 if not root.left else self.rob(root.left.left) + self.rob(root.left.right)) \
                + (0 if not root.right else self.rob(root.right.left) + self.rob(root.right.right))
        not_do_it = self.rob(root.left) + self.rob(root.right)
        res = max(do_it, not_do_it)
        self.memo[root] = res
        return res




class Solution2(object):

    def __init__(self):
        self.f = {}
        self.g = {}


    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.dfs(root)
        return max(self.f.get(root), self.g.get(root))

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        self.dfs(root.right)

        self.f[root] = root.val + self.g.get(root.left, 0) + self.g.get(root.right, 0) # 选中root
        self.g[root] = max(self.f.get(root.left, 0), self.g.get(root.left, 0)) + max(self.f.get(root.right, 0), self.g.get(root.right, 0)) # 未选中root




class Solution3(object):

    def rob(self, root):
        root_status = self.dfs(root)
        return max(root_status[0], root_status[1])

    def dfs(self, node):
        if node is None:
            return [0, 0]

        left_status = self.dfs(node.left)
        right_status = self.dfs(node.right)

        selected = node.val + left_status[1] + right_status[1]
        not_selected = max(left_status[0], left_status[1]) + max(right_status[0], right_status[1])
        return [selected, not_selected]

