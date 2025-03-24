
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):

        """

        二叉搜索树的中序遍历是升序序列，题目给定的数组是按照升序排序的有序数组，因此可以确保数组是二叉搜索树的中序遍历序列。

        给定二叉搜索树的中序遍历，是否可以唯一地确定二叉搜索树？答案是否定的。如果没有要求二叉搜索树的高度最小，则任何一个数字都可以作为二叉搜索树的根节点，因此可能的二叉搜索树有多个。

        如果二叉搜索树中有 n 个节点，则二叉搜索树的最小高度是 ⌊logn⌋，最大高度是 n−1。为了使二叉搜索树的高度最小，左右子树的节点数应尽可能接近，因此选择中间数字作为二叉搜索树的根节点，

            这样分给左右子树的数字个数相同或只相差 1，可以使得二叉搜索树的高度最小。如果数组长度是奇数，则根节点的选择是唯一的.

            如果数组长度是偶数，则可以选择中间位置左边的数字作为根节点或者选择中间位置右边的数字作为根节点，选择不同的数字作为根节点则创建的最小高度二叉搜索树也是不同的。

        确定最小高度二叉搜索树的根节点之后，其余的数字分别位于最小高度二叉搜索树的左子树和右子树中，左子树和右子树分别也是最小高度二叉搜索树，因此可以通过递归的方式创建最小高度二叉搜索树。

        递归的基准情形是最小高度二叉搜索树不包含任何数字，此时最小高度二叉搜索树为空。

        在给定中序遍历序列数组的情况下，每一个子树中的数字在数组中一定是连续的，因此可以通过数组下标范围确定子树包含的数字，下标范围记为 [left,right]。对于整个中序遍历序列，

        下标范围从 left=0 到 right=nums.length−1。当 left>right 时，最小高度二叉搜索树为空。

        以下三种方法中，方法一总是选择中间位置左边的数字作为根节点，方法二总是选择中间位置右边的数字作为根节点，方法三是方法一和方法二的结合，选择任意一个中间位置数字作为根节点。


        """

        def helper(nums, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums, left, mid - 1)
            root.right = helper(nums, mid + 1, right)

            return root
        return helper(nums, 0, len(nums) - 1)


