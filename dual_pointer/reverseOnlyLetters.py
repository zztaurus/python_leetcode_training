

# 917, 仅仅翻转字母


def reverseOnlyLetters(s):
    """
    :type s: str
    :rtype: str
    """
    ans = list(s)
    left, right = 0, len(ans) - 1
    while (left < right):
        while(left < right and not ans[left].isalpha()):
            left += 1
        while(left < right and not ans[right].isalpha()):
            right -= 1
        ans[left], ans[right] = ans[right], ans[left]
        left += 1
        right -= 1
    return ''.join(ans)

