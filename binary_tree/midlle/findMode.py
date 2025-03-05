
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        answer = {}
        def dfs(node):

            if node is None:
                return
            dfs(node.left)
            x = node.val
            if x in answer:
                answer[x] += 1
            else:
                answer[x] = 1
            dfs(node.right)

        dfs(root)
        return self.find_most_frequent_key(answer)

    def find_most_frequent_key(self, hash_table):
        # Initialize variables to track the most frequent key and its count
        most_frequent_keys = []
        max_count = 0

        # Iterate over the hash table
        for key, count in hash_table.items():
            if count > max_count:
                # Found a new maximum count, update the list and max_count
                most_frequent_keys = [key]
                max_count = count
            elif count == max_count:
                # If the current count equals max_count, add the key to the list
                most_frequent_keys.append(key)

        return most_frequent_keys


class Solution2(object):

    def findMode(self, root):

        if root is None:
            return []

        self.current_val = None
        self.max_count = 0
        self.current_count = 0
        self.modes = []

        def inOrder(root):

            if root is None:
                return

            inOrder(root.left)
            if root.val != self.current_val:
                self.current_val = root.val
                self.current_count = 1
            else:
                self.current_count += 1

            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [self.current_val]
            elif self.current_count == self.max_count:
                self.modes.append(self.current_val)
            inOrder(root.right)

        inOrder(root)
        return self.modes



