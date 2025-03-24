
# Definition for a binary tree node.

# LCR 150. 彩灯装饰记录 II

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def decorateRecord(self, root):

        res = []
        if not root:
            return res

        queue = [root]
        while queue:
            sub_res = []
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                sub_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sub_res)

        return  res






