

# 111 二叉树的最小深度
# 二叉树的最小深度是指从根节点到最近叶子节点的最短路径上的节点数量。

def minDepth1(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root:
        return 0

    if not root.left or not root.right: # 这里需要考虑到左右子树是否有叶子节点
        return 1 + max(self.minDepth(root.left), self.minDepth(root.right))

    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

def minDepth2(self, root):
    #BFS

    if root is None:
        return 0

    queue = [(root, 1)]
    while queue:
        node, depth = queue.pop(0)
        if node.left is None and node.right is None:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))  # 保存节点所处的深度
        if node.right:
            queue.append((node.right, depth + 1)) # 保存节点所处的深度

    return 0




