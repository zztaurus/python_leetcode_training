
# 543. 二叉树的直径

"""

假设我们知道对于该节点的左儿子向下遍历经过最多的节点数 L （即以左儿子为根的子树的深度） 和其右儿子向下遍历经过最多的节点数 R （即以右儿子为根的子树的深度）

那么以该节点为起点的路径经过节点数的最大值即为 L+R+1 。

我们记节点 node 为起点的路径经过节点数的最大值为 dNode, ，那么二叉树的最大直径就是所有节点 dNode的最大值减一。


"""


def diameterOfBinaryTree(root):
    """

    本质是利用后序遍历的逻辑, 知道左子树的深度，右子树的深度，包含当前的节点的做大路径的值 左子树深度 + 右子树深度

    """
    ans = -1
    def depth(node):
        if node is None:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        ans = max(ans, left_depth + right_depth + 1)
        return 1 + max(left_depth, right_depth)
    depth(root)
    return ans - 1






