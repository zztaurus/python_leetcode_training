
# 700. 二叉搜索树中的搜索

"""

给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

"""

class Solution1(object):

    def searchBST(self, root, val):
        """
        DFS
        """
        if root is None:
            return None
        if val == root.val:
            return root
        return self.searchBST(root.left if val < root.val else root.right, val)


class Solution2(object):

    def searchBST(self, root, val):
        """
        迭代
        """
        if root is None:
            return None
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None

