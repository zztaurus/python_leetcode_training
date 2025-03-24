
# 637 二叉树的层平均值

class Solution1(object):

    def averageOfLevels(self, root):
        """
        DFS: 深度优先搜索
        """

        def dfs(root, level):
            if not root:
                return
            if level < len(totals):
                totals[level] += root.val
                counts[level] += 1
            else:
                totals.append(root.val)
                counts.append(1)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        counts = list()
        totals = list()
        dfs(root, 0)
        return [total / count for total, count in zip(totals, counts)]


class Solution2(object):

    def averageOfLevels(self, root):
        """
        BFS: 广度优先搜索
        """
        return self.bfs(root)

    def bfs(self, root):

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
            print("sum_val: ", sum_val, " count: ", count, " avg: ", round(sum_val // count, 5))
            avg_val = round(sum_val / count, 5)
            res.append(avg_val)
        return res





