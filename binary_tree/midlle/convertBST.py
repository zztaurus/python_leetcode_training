
# Definition for a binary tree node.

# 538 把二叉搜索树转换为累加树


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def reverse_inorder(node, acc_sum):
            if not node:
                return acc_sum
            # Traverse the right subtree first
            acc_sum = reverse_inorder(node.right, acc_sum)
            # Update the current node's value
            node.val += acc_sum
            # Update the accumulated sum
            acc_sum = node.val
            # Traverse the left subtree
            return reverse_inorder(node.left, acc_sum)

        reverse_inorder(root, 0)
        return root



