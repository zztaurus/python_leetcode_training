# Definition for a binary tree node.
from lib2to3.btm_utils import reduce_tree


# 515 在每个树行中找最大值

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 使用 bfs 解决
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        res = []
        if not root:
            return res

        queue = [root]
        while queue:
            size = len(queue)
            max_val = float('-inf')

            for _ in range(size):
                node = queue.pop(0)
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(max_val)

        return res

class Solution2(object):
    # 一定要用 array 存储，因为要用索引随机访问
    res = []

    def largestValues(self, root):
        if root is None:
            return self.res
        self.traverse(root, 0)
        return self.res

    # 遍历二叉树
    def traverse(self, root, depth):
        if root is None:
            return
        if len(self.res) <= depth:
            self.res.append(root.val)
        else:
            # 记录当前行的最大值
            self.res[depth] = max(self.res[depth], root.val)
        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)








