

def inorderTraversal2(root):
    white, gray = 0, 1
    res = []
    stack = []
    stack.append((white, root))
    while stack:
        color, node = stack.pop()
        if node is None: continue
        if color == white:
            stack.append((white, node.right))
            stack.append((gray, node))
            stack.append((white, node.left))
        else:
            res.append(node.val)
    return res
