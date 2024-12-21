class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, node, visited):
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in self.graph[node]:
                self._dfs_recursive(neighbor, visited)

# Näide kasutamisest
if __name__ == "__main__":
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')
    g.add_node('F')

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    print("DFS algus sõlmest A:")
    g.dfs('A')

# Aja- ja ruumikomplekssus:
# Ajakomplekssus: O(V + E), kus V on sõlmede arv ja E on servade arv.
# Ruumikomplekssus: O(V), kuna peame hoidma külastatud sõlmede hulka.