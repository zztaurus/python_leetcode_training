
# 144 二叉树的前序遍历


def preorderTraversal(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """

    def preorder(root):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    res = []
    preorder(root)
    return res


def preorderTraversal2(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """

    """
    
        入栈顺序：
                
            1. 先根节点
            2. 弹出并visit根节点
            3. 入右子树
            4. 入左子树
    
    """

    res = list()
    if not root:
        return res

    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def preorderTraversal3(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """

    pass

