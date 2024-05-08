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

def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in Graph")
    elif v2 not in nodes:
        print(v2, "is not present in Graph")
    else:
        idx1 = nodes.index(v1)
        idx2 = nodes.index(v2)
        graph[idx1][idx2] = cost
        graph[idx2][idx1] = cost

def delete_node(v):
    global count_node
    if v not in nodes:
        print(v, "is not present in Graph")
    else:
        idx = nodes.index(v)
        count_node = count_node - 1
        nodes.remove(v)
        graph.pop(idx)
        for i in graph:
            i.pop(idx)

def print_matrix():
    for i in range(count_node):
        for j in range(count_node):
            print(graph[i][j], end=' ')
        print()

nodes = []
graph = []
count_node = 0
insert_node('a')
insert_node('b')
insert_node('c')
add_edge('a', 'b', 10)
delete_node('c')
print("After Deleting Graph")
print_matrix()
print("nodes: ", nodes)