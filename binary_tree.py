from collections import deque

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_binary_tree(letters):
    if not letters:
        return None
    nodes = [Node(ch) for ch in letters]
    for i in range(len(nodes)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(nodes):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(nodes):
            nodes[i].right = nodes[right_idx]
    return nodes[0]


def bfs_tree(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def dfs_tree(root):
    result = []

    def traverse(node):
        if not node:
            return
        result.append(node.value)  # Visit root node
        traverse(node.left)  # Traverse left subtree
        traverse(node.right)  # Traverse right subtree

    traverse(root)
    return result


if __name__ == "__main__":
    word = "CAPUCONG"
    root = build_binary_tree(word)

    print("I. BINARY TREE (CAPUCONG)")
    print("BFS Traversal Result:", " -> ".join(bfs_tree(root)))
    print("DFS Traversal Result:", " -> ".join(dfs_tree(root)))