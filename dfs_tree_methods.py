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


def preorder(root):
    result = []

    def traverse(node):
        if not node:
            return
        result.append(node.value)   # Root
        traverse(node.left)         # Left
        traverse(node.right)        # Right

    traverse(root)
    return result


def inorder(root):
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)         # Left
        result.append(node.value)   # Root
        traverse(node.right)        # Right

    traverse(root)
    return result


def postorder(root):
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)         # Left
        traverse(node.right)        # Right
        result.append(node.value)   # Root

    traverse(root)
    return result


if __name__ == "__main__":
    name_tree = "JAMAICACAPUCONG"
    root = build_binary_tree(name_tree)

    print("Assessment 3.6: DFS Methods in Tree (JAMAICACAPUCONG)")
    print("Preorder  (Root -> Left -> Right):", " -> ".join(preorder(root)))
    print("Inorder   (Left -> Root -> Right):", " -> ".join(inorder(root)))
    print("Postorder (Left -> Right -> Root):", " -> ".join(postorder(root)))