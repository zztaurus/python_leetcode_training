
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.size = 1  # Size of the subtree rooted at this node


class MyTreeMap:
    def __init__(self):
        self.root = None

    def _put(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _get(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.value

    def get(self, key):
        return self._get(self.root, key)

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def _max(self, node):
        if node.right is None:
            return node
        return self._max(node.right)

    def first_key(self):
        if self.root is None:
            return None
        return self._min(self.root).key

    def last_key(self):
        if self.root is None:
            return None
        return self._max(self.root).key

    def _floor(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._floor(node.left, key)
        t = self._floor(node.right, key)
        if t is not None:
            return t
        return node

    def floor_key(self, key):
        node = self._floor(self.root, key)
        if node is None:
            return None
        return node.key

    def _ceiling(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key > node.key:
            return self._ceiling(node.right, key)
        t = self._ceiling(node.left, key)
        if t is not None:
            return t
        return node

    def ceiling_key(self, key):
        node = self._ceiling(self.root, key)
        if node is None:
            return None
        return node.key

    def _rank(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(node.right, key)
        else:
            return self._size(node.left)

    def rank(self, key):
        return self._rank(self.root, key)

    def _select(self, node, k):
        if node is None:
            return None
        t = self._size(node.left)
        if t > k:
            return self._select(node.left, k)
        elif t < k:
            return self._select(node.right, k - t - 1)
        else:
            return node

    def select_key(self, k):
        node = self._select(self.root, k)
        if node is None:
            return None
        return node.key

    def _range_keys(self, node, low, high, keys):
        if node is None:
            return
        if low < node.key:
            self._range_keys(node.left, low, high, keys)
        if low <= node.key <= high:
            keys.append(node.key)
        if high > node.key:
            self._range_keys(node.right, low, high, keys)

    def range_keys(self, low, high):
        keys = []
        self._range_keys(self.root, low, high, keys)
        return keys

    def _size(self, node):
        if node is None:
            return 0
        return node.size