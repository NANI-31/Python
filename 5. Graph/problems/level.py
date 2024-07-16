def matrix(edges, n):
    adj_matrix = [[] for i in range(n)]
    for u,v in edges:
        adj_matrix[u].append(v)
        adj_matrix[v].append(u)
    return adj_matrix

def levels(edges, root=0):
    max_vertex = max(max(u,v) for u,v in edges) + 1
    print(max_vertex)
    adj_matrix = matrix(edges, max_vertex)
    
    e_Level  = [-1] * max_vertex
    e_Level[root] = 0
    queue = [root]
    
    while queue:
        v = queue.pop(0)
        for u in adj_matrix[v]:
            if e_Level[u] == -1:
                e_Level[u] = e_Level[v] + 1
                queue.append(u)
    return e_Level
    

edges = [[0, 1], [0, 2], [1, 3], [2, 4]]
x = 3
level = levels(edges)
print(level)
print(level[x-1])