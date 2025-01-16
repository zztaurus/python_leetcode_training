# 671. 二叉树中第二小的节点


"""

一个朴素的做法是，直接对树进行遍历（广度 & 深度），使用 HashSet 进行存储，得到所有去重后的节点大小。

然后找次小值的方式有多种：可以通过排序找次小值，复杂度为 O(nlogn)；也可以使用经典的两个变量 & 一次遍历的方式，找到次小值，复杂度为 O(n)。

"""

class Solution1:
    def __init__(self):
        self.set = set()

    def findSecondMinimumValue(self, root):
        self.dfs(root)
        if len(self.set) < 2:
            return -1
        else:
            return list(self.set)[1]

    def dfs(self, root):
        if root is None:
            return
        self.set.add(root.val)
        self.dfs(root.left)
        self.dfs(root.right)



"""

根据题目中的描述「如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个」，我们可以知道，对于二叉树中的任意节点 x，x 的值不大于其所有子节点的值，因此：

对于二叉树中的任意节点 x，x 的值不大于以 x 为根的子树中所有节点的值。

令 x 为二叉树的根节点，此时我们可以得出结论：

二叉树根节点的值即为所有节点中的最小值。

因此，我们可以对整棵二叉树进行一次遍历。设根节点的值为 rootvalue，我们只需要通过遍历，找出严格大于 rootvalue 的最小值，即为「所有节点中的第二小的值」。


"""


class Solution2:
    def __init__(self):
        self.ans = -1

    def findSecondMinimumValue(self, root):
        self.dfs(root, root.val)
        return self.ans

    def dfs(self, root, cur):
        if root is None:
            return
        if root.val != cur: # 当前节点非根节点且当前值不等于根节点的值
            if self.ans == -1:
                self.ans = root.val
            else:
                self.ans = min(self.ans, root.val)
            return
        self.dfs(root.left, cur)
        self.dfs(root.right, cur)

