
# 283:移动零。给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    """
    
    思路及解法

        使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
        
        右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。
        
        注意到以下性质：
        
        左指针左边均为非零数；
        
        右指针左边直到左指针处均为零。
        
        因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变。
    
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

