
# 二叉树中序遍历


def inorderTraversal(root):
    res = []
    traverse(root.left, res)
    return res

def traverse(root, res):
    if not root:
        return res
    traverse(root.left, res)
    res.append(root.val)
    traverse(root.left, res)


def inorderTraversal2(root):

    res, stack = [], []
    current = root

    while current or stack:
        # Reach the leftmost node of the current node
        while current: # 首先找到整个树的最左子树
            stack.append(current)
            current = current.left

        # Current must be None at this point
        current = stack.pop()
        res.append(current.val)  # Add the node value to the result

        # We have visited the node and its left subtree. Now, it's right subtree's turn
        current = current.right

    return res
