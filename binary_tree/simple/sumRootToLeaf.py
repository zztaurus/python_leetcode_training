
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:

    def sumRootToLeaf(self, root):

        res = []
        sum = 0

        def dfs(node, path):
            if not node:
                return

            # Append the current node's value to the path
            path.append(node.val)

            # If it's a leaf node, add the path to the results
            if not node.left and not node.right:
                res.append(list(path))
            else:
                # Continue the DFS on the left and right children
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)

            # Backtrack: remove the current node's value from the path
            path.pop()

        # Start DFS from the root
        dfs(root, [])

        # Calculate the sum of all root-to-leaf paths interpreted as binary numbers
        for item in res:
            # Convert the binary path to a decimal number and add to the sum
            binary_number = int(''.join(map(str, item)), 2)
            sum += binary_number

        return sum


class Solution2:

    # 后序遍历

    def sumRootToLeaf(self, root):

        def dfs(node, val) -> int:
            if node is None:
                return 0
            # val = (val << 1) | node.val
            val = val * 2 + root.val
            if node.left is None and node.right is None:
                return val
            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, 0)








