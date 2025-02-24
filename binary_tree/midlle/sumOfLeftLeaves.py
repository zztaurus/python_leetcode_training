# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.sum = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.traverse(root)
        return self.sum

    def traverse(self, root):
        if not root:
            return
        if root.left and root.left.left is None and root.left.right is None:
            self.sum += root.left.val
        self.traverse(root.left)
        self.traverse(root.right)



class Solution2(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = 0

        isLeafNode = lambda node: not node.left and not node.right

        queue = [root]

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                if isLeafNode(node.left):
                    ans += node.val
                else:
                    queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans
