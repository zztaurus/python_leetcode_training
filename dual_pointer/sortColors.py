

# 单指针解法

def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    n = len(nums)
    ptr = 0
    for i in range(n):
        if nums[i] == 0:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
        i += 1

    for i in range(ptr, n):
        if nums[i] == 1:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
        i += 1


def sortColors2(nums):
    n = len(nums)
    p0 = 0
    p2 = n - 1
    for i in range(n):
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1
        if i < p2 and nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
        i += 1

def sortColors3(nums):
    p0 = 0
    p1 = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == 1:
            nums[i], nums[p1] = nums[p1], nums[i]
            p1 += 1
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            if p0 < p1:
                nums[i], nums[p1] = nums[p1], nums[i]
            p0 += 1
            p1 += 1 # p1 指针一定在p0之后，所有每次 p0 + 1, 那么 p1 + 1

        i += 1


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    sortColors3(nums)
    print(nums)
