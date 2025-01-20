
# Definition for a binary tree node.

# 993. 二叉树的堂兄弟节点

"""

前序遍历二叉树，找到目标节点的深度和父节点

"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isCousins(self, root, x, y):
        # x 的信息
        x_parent, x_depth, x_found = None, None, False
        # y 的信息
        y_parent, y_depth, y_found = None, None, False


        def dfs(node, parent, depth):
            nonlocal x_parent, x_depth, x_found, y_parent, y_depth, y_found
            if node is None:
                return

            if node.val == x:
                x_parent, x_depth, x_found = parent, depth, True
            if node.val == y:
                y_parent, y_depth, y_found = parent, depth, True

            if x_found and y_found:
                return
            dfs(node.left, node, depth + 1)

            if x_found and y_found:
                return
            dfs(node.right, node, depth + 1)

        dfs(root, 0, None)
        return x_depth == y_depth and x_parent != y_parent



