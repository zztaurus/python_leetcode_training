
# Definition for a binary tree node

# 965. 单值二叉树

# 深度优先搜索

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isUnivalTree(self, root):

        if not root:
            return True

        if root.left and root.val != root.left.val or not self.isUnivalTree(root.left):
            return False

        if root.right and root.val != root.right.val or not self.isUnivalTree(root.right):
            return False

        return True


# 广度优先搜索

class TreeNode2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isUnivalTree(self, root):

        if not root:
            return True

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                if node.val != node.left.val:
                    return False
                else:
                    queue.append(node.left)

            if node.right:
                if node.val != node.right.val:
                    return False
                else:
                    queue.append(node.right)
        return True






