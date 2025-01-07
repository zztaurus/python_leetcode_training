
# 226. 翻转二叉树

def invertTree(self, root):
    if not root:
        return None

    left_root =  self.invertTree(root.left)
    right_root = self.invertTree(root.right)
    root.right = left_root
    root.left = right_root
    return root


def invertTree2(root):
    if not root: return None
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
        node.left, node.right = node.right, node.left
    return root