

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    for first in (len(nums) - 1):
        if first > 0 and nums[first] == nums[first - 1]:
            continue # 这一步主要是要跳过重复元素, 避免结果中出现重复的三元组
        target =  0 - nums[first]

        # 从此开始问题转变为 TwoSum 问题
        left, right = first + 1, len(nums) - 1
        while left < right:

            if nums[left] + nums[right] == target:
                res.append([nums[first], nums[left], nums[right]]) # 保存满足条件的三元组
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
    return res





