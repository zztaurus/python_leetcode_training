# Definition for a binary tree node.


# 897. 递增顺序搜索树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res_node = None

    def increasingBST(self, root):
        # 创建一个 dummpy 节点
        dummpy_node = TreeNode(-1)
        self.res_node = dummpy_node
        self.inorder(root)
        return dummpy_node.right

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)

        self.res_node.right = node
        node.left = None
        self.res_node = node

        self.inorder(node.right)



