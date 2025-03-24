# Definition for a binary tree node.

# LCR 194. 二叉树的最近公共祖先

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root, p, q):

        """

            如果root节点为p和q的公共祖先节点，则需满足下面三个条件之一:

                1. p 和 q 分别位于root的左右子树中

                2. p == root, q 位于root的子树中

                3. q == root, p 位于root的子树中


        1. 递归终止条件:

            root为叶子节点或者 root == p 或者 root == q

        2. 递推逻辑:

            开启递归左子节点，返回值记为 left ；
            开启递归右子节点，返回值记为 right ；

        3. 返回值:

            1. 当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p , q ，返回 null ；

            2. 当 left 和 right 同时不为空 ：说明 p , q 分列在 root 的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root ；

            3. 当 left 为空 ，right 不为空 ：p , q 都不在 root 的左子树中，直接返回 right 。具体可分为两种情况：

                p , q 其中一个在 root 的 右子树 中，此时 right 指向 p（假设为 p ）；

                p , q 两节点都在 root 的 右子树 中，此时的 right 指向 最近公共祖先节点 ；

            当 left 不为空 ，right 为空 ：与情况 3. 同理；

        遍历方式: 基于二叉树的先序遍历

        """

        if root is None:
            return None  # 如果树为空，直接返回None
        if root == p or root == q:
            return root  # 如果 p和q中有等于 root的，那么它们的最近公共祖先即为root（一个节点也可以是它自己的祖先）

        left = self.lowestCommonAncestor(root.left, p, q)  # 递归遍历左子树
        right = self.lowestCommonAncestor(root.right, p, q)  # 递归遍历右子树

        if left is None:
            return right  # 如果在左子树中 p和 q都找不到，则 p和 q一定都在右子树中
        elif right is None:
            return left  # 如果在右子树中 p和 q都找不到，则 p和 q一定都在左子树中
        else:
            return root  # 如果 left和 right均不为空，说明 p、q节点分别在 root异侧



