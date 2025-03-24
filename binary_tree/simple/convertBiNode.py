
# Definition for a binary tree node.

"""
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。

实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def convertBiNode(self, root):

        def inorder(node):
            nonlocal last, head
            if node is None:
               return

            inorder(node.left) # 如果左子树不为空, 则 last 和 head 均存在

            if last:
                last.right = node # 如果前驱节点存在，则当前节点为前驱节点的右子节点
            else:
                head = node # 如果前驱节点不存在，则当前节点为头结点
            node.left = None # 删除当前节点的左指针
            last = node # 更新当前节点为新的前驱节点，然后遍历右子树

            inorder(node.right)

        last, head = None, None
        inorder(root)
        return head





