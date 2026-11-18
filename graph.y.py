from collections import deque


class CapucongGraph:

    def __init__(self):
        self.labels = {
            0: "C",
            1: "A",
            2: "P",
            3: "U",
            4: "C",
            5: "O",
            6: "N",
            7: "G",
        }
        self.adj = {
            0: [1, 2],  # C (0) -> A (1), P (2)
            1: [0, 3, 4],  # A (1) -> C (0), U (3), C (4)
            2: [0, 5, 6],  # P (2) -> C (0), O (5), N (6)
            3: [1, 7],  # U (3) -> A (1), G (7)
            4: [1],  # C (4) -> A (1)
            5: [2],  # O (5) -> P (2)
            6: [2, 7],  # N (6) -> P (2), G (7)
            7: [3, 6],  # G (7) -> U (3), N (6)
        }

    def bfs(self, start=0):
        visited = {start}
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(self.labels[vertex])
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start=0):
        visited = set()
        result = []

        def traverse(vertex):
            visited.add(vertex)
            result.append(self.labels[vertex])
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    traverse(neighbor)

        traverse(start)
        return result


if __name__ == "__main__":
    graph = CapucongGraph()

    print("II. GRAPH (CAPUCONG)")
    print("BFS Traversal Result:", " -> ".join(graph.bfs(0)))
    print("DFS Traversal Result:", " -> ".join(graph.dfs(0)))