
# 235. 二叉搜索树的最近公共祖先
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """

        如果在 BST 中寻找最近公共祖先，反而容易很多，主要利用 BST 左小右大（左子树所有节点都比当前节点小，右子树所有节点都比当前节点大）的特点即可。

        1、如果 p 和 q 都比当前节点小，那么显然 p 和 q 都在左子树，那么 LCA 在左子树。

        2、如果 p 和 q 都比当前节点大，那么显然 p 和 q 都在右子树，那么 LCA 在右子树。

        3、一旦发现 p 和 q 在当前节点的两侧，说明当前节点就是 LCA。

        """
        if not root:
            return None
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if root.val >= p.val or root.val <= q.val:
            return root
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

    def lowestCommonAncestor2(self, root, p, q):

        if not root:
            return None

        ancestor = root
        while ancestor:

            # If both p and q are less than ancestor, move to the left child
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            # If both p and q are greater than ancestor, move to the right child
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                # We have found the split point, i.e., the LCA node
                break

        return ancestor




