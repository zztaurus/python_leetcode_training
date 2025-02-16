# Definition for a binary tree node.

# 129. 求根节点到叶节点数字之和

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):


    def __init__(self):
        self.path = ""
        self.res = 0

    def sumNumbers(self, root):
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return
        self.path += str(root.val)
        if not root.left and not root.right:
            self.res += int(self.path)

        self.traverse(root.left)
        self.traverse(root.right)

        self.path = self.path[:-1]


class Solution2(object):


    def sumNumbers(self, root):

        total = 0
        if not root:
            return total

        queue = [root]
        queue_num = [root.val]
        while queue:

            node = queue.pop(0)
            num = queue_num.pop(0)
            if not node.left and not node.right:
                total += num
            else:
                if node.left:
                    queue.append(node.left)
                    queue_num.append(num*10 + node.left.val)

                if node.right:
                    queue.append(node.right)
                    queue_num.append(num*10 + node.right.val)

        return total






