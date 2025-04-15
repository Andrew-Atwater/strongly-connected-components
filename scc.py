from collections import defaultdict
from typing import List, Set, Dict, Union, Collection

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def addEdge(self, u: str, v: str) -> None:
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
    
    def transpose(self) -> 'Graph':
        g_transpose = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                g_transpose.addEdge(v, u)
        return g_transpose
    
    def dfsUtil(self, v: str, visited: Set[str], collection: Union[List[str], Set[str]] = None) -> None:
        visited.add(v)
        for u in self.graph.get(v, []):
            if u not in visited:
                self.dfsUtil(u, visited, collection)
        if collection is not None:
            if isinstance(collection, list):
                collection.append(v)
            else:
                collection.add(v)
    
    def getComponents(self) -> List[Set[str]]:
        visited = set()
        finish_order = []
        for vertex in sorted(self.vertices):
            if vertex not in visited:
                self.dfsUtil(vertex, visited, finish_order)
        transpose = self.transpose()
        visited = set()
        components = []
        
        for vertex in reversed(finish_order):
            if vertex not in visited:
                component = set()
                transpose.dfsUtil(vertex, visited, component)
                components.append(component)
        
        return components

    def createMatrix(self, components: List[Set[str]]) -> Dict:
        vertex_to_component = {}
        for i, component in enumerate(components):
            for vertex in component:
                vertex_to_component[vertex] = i
        
        n = len(components)
        matrix = defaultdict(lambda: defaultdict(int))
        
        for u in self.graph:
            for v in self.graph[u]:
                comp_u = vertex_to_component[u]
                comp_v = vertex_to_component[v]
                if comp_u != comp_v: 
                    matrix[comp_u][comp_v] += 1
        
        return matrix

def readGraph(filename: str) -> Graph:
    g = Graph()
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) != 2:
                    continue
                    
                source = parts[0].strip()
                targets = parts[1].strip().split()
                
                for target in targets:
                    g.addEdge(source, target)                
                if not targets:
                    g.vertices.add(source)
                    
        return g
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def printMatrix(components: List[Set[str]], matrix: Dict) -> None:
    n = len(components)
    
    print("   ", end="")
    for i in range(n):
        component_str = f"[{''.join(sorted(components[i]))}]"
        print(f"{component_str:>8}", end="")
    print()
    
    for i in range(n):
        component_str = f"[{''.join(sorted(components[i]))}]"
        print(f"{component_str:>3}", end="")
        for j in range(n):
            count = matrix[i][j]
            print(f"{count:>8}", end="")
        print()

def main():
    filename = input("Enter the input file name: ")
    
    graph = readGraph(filename)
    if not graph:
        return
    
    components = graph.getComponents()
    matrix = graph.createMatrix(components)
    
    print("\nStrongly Connected Components:")
    for i, component in enumerate(components):
        print(f"{i}: {sorted(component)}")
    
    print("\nComponent Adjacency Matrix:")
    printMatrix(components, matrix)

if __name__ == "__main__":
    main() 