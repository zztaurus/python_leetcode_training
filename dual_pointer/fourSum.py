

def forSum(nums, target):

    res = []
    nums.sort()
    for first in range (len(nums) - 3):

        x = nums[first]

        if first > 0 and nums[first] == nums[first - 1]:
            continue  # 这一步主要是要跳过重复元素, 避免结果中出现重复的三元组
        if x + nums[first + 1] + nums[first + 2] + nums[first + 3] > target:  # 优化一 sum > target，由于数组已经排序，后面无论怎么选，选出的四个数的和不会比 s 还小，所以后面不会找到等于 target 的四数之和了
            break
        if x + nums[-3] + nums[-2] + nums[-1] < target:  # 优化二 由于数组已经排序，nums[a] 加上后面任意三个数都不会超过 s，所以无法在后面找到另外三个数与 nums[a] 相加等于 target。但是后面还有更大的 nums[a]，可能出现四数之和等于 target 的情况，所以还需要继续枚举，continue 外层循环。
            continue


        for second in range(first + 1, len(nums) - 2):
            y = nums[second]

            if second > (first + 1) and nums[second] == nums[second - 1]:
                continue

            if x + y + nums[second + 1] + nums[second + 2] > target:  # 优化一 sum > target，由于数组已经排序，后面无论怎么选，选出的四个数的和不会比 s 还小，所以后面不会找到等于 target 的四数之和了
                break
            if x + y + nums[-2] + nums[-1] < target:  # 优化二 由于数组已经排序，nums[a] 加上后面任意三个数都不会超过 s，所以无法在后面找到另外三个数与 nums[a] 相加等于 target。但是后面还有更大的 nums[a]，可能出现四数之和等于 target 的情况，所以还需要继续枚举，continue 外层循环。

                continue

            # 从此开始问题转变为 TwoSum 问题
            left, right = second + 1, len(nums) - 1
            while left < right:
                total = nums[first] + nums[second] + nums[left] + nums[right]
                if total == target:
                    res.append([nums[first], nums[second], nums[left], nums[right]])  # 保存满足条件的三元组
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total > target:
                    right -= 1
                else:
                    left += 1
    return res