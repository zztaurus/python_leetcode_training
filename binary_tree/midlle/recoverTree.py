from IPython.core.inputsplitter import num_ini_spaces


# 99. 恢复二叉搜索树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        nums = []
        self.inorder(root, nums)
        x, y = self.findtwoSwaped(root, nums)
        self.recover(root, 2, x, y)

    def inorder(self, root, nums):
        if root is None:
            return
        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)
        return nums

    def findtwoSwaped(self, nums):
        n = len(nums)
        index1, index2 = -1, -1
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                index2 = i + 1
                if index1 == -1:
                    index1 = i
                else:
                    break
        x, y = nums[index1], nums[index2]
        return x, y

    def recover(self, root, count, x, y):
        if root is not None:
            if root.val == x or root.val == y:
                root.val = y if root.val == x else x
                count -= 1
                if count == 0:
                    return
            self.recover(root.left, count, x, y)
            self.recover(root.right, count, x, y)




class Solution2:

    """


    方法一是显式地将中序遍历的值序列保存在一个 nums 数组中，然后再去寻找被错误交换的节点，但我们也可以隐式地在中序遍历的过程就找到被错误交换的节点 x 和 y。

    具体来说，由于我们只关心中序遍历的值序列中每个相邻的位置的大小关系是否满足条件，且错误交换后最多两个位置不满足条件，因此在中序遍历的过程我们只需要维护当前中序遍历到的最后一个节点 pred，

    然后在遍历到下一个节点的时候，看两个节点的值是否满足前者小于后者即可，如果不满足说明找到了一个交换的节点，且在找到两次以后就可以终止遍历。

    这样我们就可以在中序遍历中直接找到被错误交换的两个节点 x 和 y，不用显式建立 nums 数组。

    中序遍历的实现有迭代和递归两种等价的写法，在本方法中提供迭代实现的写法。使用迭代实现中序遍历需要手动维护栈。


    """
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """

        stack = []
        x = y = pred = None

        while stack or root:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 找到 x 和 y
            if pred is not None and root.val < pred.val:
                y = pred
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right
        self.swap(x, y)

    def swap(self, x, y):
        x.val, y.val = y.val, x.val

class Solution2:

    """

    Morris 遍历算法，该算法能将非递归的中序遍历空间复杂度降为 O(1)。

    Morris 遍历算法整体步骤如下（假设当前遍历到的节点为 x）：

    如果 x 无左孩子，则访问 x 的右孩子，即 x=x.right。
    如果 x 有左孩子，则找到 x 左子树上最右的节点（即左子树中序遍历的最后一个节点，x 在中序遍历中的前驱节点），我们记为 predecessor。根据 predecessor 的右孩子是否为空，进行如下操作。
        如果 predecessor 的右孩子为空，则将其右孩子指向 x，然后访问 x 的左孩子，即 x=x.left。
        如果 predecessor 的右孩子不为空，则此时其右孩子指向 x，说明我们已经遍历完 x 的左子树，我们将 predecessor 的右孩子置空，然后访问 x 的右孩子，即 x=x.right。
    重复上述操作，直至访问完整棵树。
    其实整个过程我们就多做一步：将当前节点左子树中最右边的节点指向它，这样在左子树遍历完成后我们通过这个指向走回了 x，且能再通过这个知晓我们已经遍历完成了左子树，而不用再通过栈来维护，省去了栈的空间复杂度。



    """
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """

        x = y = pred = predecessor = None

        while root:
            if root.left:
                #  predecessor 节点就是当前 root 节点向左走一步，然后一直向右走至无法走为止
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                # 让 predecessor 的右指针指向 root，继续遍历左子树
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    # 说明左子树已经访问完了，我们需要断开链接
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root

                    # 断开链接
                    predecessor.right = None
                    root = root.right
            else:
                # 如果没有左孩子，则直接访问右孩子
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root
                root = root.right
        self.swap(x, y)

    def swap(self, x, y):
        x.val, y.val = y.val, x.val




