
# 106 从中序遍历和后序遍历序列构造二叉树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.valToIndex = {}

    def buildTree(self, inorder, postOrder):

        for i in range(len(inorder)):
            self.valToIndex[inorder[i]] = i
        return self.build(postOrder, 0, len(postOrder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, postOrder, postStart, postEnd, inorder, inStart, inEnd):
        if postStart > postEnd:
            return None

        # root 节点对应的值就是前序遍历数组的第一个元素
        rootVal = postOrder[postEnd]
        # rootVal 在中序遍历数组中的索引
        index = self.valToIndex[rootVal]

        leftSize = index - inStart

        # 先构造出当前根节点
        root = TreeNode(rootVal)

        # 递归构造左右子树
        root.left = self.build(postOrder, postStart,  postStart + leftSize-1,
                               inorder, inStart, index - 1)

        root.right = self.build(postOrder, postStart + leftSize, postEnd - 1,
                                inorder, index + 1, inEnd)
        return root