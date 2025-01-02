
# 104, 二叉树的最大深度
# 树的遍历: 深度优先(DFS)遍历和广度优先(BFS)遍历


def maxDepth(self, root):
    if root is None:
        return 0
    else:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def maxDepeth(root):

    if root is None:
        return 0

    queue, depth = [root], 0
    while queue:

        for node in queue:
            queue.append(node.left)
            queue.append(node.right)
            queue.remove(node)
        depth += 1

    return depth


