# 101 对称二叉树
# 思路一: 对左子树左右交换 或者 右子树左右交换
# 思路二: 分别对左子树和右子树进行中序遍历，遍历结果应该互为翻转


def isSymmetric(root):
    if root is None:
        return True
    elif root.left is None and root.right is None:
        return True
    else:
        left_res = inorder_traversal(root.left)
        right_res = inorder_traversal(root.right)
        print(left_res)
        print(right_res)
        if left_res == reversed(right_res):
            return True
        else:
            return False


def inorder_traversal(root):
    """中序遍历：左 -> 根 -> 右"""
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def isSymmetric2(self, root):
    return self.check(root.left, root.right)

def check(self, p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    else:
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)



def isSymmetric3(self, root):
    return self.check(root.left, root.right)

def check(self, p, q): # 借助队列迭代
    queue = [p, q]
    while len(queue) > 0:
        u = queue.pop(0)
        v = queue.pop(0)

        if u is None and v is None:
            continue

        if u is None or v is None or u.val != v.val:
            return False

        queue.append(u.left)
        queue.append(v.right)

        queue.append(u.right)
        queue.append(v.left)


    return True




