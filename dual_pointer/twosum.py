
'''
两数之和- 输入有序序列

给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。

如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。


'''

def solution(numbers, target):

    i,j = 0, len(numbers) - 1

    while(i < j):
        val = numbers[i] + numbers[j]
        if val < target:
            i += 1
        elif val > target:
            j -= 1
        else:
            return i+1, j+1


if __name__ == '__main__':
    print(solution([2,7,11,13,15], 9))

