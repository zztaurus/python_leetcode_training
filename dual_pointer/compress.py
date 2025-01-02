
# 443 压缩字符串 


def compress(chars):

    def reverse(left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    res = []
    n = len(chars)
    write, left = 0, 0
    for read in range(n):
        if read != n - 1 and chars[read] != chars[read + 1]:
            res[write] = chars[read]
            write += 1
            num = read - left + 1
            if num > 1:
                anchor = write
                while num > 0:
                    chars[write] = str(num % 10)
                    write += 1
                    num //= 10
                reverse(anchor, write - 1) # 为了达到 O(1) 空间复杂度，我们需要自行实现将数字转化为字符串写入到原字符串的功能。这里我们采用短除法将子串长度倒序写入原字符串中，然后再将其反转即可。
            left = read + 1
    return write



