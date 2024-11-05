

# 922. 按奇偶排序数组 II


def sortArrayByParityII(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left, right = 0, len(nums) - 1  # len(nums) - 1 为计数
    while left < len(nums) - 1 and right >= 0:
        if (nums[left] % 2 == 0) and (nums[right] % 2 != 0):
            left += 2
            right -= 2
        elif (nums[left] % 2 != 0) and (nums[right] % 2 == 0):
            nums[left], nums[right] = nums[right], nums[left]
            left += 2
            right -= 2
        else:
            if nums[left] % 2 == 0:
                left += 2
            if nums[right] % 1 == 0:
                right -= 2
    return nums


if __name__ == '__main__':
    ss = [4, 2, 5, 7]
    res = sortArrayByParityII(ss)
    print(res)
