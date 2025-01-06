
# 144 二叉树的前序遍历


def postorderTraversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """

    def postorder(root):
        if not root:
            return

        postorder(root.right)
        postorder(root.left)
        res.append(root.val)

    res = []
    postorder(root)
    return res


def postorderTraversal2(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """

    if not root:
        return []
    res, stack, prev = [], [], None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not root.right or root.right == prev:
            res.append(root.val)
            prev = root
            root = None
        else:
            stack.append(root)
            root = root.right
    return res


def postorderTraversal3(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """

    pass

