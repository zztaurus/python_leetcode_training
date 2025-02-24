
# 404 左叶子之和

def sumOfLeftLeaves1(self, root):
    """
    DFS

    当且仅当左子节点是叶子节点时，

    """

    pass



def sumOfLeftLeaves2(self, root):
    """
    BFS

    层序遍历每一个节点，判断节点是否是左叶子节点，然后将左叶子节点的值相加

    """

    ans = 0

    isLeafNode = lambda node: not node.left and not node.right

    queue = [root]
    while queue:
        node = queue.pop(0)

        if node.left:
            if isLeafNode(node.left):
                ans += node.left.val
            else:
                queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return ans








