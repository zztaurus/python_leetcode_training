
# 783. 二叉搜索树节点最小距离

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root) -> int:

        pre = -1
        min_diff = float('inf')

        def in_order_traversal(node):
            nonlocal pre, min_diff
            if not node:
                return

            # Traverse the left subtree
            in_order_traversal(node.left)

            # Process the current node
            if pre != -1:
                min_diff = min(min_diff, node.val - pre)
            pre = node.val

            # Traverse the right subtree
            in_order_traversal(node.right)

        in_order_traversal(root)
        return min_diff
