
# 222. 完全二叉树的节点个数

"""

对于任意二叉树，都可以通过广度优先搜索或深度优先搜索计算节点个数，时间复杂度和空间复杂度都是 O(n)，其中 n 是二叉树的节点个数。

这道题规定了给出的是完全二叉树，因此可以利用完全二叉树的特性计算节点个数。

根据完全二叉树的特性可知，完全二叉树的最左边的节点一定位于最底层，因此从根节点出发，每次访问左子节点，直到遇到叶子节点，该叶子节点即为完全二叉树的最左边的节点，经过的路径长度即为最大层数 h。

"""


def countNodes(self, root):

    """

    递归的解法适用于所有二叉树，但是这种解法没有完全利用二叉树的特性

    """
    if root is None:
        return 0
    left_count = self.countNodes(root.left)
    right_count = self.countNodes(root.right)
    return left_count + right_count + 1


def countNodes2(self, root):

    """

    如果满二叉树的层数为h，则总节点数为：2^h - 1.

    那么我们来对 root 节点的左右子树进行高度统计，分别记为 left 和 right，有以下两种结果：

    left == right。这说明，左子树一定是满二叉树，因为节点已经填充到右子树了，左子树必定已经填满了。

        所以左子树的节点总数我们可以直接得到，是 2^left - 1，加上当前这个 root 节点，则正好是 2^left。再对右子树进行递归统计。

    left != right。说明此时最后一层不满，但倒数第二层已经满了，可以直接得到右子树的节点个数。同理，右子树节点 +root 节点，总数为 2^right。再对左子树进行递归查找。

    """

    if root is None:
        return 0
    left  = countLevel(root.left)
    right = countLevel(root.right)
    if left == right:
        return self.countNodes(root.right) + 1 << left
    else:
        return self.countNodes(root.left) + 1 << right


def countLevel(node):
    level = 0
    while node is not None:
        level += 1
        node = node.left
    return level

