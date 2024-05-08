# undirected unweighted graph
def insert_node(v):
    if v in graph:
        print(v, "is already in Graph")
    else:
        graph[v] = []

def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in Graph")
    elif v2 not in graph:
        print(v2, "is not present in Graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFS_recursion(node, visited, graph):
    if node not in graph:
        print("Node is not present in Graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS_recursion(i, visited, graph)

visited =set()
graph = {}
insert_node('a')
insert_node('b')
insert_node('c')
insert_node('d')
insert_node('e')

add_edge('a', 'b')
add_edge('b', 'e')
add_edge('a', 'c')
add_edge('a', 'd')
add_edge('b', 'd')
add_edge('c', 'd')
add_edge('e', 'd')
print(graph)
DFS_recursion('a', visited, graph)