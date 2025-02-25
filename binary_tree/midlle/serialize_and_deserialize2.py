# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return "[]"

        def preorder(node):
            if not node:
                return ["null"]
            return [str(node.val)] + preorder(node.left) + preorder(node.right)

        res = preorder(root)
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        if not data or data == "[]":
            return None

        vals = data[1:-1].split(',')

        def build_bst(nodes):
            if not nodes:
                return None

            first = nodes.pop(0)
            if first == 'null':
                return None

            root = TreeNode(int(first))
            root.left = build_bst(nodes)
            root.right = build_bst(nodes)
            return root

        return build_bst(vals)
