

# 572 另一棵树的子树

"""

给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

"""

class Solution1(object):

    def isSubtree1(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        # 判断 subTree 是否是当前树的子树
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s, l):
        if not s and not l:
            return True
        if not s or not l:
            return False
        return s.val == l.val and self.isSameTree(s.left, l.left) and self.isSameTree(s.right, l.right)



"""

解法二:

    深度优先搜索遍历两棵树 S 和 T， 判断T的搜索序列是否是S的搜索序列的子串。

"""


class Solution2(object):

    def isSubtree2(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        pass

    def dfs(self, node):
        pass
         


    def kmp(self, m, n):
        pass

