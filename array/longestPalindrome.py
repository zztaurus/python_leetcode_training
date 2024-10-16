
def longestPalindrome(s):
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
    return s[l + 1: r]