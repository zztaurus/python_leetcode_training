

# 257. 二叉树的所有路径

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):

        result = []

        def construct_paths(root, path):

            path += str(root.val)
            if not root.left and not root.right:
                result.append(path)
            else:
                path += '->'
                construct_paths(root.left, path)
                construct_paths(root.right, path)

        construct_paths(root, "")

        return result

    def binaryTreePaths2(self, root):

        """

        BFS

        """
        result = []
        if not root:
            return []
        queue = [root]
        node_paths = [str(root.val)]
        while queue:

            node = queue.pop(0)
            node_path = node_paths.pop(0)
            node_path += str(node.val)
            if not node.left and not node.right:
                result.append(node_path)
            else:
                if node.left:
                    queue.append(node.left)
                    node_paths.append(node_path + '->' + str(node.left.val))
                if node.right:
                    queue.append(node.right)
                    node_paths.append(node_path + '->' + str(node.right.val))
        return result




