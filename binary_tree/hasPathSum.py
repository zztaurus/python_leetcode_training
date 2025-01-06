
# 112 路劲总和


def hasPathSum(self, root, targetSum):
    """
    DFS
    """

    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


def hasPathSum2(self, root, targetSum):

    """
    BFS
    """

    if not root:
        return False

    queue = [(root, targetSum)]
    while queue:
        node, target = queue.pop(0)
        if not node.left and not node.right and target == root.val:
            return True
        if node.left: queue.append((node.left, target - node.val))
        if node.right: queue.append((node.right, target - node.val))
    return False

