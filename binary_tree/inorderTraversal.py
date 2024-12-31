
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
