
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



class BSTIterator2(object):

    # 遍历二叉树然后存储二叉树的中序遍历结果
    
    def __init__(self, root):
        self.idx = 0
        self.arr = []
        self._inorder_traversal(root)

    def _inorder_traversal(self, root):
        if root is None:
            return
        self._inorder_traversal(root.left)
        self.arr.append(root.val)
        self._inorder_traversal(root.right)

    def next(self):
        result = self.arr[self.idx]
        self.idx += 1
        return result

    def hasNext(self):
        return self.idx < len(self.arr)
