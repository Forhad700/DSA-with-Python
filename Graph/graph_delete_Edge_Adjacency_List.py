# # undirected unweighted graph
# def insert_node(v):
#     if v in graph:
#         print(v, "is already in Graph")
#     else:
#         graph[v] = []

# def add_edge(v1, v2):
#     if v1 not in graph:
#         print(v1, "is not present in Graph")
#     elif v2 not in graph:
#         print(v2, "is not present in Graph")
#     else:
#         graph[v1].append(v2)
#         graph[v2].append(v1)

# def delete_edge(v1, v2):
#     if v1 not in graph:
#         print(v1, "is not present in Graph")
#     elif v2 not in graph:
#         print(v2, "is not present in Graph")
#     else:
#         if v2 in graph[v1]:
#             graph[v1].remove(v2)
#             graph[v2].remove(v1)


# # directed unweighted graph
# def insert_node(v):
#     if v in graph:
#         print(v, "is already in Graph")
#     else:
#         graph[v] = []

# def add_edge(v1, v2):
#     if v1 not in graph:
#         print(v1, "is not present in Graph")
#     elif v2 not in graph:
#         print(v2, "is not present in Graph")
#     else:
#         graph[v1].append(v2)

# def delete_edge(v1, v2):
#     if v1 not in graph:
#         print(v1, "is not present in Graph")
#     elif v2 not in graph:
#         print(v2, "is not present in Graph")
#     else:
#         if v2 in graph[v1]:
#             graph[v1].remove(v2)


# undirected weighted graph

def insert_node(v):
    if v in graph:
        print(v, "is already in Graph")
    else:
        graph[v] = []

def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in Graph")
    elif v2 not in graph:
        print(v2, "is not present in Graph")
    else:
        lst1 = [v2, cost]
        lst2 = [v1, cost]
        graph[v1].append(lst1)
        graph[v2].append(lst2)

def delete_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in Graph")
    elif v2 not in graph:
        print(v2, "is not present in Graph")
    else:
        lst1 = [v1, cost]
        lst2 = [v2, cost]
        if lst1 in graph[v1]:
            graph[v1].remove(lst2)
            graph[v2].remove(lst1)

graph = {}
insert_node('a')
insert_node('b')
insert_node('c')
insert_node('d')
insert_node('e')

add_edge('a', 'b', 10)
add_edge('b', 'e', 3)
add_edge('a', 'c', 5)
add_edge('a', 'd', 4)
add_edge('b', 'd', 7)
add_edge('c', 'd', 1)
add_edge('e', 'd', 2)
print(graph)
delete_edge('c', 'd', 1)
print(graph)