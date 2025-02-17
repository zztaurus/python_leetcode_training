
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def rightSideView(self, root):
        """
        用 BFS 层序遍历算法，每一层的最后一个节点就是二叉树的右侧视图。我们可以把 BFS 反过来，从右往左遍历每一行，进一步提升效率。
        """

        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            size = len(queue)
            last = queue[0]
            for i in range(size):
                node = queue.pop(0)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            res.append(last.val)
        return res

    def rightSideView2(self, root):
        """
        用 DFS 递归遍历算法，同样需要反过来，先递归 root.right 再递归 root.left，同时用 res 记录每一层的最右侧节点作为右侧视图。
        """

        self.res = []
        self.depth = 0
        self.traverse(root)
        return self.res


    def traverse(self, root):
        if not root:
            return
        self.depth += 1
        if len(self.res) < self.depth:
            # 当前层还没有记录右视图值
            self.res.append(root.val)

        self.traverse(root.right)
        self.traverse(root.left)

        self.depth -= 1


