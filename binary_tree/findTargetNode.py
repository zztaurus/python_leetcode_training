
# LCR 174. 寻找二叉搜索树中的目标节点

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    """

    1. 中序遍历的倒序遍历

    递归解析：
        终止条件： 当节点 root 为空（越过叶节点），则直接返回；

        递归右子树： 即 dfs(root.right) ；
        递推工作：
            提前返回： 若 cnt=0 ，代表已找到目标节点，无需继续遍历，因此直接返回；
            统计序号： 执行 cnt=cnt−1 （即从 cnt 减至 0 ）；
            记录结果： 若 cnt=0 ，代表当前节点为第 cnt 大的节点，因此记录 res=root.val ；
        递归左子树： 即 dfs(root.left) ；


    """

    def findTargetNode(self, root, cnt):

        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.cnt == 0: return
            self.cnt -= 1
            if self.cnt == 0: self.res = root.val
            dfs(root.left)

        self.cnt = cnt
        dfs(root)
        return self.res





