

# 教练使用整数数组 actions 记录一系列核心肌群训练项目编号。
# 为增强训练趣味性，需要将所有奇数编号训练项目调整至偶数编号训练项目之前。
# 请将调整后的训练项目编号以 数组 形式返回。


# 示例 1：
# 输入：actions = [1,2,3,4,5]
# 输出：[1,3,5,2,4]
# 解释：为正确答案之一


def traningPlan(actions):
    i,j = 0, 0
    while (j < len(actions)):
        if actions[i] %2 ==0:
            if actions[j] %2 !=0:
                actions[i], actions[j] = actions[j], actions[i]
                i += 1
                j += 1
            else:
                j += 1
        else:
            i += 1
            j += 1

    return actions


def traningPlan2(actions):
    left = 0
    right = 0
    while right < len(actions):
        if actions[right] % 2 == 1:
            actions[left], actions[right] = actions[right], actions[left]
            left += 1
        right += 1
    return actions


def traningPlan3(actions):
    left, right = 0, (len(actions) - 1)
    while left < right:
        while left < right and actions[right] %2 == 0:
            print(right)
            right -= 1
        while left < right and actions[left] %2 == 1:
            left += 1
        if left < right and actions[left] %2 == 0 and actions[right] %2 == 1:
            actions[left], actions[right] = actions[right], actions[left]
            left += 1
            right -= 1
    return actions



if __name__ == '__main__':
    res = traningPlan3([1,2,3,4,5])
    print(res)



