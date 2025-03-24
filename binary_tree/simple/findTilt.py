

# 563. 二叉树的坡度


"""

一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。

如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。

整个树 的坡度就是其所有节点的坡度之和。

"""


def findTilt(root):

    """

    操作逻辑：后序遍历

    """

    left = dfs(root.left)
    right = dfs(root.right)

    # 后序逻辑
    # if left and right:


def dfs(node):
    pass


def dfs(node):
    pass

