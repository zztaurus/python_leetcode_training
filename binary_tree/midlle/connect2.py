
# Definition for a Node.

class Node(object):

    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

            # Initialize the queue with the root node
        queue = [root]

        while queue:
            size = len(queue)
            for i in range(size):
                # Pop the first node from the queue
                node = queue.pop(0)
                # If this is not the last node of the current level,
                # set its next pointer to the next node in the queue
                if i < size - 1:
                    node.next = queue[0]

                # Add the left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


class Solution2(object):

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

            # Initialize the queue with the root node
        queue = [root]

        while queue:
            size = len(queue)
            for i in range(size):
                # Pop the first node from the queue
                node = queue.pop(0)
                # If this is not the last node of the current level,
                # set its next pointer to the next node in the queue
                if i < size - 1:
                    node.next = queue[0]

                # Add the left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root



