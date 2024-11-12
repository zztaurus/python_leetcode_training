
def longest_palindrome_v1(s):
    """
    :type s: str
    :rtype: str
    """

    res = ""
    for i in range(0, len(s)):
        # 以 s[i] 为中心的最长回文子串
        s1 = palindrome(s, i, i) # 奇数回文串
        # 以 s[i] 和 s[i+1] 为中心的最长回文子串
        s2 = palindrome(s, i, i + 1) # 偶数回文串
        # res = longest(res, s1, s2)
        res = s1 if len(res) < len(s1) else res
        res = s2 if len(res) < len(s2) else res
    return res

def palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1: r] # 以 l, r 为左右边界的最长回文串


# 在状态转移方程中，我们是从长度较短的字符串向长度较长的字符串进行转移的，因此一定要注意动态规划的循环顺序。

def longest_palindrome_v2(s: str) -> str:
    n = len(s)
    if n < 2:
        return s

    # Initialize a table to store palindrome status
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length greater than 2
    for length in range(3, n + 1):  # length is the length of the substring
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index of the current substring
            # Check if the current substring is a palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length

    return s[start:start + max_length]

