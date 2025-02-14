
# Definition for a Node.

# 116. 填充每个节点的下一个右侧节点指针

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
        if not root:
            return None

        self.traverse(root.left, root.right)
        return root


    def traverse(self, node1, node2):
        if not node1 and not node2:
            return

        node1.next = node2

        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        self.traverse(node1.right, node2.left)

