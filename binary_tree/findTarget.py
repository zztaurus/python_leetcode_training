
# 653. 两数之和 IV - 输入二叉搜索树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:

    def findTarget(self, root, k):
        """
        中序遍历，得到一个递增的序列, 然后问题转换为 two-sum 问题

        中序遍历 + 双指针
        """

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        res = []
        dfs(root)
        i, j = 0, len(res) - 1
        while i < j:
            if res[i] + res[j] == k:
                return True
            elif res[i] + res[j] > k:
                j -= 1
            else:
                i += 1
        return False


class Solution2:

    def findTarget(self, root, k):
        """
        深度优先搜索 + 哈希表, 在搜索二叉树的过程中完成目标值检测
        """
        def dfs(root):
            if not root:
                return False
            les = k - root.val
            if les in target_set:
                return True
            else:
                target_set.add(root.val)
                return dfs(root.left) or dfs(root.right)
        target_set = set()
        return dfs(root)



# 本质上的问题可以拆解为数的中序遍历和Two-Sum问题.


