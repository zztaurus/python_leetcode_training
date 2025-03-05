
# Definition for a binary tree node.

# 101. 对称二叉树
# 思路一: 对左子树左右交换 或者 右子树左右交换
# 思路二: 分别对左子树和右子树进行中序遍历，遍历结果应该互为翻转


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1(object):

    def isSymmetric(self, root):
        return self.check(root.left, root.right)

    def check(self, p, q):  # 借助队列迭代
        queue = [p, q]
        while len(queue) > 0:
            u = queue.pop(0)
            v = queue.pop(0)

            if u is None and v is None:
                continue

            if u is None or v is None or u.val != v.val:
                return False

            queue.append(u.left)
            queue.append(v.right)

            queue.append(u.right)
            queue.append(v.left)

        return True


class Solution2(object):

    def isSymmetric(self, root):
        return self.check(root.left, root.right)

    def check(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)
