
# 判断两个字符串是否互为重排字符串
# 排序
def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) != sorted(s2):
        return False
    return True


# 哈希表
def checkPermutation2(s1, s2):
    table = {}

    for i in s1:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1

    for j in s2:
        if j not in table:
            return False
        table[j] -= 1
        if table[j] < 0:
            return False

    return True

