# Definition for a binary tree node.

# 513 找到左下角的值

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return None
        queue = [root]
        leftmost_value = root.val
        while queue:
            size = len(queue)
            next_queue = []
            for i in range(size):
                node = queue.pop(0)
                if i == 0:
                    leftmost_value = node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return leftmost_value


class Solution2(object):

    def __init__(self):
        self.max_depth = 0
        self.depth = 0
        self.res = None

    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.traverse(root)
        return self.res.va

    def traverse(self, root):
        if not root:
            return
        self.depth += 1
        if self.depth > self.max_depth:
            # 按照从左向右的方式遍历, 当到达最大深度时遍历的第一个节点就是最左子节点
            self.max_depth = self.depth
            self.res = root
        self.traverse(root.left)
        self.traverse(root.right)
        self.depth -= 1
