
# 110 平衡二叉树

"""

平衡二叉树的定义是：二叉树的每个节点的左右子树的高度差的绝对值不超过 1，则二叉树是平衡二叉树。

根据定义，一棵二叉树是平衡二叉树，当且仅当其所有子树也都是平衡二叉树，因此可以使用递归的方式判断二叉树是不是平衡二叉树，递归的顺序可以是自顶向下或者自底向上。

"""


def isBalanced(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    if root is None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    else:
        return isBalanced(root.left) and isBalanced(root.right)


def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1



