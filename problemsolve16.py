from collections import defaultdict , deque

def bulid_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        start , end = edge
        graph[start].append(end)
        graph[end].append(start)
    return graph

def shortest_path(graph , start , end):
    visited = set()
    queue = deque([(start, [])])
    
    while queue:
        node, path = queue.popleft()
        if node == end:
            return " - ".join(path + [end])
        if node not in visited:
            visited.add(node)
            queue.extend((neighbor, path + [node]) for neighbor in graph[node])
                
    return "No path found"

edges = [('H3', 'E2') , ('A4', 'B2'), ('A4' , 'C2')]
center = 'A0'

graph = bulid_graph(edges)
output = []

for start , end in edges:
    path = shortest_path(graph, start, center) + ' - ' + shortest_path(graph, center, end)
    output.append(path)
    
print("/n".join(output))