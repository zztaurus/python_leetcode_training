
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def tree2str(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """

        if not root:
            return ""

        if not root.left and not root.right:
            return str(root.val)

        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)

        if root.left is not None and root.right is None:
            #忽略空的右子树
            return f"{root.val}({left_str})"

        if root.left is None and root.right is not None:
            #空的左子树不能忽略
            return f"{root.val}()({right_str})"

        return f"{root.val}({left_str})({right_str})"


