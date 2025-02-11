
# 105. 从前序与中序遍历序列构造二叉树


"""

二叉树前序遍历的顺序为：

    先遍历根节点；

    随后递归地遍历左子树；

    最后递归地遍历右子树。

二叉树中序遍历的顺序为：

    先递归地遍历左子树；

    随后遍历根节点；

    最后递归地遍历右子树。

    在「递归」地遍历某个子树的过程中，我们也是将这颗子树看成一颗全新的树，按照上述的顺序进行遍历。挖掘「前序遍历」和「中序遍历」的性质，我们就可以得出本题的做法。

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.valToIndex = {}

    def buildTree(self, preorder, inorder):

        for i in range(len(inorder)):
            self.valToIndex[inorder[i]] = i

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd:
            return None

        # root 节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]
        # rootVal 在中序遍历数组中的索引
        index = self.valToIndex[rootVal]

        leftSize = index - inStart

        # 先构造出当前根节点
        root = TreeNode(rootVal)

        # 递归构造左右子树
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                               inorder, inStart, index - 1)

        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                inorder, index + 1, inEnd)
        return root


