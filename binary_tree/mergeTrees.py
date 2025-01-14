
# 617 合并二叉树

"""

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。

你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；

否则，不为 null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

"""
from numpy.ma.core import left_shift


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def mergeTrees(self, root1, root2):
        """
        DFS
        """
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged


class Solution2(object):

    def mergeTrees(self, root1, root2):
        """
        BFS
        """

        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        queue = [merged]
        queue1 = [root1.left]
        queue2 = [root2]
        while queue and queue1 and queue2:
            node = queue.pop(0)
            root1 = queue1.pop(0)
            root2 = queue2.pop(0)
            left1, right1 = root1.left, root1.right
            left2, right2 = root2.left, root2.right

            if left1 or left2:
                if left1 and left2:
                    left = TreeNode(left1.val + left2.val)
                    node.left = left
                    queue.append(left)
                    queue1.append(left1)
                    queue2.append(left2)
                elif left1:
                    node.left = left1
                elif left2:
                    node.left = left2

            if right1 or right2:
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    node.right = right
                    queue.append(right)
                    queue1.append(right1)
                    queue2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2

        return merged






