

# 455 分发饼干

def findContentChildren(g, s):

    g.sort()
    s.sort()

    m, n = len(g), len(s)
    i = j = count = 0
    while i < m and j < n:
        while j < n and g[i] < s[j]:
            j += 1
        if j < n:  # 此时有可能 j = n
            count += 1
        i += 1
        j += 1
    return count

