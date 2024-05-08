def insert_node(v):
    global count_node
    if v in nodes:
        print(v, "is already in Graph")
    else:
        count_node = count_node + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        tmp = []
        for i in range(count_node):
            tmp.append(0)
        graph.append(tmp)

def add_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "Vertex is not present")
    elif v2 not in nodes:
        print(v2, "Vertex is not present")
    else:
        idx1 = nodes.index(v1)
        idx2 = nodes.index(v2)
        graph[idx1][idx2] = 1
        graph[idx2][idx1] = 1

def print_matrix():
    for i in range(count_node):
        for j in range(count_node):
            print(graph[i][j], end=' ')
        print()

nodes = []
graph = []
count_node = 0
print("Before insert nodes")
print(nodes)
print(graph)

insert_node('a')
insert_node('b')
insert_node('d')
add_edge('a', 'b')
add_edge('a', 'd')
print("After insert nodes")
print(nodes)
print(graph)
print_matrix()