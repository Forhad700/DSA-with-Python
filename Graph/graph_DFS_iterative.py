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

def DFS_iterative(node, graph):
    visited = set()
    if node not in graph:
        print("Node is not present in Graph")
        return
    stack = []
    stack.append(node)
    while stack:
        curr = stack.pop()
        if curr not in visited:
            print(curr)
            visited.add(curr)
            for i in graph[curr]:
                stack.append(i)
    

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
DFS_iterative('a', graph)