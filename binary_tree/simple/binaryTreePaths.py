

# 257. 二叉树的所有路径


def binaryTreePaths1(root):
    """
    DFS

    达到节点，将节点值加入到path字符串中
        如果到达叶子节点时，得到一个完整路径，加入到路径列表中，深度搜索结束。
        如果未到达叶子节点，则继续向下搜索。

    """

    def construct_paths(root, path):

        if root:
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                path += "->"
                construct_paths(root.left, path)
                construct_paths(root.right, path)

    paths = []
    construct_paths(root, "")
    return paths


def binaryTreePaths2(root):
    """
    BFS

    使用到两个队列

    队列一: 存储 BFS 遍历时的节点

    队列二: 存储 队列一中从根节点到指定节点的路径

    """
    paths = []
    if not root:
        return paths
    node_queue = [root]
    path_queue = [str(root.val)]

    while node_queue:
        path = ""
        node = node_queue.pop(0)
        node_path = path_queue.pop(0)

        if not node.left and not node.right:
            paths.append(path)

        if not node.left:
            node_queue.append(node.left)
            path_queue.append(node_path + "->" + str(node.left.val))
        if not node.right:
            node_queue.append(node.right)
            path_queue.append(node_path + "->" + str(node.right.val))

    return paths

