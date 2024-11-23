
"""

1. MinHeap 类：实现了一个小顶堆的数据结构。
2. insert 方法：在堆中插入一个新元素，并通过 _heapify_up 方法调整堆以保持堆性质。
3. extract_min 方法：移除并返回堆中的最小元素（根节点），然后通过 _heapify_down 方法调整堆。
4. _heapify_up 方法：从插入位置向上调整堆，以保持堆性质。
5. _heapify_down 方法：从根节点向下调整堆，以保持堆性质。
6. get_min 方法：返回堆中的最小元素（根节点）而不移除它。
size 和 is_empty 方法：分别返回堆的大小和是否为空。

"""

class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("extract_min from an empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        if len(self.heap) == 0:
            raise IndexError("get_min from an empty heap")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0