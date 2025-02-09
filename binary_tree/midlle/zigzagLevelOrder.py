
# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    """

    数组反转

    """

    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        queue = deque([root])
        left_to_right = True
        while queue:
            level = []
            count = len(queue)
            for i in range(count):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if not left_to_right:
                level.reverse()
            res.append(level)
            left_to_right = not left_to_right
        return res





class Solution2:


    """

    双端队列

    """

    def zigzagLevelOrder(self, root):
        ans = []
        if not root:
            return ans

        node_queue = deque([root])
        is_order_left = True

        while node_queue:
            level_list = deque()
            size = len(node_queue)
            for _ in range(size):
                cur_node = node_queue.popleft()
                if is_order_left:
                    level_list.append(cur_node.val)
                else:
                    level_list.appendleft(cur_node.val)

                if cur_node.left:
                    node_queue.append(cur_node.left)
                if cur_node.right:
                    node_queue.append(cur_node.right)

            ans.append(list(level_list))
            is_order_left = not is_order_left

        return ans


