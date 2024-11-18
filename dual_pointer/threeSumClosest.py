


def threeSumClosest(nums: object, target: object) -> object:
    most_res = 10000
    min_dis = 10000
    nums.sort()
    for first in range (len(nums) - 2):
        if first > 0 and nums[first] == nums[first - 1]:
            continue  # 这一步主要是要跳过重复元素, 避免结果中出现重复的三元组
        # 从此开始问题转变为 TwoSum 问题
        left, right = first + 1, len(nums) - 1
        while left < right:

            if nums[first] + nums[left] + nums[right] == target:
                return 0
            elif nums[first] + nums[left] + nums[right] > target:
                dis = abs(nums[first] + nums[left] + nums[right] - target)
                if dis < min_dis:
                    min_dis = dis
                    most_res = nums[first] + nums[left] + nums[right]
                right -= 1
            else:
                dis = abs(nums[first] + nums[left] + nums[right] - target)
                if dis < min_dis:
                    min_dis = dis
                    most_res = nums[first] + nums[left] + nums[right]
                left += 1
    return most_res


if __name__ == '__main__':
    print(threeSumClosest([-1,2,1,-4], 1))