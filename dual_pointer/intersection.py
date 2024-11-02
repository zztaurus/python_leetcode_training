
# 349 两个数组的交集

# 1. 双重遍历，时间复杂度：O(mn), 空间复杂度： O(1)
# 2. 哈希表: 时间复杂度：O(m), 空间复杂度： O(n)
# 3. 排序 + 双指针 时间复杂度 (mlogm + nlogn)

def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return list(set(nums1) & set(nums2))


def intersection2(nums1, nums2):
    nums1.sort()
    nums2.sort()
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            if nums1[i] not in res:
                res.appedn(nums1[i])
            i += 1
            j += 1
    return res
