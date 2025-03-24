
# 872. 叶子相似的树


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def dfs(node, leaves):
            if node and not node.left and not node.right:
                leaves.append(node.val)

            if node.left:
                dfs(node.left, leaves)
            if node.right:
                dfs(node.right, leaves)

        root1_leaves = []
        root2_leaves = []
        dfs(root1, root1_leaves)
        dfs(root2, root2_leaves)
        return root1_leaves == root2_leaves