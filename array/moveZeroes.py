

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    left, right = 0, 0  # 双指针
    while(right <= len(nums) - 1):
        if nums[right] != 0:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
        right += 1



if __name__ == '__main__':
    pass

