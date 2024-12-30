

def isSameTree(root1, root2):
    res1 = []
    res2 = []
    traverse(root1, res1)
    traverse(root2, res2)
    if res1 == res2:
        return True
    else:
        return False

def traverse(root, res):
    if not root:
        return res
    traverse(root.left, res)
    res.append(root.val)
    traverse(root.left, res)


def isSameTree2(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    else:
        return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)