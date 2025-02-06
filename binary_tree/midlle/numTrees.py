
# 96. 不同的二叉搜索树

class Solution:

    def numTrees(self, n: int) -> int:

        """

        - 设 `G(n)` 表示由 `n` 个节点组成的不同二叉搜索树的种数。

        - 对于一个二叉搜索树，以 `i` 为根节点时，左子树有 `i-1` 个节点，右子树有 `n-i` 个节点。


           - 因此，`G(n)` 可以表示为：
                G(n): 累加(1-n)：G(i−1)×G(n−i)


        - 使用动态规划数组 `dp`，其中 `dp[i]` 表示 `G(i)`。

        - 初始化 `dp[0] = 1` 和 `dp[1] = 1`。

        - 通过双重循环计算 `dp[i]`，外层循环遍历节点数 `i`，内层循环遍历根节点 `j`。

        """

        dp = [0] * (n + 1)

        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j - 1]

        return dp[n]





