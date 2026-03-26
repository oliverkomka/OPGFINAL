import sys
sys.setrecursionlimit(50000)


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class TreeSort:
    def __init__(self):
        self.comparisons = 0
        self.assignments = 0
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            self.assignments += 1
            return
        current = self.root
        while True:
            self.comparisons += 1
            if key < current.key:
                if current.left is None:
                    current.left = TreeNode(key)
                    self.assignments += 1
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(key)
                    self.assignments += 1
                    return
                current = current.right

    def inorder(self, node, result):
        if node is not None:
            self.inorder(node.left, result)
            result.append(node.key)
            self.assignments += 1
            self.inorder(node.right, result)

    def sort(self, arr):
        self.comparisons = 0
        self.assignments = 0
        self.root = None
        for x in arr:
            self.insert(x)
        result = []
        self.inorder(self.root, result)
        return result


def tree_sort(arr, length=None):
    """Wrapper funkcia pre kompatibilitu so zvysnymi algoritmami."""
    sorter = TreeSort()
    sorted_arr = sorter.sort(arr)
    return sorted_arr, sorter.comparisons, sorter.assignments
