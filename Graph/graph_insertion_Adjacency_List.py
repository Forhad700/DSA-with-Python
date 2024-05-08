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


# # undirected weighted graph

# def insert_node(v):
#     if v in graph:
#         print(v, "is already in Graph")
#     else:
#         graph[v] = []

# def add_edge(v1, v2, cost):
#     if v1 not in graph:
#         print(v1, "is not present in Graph")
#     elif v2 not in graph:
#         print(v2, "is not present in Graph")
#     else:
#         lst1 = [v2, cost]
#         lst2 = [v1, cost]
#         graph[v1].append(lst1)
#         graph[v2].append(lst2)
        

# # directed weighted graph
# def insert_node(v):
#     if v in graph:
#         print(v, "is already in Graph")
#     else:
#         graph[v] = []

# def add_edge(v1, v2, cost):
#     if v1 not in graph:
#         print(v1, "is not present in Graph")
#     elif v2 not in graph:
#         print(v2, "is not present in Graph")
#     else:
#         lst1 = [v2, cost]
#         graph[v1].append(lst1)
        
# directed unweighted graph
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

graph = {}
insert_node('a')
insert_node('b')
insert_node('c')
add_edge('a', 'b')
add_edge('a', 'c')
print(graph)