

def rotateArray(nums, k):
    n = len(nums)
    m = k % n
    nums[:] = nums[n-m:n] + nums[0:n-m]


def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # In case k is greater than the length of the array

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the rest
    reverse(k, n - 1)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotateArray(nums, 2)
    print(nums)

    nums = [1,2]
    rotateArray(nums, 5)
    print(nums)

    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(nums, 2)
    print(nums)

    nums = [1, 2]
    rotate_array(nums, 5)
    print(nums)