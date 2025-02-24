
# Definition for a binary tree node.

# 297. 二叉树的序列化与反序列化
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return "[]"

        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return "[" + ",".join(res) + "]"


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "[]":
            return None
        vals = data[1:-1].split(',')
        index = 1
        root = TreeNode(int(vals[0]))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if vals[index] != 'null':
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1

            if vals[index] != 'null':
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1

        return root


class Codec2:

    def __init__(self):
        self.res = []

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root: return "[]"
        return self._serialize(root)


    def _serialize(self, root):
        if not root:
            self.res.append("null")
            return
        self._serialize(root.left)
        self.res.append(str(root.val))  # 前序遍历
        self._serialize(root.right)
        return "[" + ",".join(self.res) + "]"


    def deserialize(self, data):
        if not data: return None
        nodes = data[1:-1].split(',')
        root = self._deserialize(nodes)
        return root

    def _deserialize(self, nodes):
        if not nodes:
            return None
        first = nodes.pop(0)
        if first == 'null':
            return None
        root = TreeNode(int(first))
        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)
        return root

