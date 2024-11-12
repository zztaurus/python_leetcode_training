# 11 盛水最多的容器

def maxArea(height):

    left, right = 0, len(height) -1
    max_area = 0

    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area



