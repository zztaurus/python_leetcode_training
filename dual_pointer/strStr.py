

'''
找出字符串中第一个匹配项的下标
'''

def strStr(haystack, needle):
    '''

    朴素匹配算法
    :param haystack:
    :param needle:
    :return:
    '''
    h_len = len(haystack)
    n_len = len(needle)

    if n_len == 0:
        return 0

    for i in range(0, h_len - n_len):
        if haystack[i:i+n_len] == needle:
            return i
    return -1



def strStr2(haystack, needle):
    pass




