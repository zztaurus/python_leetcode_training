
# 110 平衡二叉树

"""

平衡二叉树的定义是：二叉树的每个节点的左右子树的高度差的绝对值不超过 1，则二叉树是平衡二叉树。

根据定义，一棵二叉树是平衡二叉树，当且仅当其所有子树也都是平衡二叉树，因此可以使用递归的方式判断二叉树是不是平衡二叉树，递归的顺序可以是自顶向下或者自底向上。

"""


def isBalanced(self, root):
    """
        自顶向下的递归:
        
            p 是空节点: height(p) = 0
            p 是非空节点:  height(p)= max(height(p.left),height(p.right))+1
            
        有了计算节点高度的函数，即可判断二叉树是否平衡。具体做法类似于二叉树的前序遍历，即对于当前遍历到的节点，
        
        首先计算左右子树的高度，如果左右子树的高度差是否不超过 1，再分别递归地遍历左右子节点，并判断左子树和右子树是否平衡。这是一个自顶向下的递归的过程。

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


def isBalanced2(self, root):

    """

    方法一由于是自顶向下递归，因此对于同一个节点，函数 height 会被重复调用，导致时间复杂度较高。如果使用自底向上的做法，则对于每个节点，函数 height 只会被调用一次。

    自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。

    如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回 −1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。

    """
    return height2(root) >= 0;


def height2(root):

    if root is None:
        return 0

    left_height = height2(root.left)
    right_height = height2(root.right)
    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1






