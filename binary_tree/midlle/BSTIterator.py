
# Definition for a binary tree node.

# 173. 二叉搜索树迭代器

# 利用栈模拟二叉树的中序遍历

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self.pushBranchLeft(root)

    def pushBranchLeft(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.pushBranchLeft(node.right)
        return node.val



    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

