"""
cursor_module.py
A collection of classic data structures and algorithms with doctest-based tests.
Inspired by TheAlgorithms and context7 best practices.
"""

from collections import deque


# ------------------ Binary Tree ------------------
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert data into the binary tree (level order).
        >>> bt = BinaryTree()
        >>> for v in [1, 2, 3]:
        ...     bt.insert(v)
        >>> bt.root.data, bt.root.left.data, bt.root.right.data
        (1, 2, 3)
        """
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            return
        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.left:
                node.left = new_node
                return
            elif not node.right:
                node.right = new_node
                return
            else:
                q.append(node.left)
                q.append(node.right)

    def inorder(self):
        """
        Inorder traversal (left, root, right).
        >>> bt = BinaryTree()
        >>> for v in [1, 2, 3]:
        ...     bt.insert(v)
        >>> list(bt.inorder())
        [2, 1, 3]
        """

        def _inorder(node):
            if node:
                yield from _inorder(node.left)
                yield node.data
                yield from _inorder(node.right)

        return _inorder(self.root)

    def preorder(self):
        """
        Preorder traversal (root, left, right).
        >>> bt = BinaryTree()
        >>> for v in [1, 2, 3]:
        ...     bt.insert(v)
        >>> list(bt.preorder())
        [1, 2, 3]
        """

        def _preorder(node):
            if node:
                yield node.data
                yield from _preorder(node.left)
                yield from _preorder(node.right)

        return _preorder(self.root)

    def postorder(self):
        """
        Postorder traversal (left, right, root).
        >>> bt = BinaryTree()
        >>> for v in [1, 2, 3]:
        ...     bt.insert(v)
        >>> list(bt.postorder())
        [2, 3, 1]
        """

        def _postorder(node):
            if node:
                yield from _postorder(node.left)
                yield from _postorder(node.right)
                yield node.data

        return _postorder(self.root)

    def bfs(self):
        """
        Level-order (BFS) traversal.
        >>> bt = BinaryTree()
        >>> for v in [1, 2, 3]:
        ...     bt.insert(v)
        >>> list(bt.bfs())
        [1, 2, 3]
        """
        if not self.root:
            return
        q = deque([self.root])
        while q:
            node = q.popleft()
            yield node.data
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


# ------------------ Graph ------------------
class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        """
        Add an edge to the graph (undirected).
        >>> g = Graph()
        >>> g.add_edge(1, 2)
        >>> g.add_edge(1, 3)
        >>> sorted(g.adj[1])
        [2, 3]
        """
        self.adj.setdefault(u, set()).add(v)
        self.adj.setdefault(v, set()).add(u)

    def bfs(self, start):
        """
        Breadth-first search from start node.
        >>> g = Graph()
        >>> g.add_edge(1, 2)
        >>> g.add_edge(1, 3)
        >>> list(g.bfs(1))
        [1, 2, 3]
        """
        visited = set()
        q = deque([start])
        while q:
            node = q.popleft()
            if node not in visited:
                yield node
                visited.add(node)
                q.extend(self.adj.get(node, []) - visited)

    def dfs(self, start):
        """
        Depth-first search from start node.
        >>> g = Graph()
        >>> g.add_edge(1, 2)
        >>> g.add_edge(1, 3)
        >>> list(g.dfs(1))
        [1, 2, 3]
        """
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                yield node
                visited.add(node)
                stack.extend(self.adj.get(node, []) - visited)


# ------------------ Famous Algorithms ------------------


def binary_search(arr, target):
    """
    Binary search on sorted array.
    >>> binary_search([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search([1, 2, 3, 4, 5], 6)
    -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bubble_sort(arr):
    """
    Bubble sort (returns sorted copy).
    >>> bubble_sort([3, 1, 2])
    [1, 2, 3]
    """
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def quick_sort(arr):
    """
    Quick sort (returns sorted copy).
    >>> quick_sort([3, 1, 2])
    [1, 2, 3]
    """
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def dijkstra(graph, start):
    """
    Dijkstra's shortest path algorithm (returns distances dict).
    >>> g = {0: {1: 2, 2: 4}, 1: {2: 1}, 2: {3: 1}, 3: {}}
    >>> dijkstra(g, 0)
    {0: 0, 1: 2, 2: 3, 3: 4}
    """
    import heapq

    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u].items():
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist


if __name__ == "__main__":
    import doctest

    doctest.testmod()
