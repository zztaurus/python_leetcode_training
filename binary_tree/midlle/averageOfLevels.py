
# Definition for a binary tree node.

# 637. 二叉树的层平均值

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        res = []
        queue = [root]
        while queue:
            count = 0
            sum_val = 0
            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                sum_val += node.val
                count += 1
            queue = next_queue
            print("sum_val: ", sum_val, " count: ", count,  " avg: ", round(sum_val / count,  5))
            avg_val = round(sum_val / count)
            res.append(avg_val)
        return res


class Solution2(object):

    def averageOfLevels(self, root):
        res = []
        queue = [root]
        while queue:
            count = len(queue)
            sum_val = 0
            next_queue = []
            for i in range(count):
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                node = queue.pop(0)
                sum_val += node.val
            avg_val = round(sum_val / count, 5)
            res.append(avg_val)
            queue = next_queue

        return res





