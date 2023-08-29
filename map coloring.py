class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.coloring = {}
    
    def is_safe(self, node, color):
        for neighbor in self.graph[node]:
            if neighbor in self.coloring and self.coloring[neighbor] == color:
                return False
        return True
    
    def backtrack(self, node):
        if node is None:
            return True
        
        for color in self.colors:
            if self.is_safe(node, color):
                self.coloring[node] = color
                next_node = None
                for neighbor in self.graph[node]:
                    if neighbor not in self.coloring:
                        next_node = neighbor
                        break
                if next_node is None or self.backtrack(next_node):
                    return True
                self.coloring.pop(node, None)
        
        return False
    
    def color_map(self):
        start_node = list(self.graph.keys())[0]
        self.backtrack(start_node)
    
    def get_coloring(self):
        return self.coloring

def main():
    graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW']
    }
    
    colors = ['Red', 'Green', 'Blue']
    
    map_coloring = MapColoring(graph, colors)
    map_coloring.color_map()
    
    coloring_result = map_coloring.get_coloring()
    print("Map Coloring Result:")
    for node, color in coloring_result.items():
        print(f"{node}: {color}")

if __name__ == "__main__":
    main()
