def find_parent(parent, x):
    if parent[x - 1] != x:
        parent[x - 1] = find_parent(parent, parent[x - 1])
    return parent[x - 1]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b - 1] = a 
    else:
        parent[a - 1] = b 

def solution(n, costs):
    parent = [i for i in range (1, n+1)]
    
    edges = []
    total_cost = 0
    for a,b,cost in costs:
        edges.append((cost, a,b))
    
    edges.sort()
    
    
    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b): # 사이클 x
            union_parent(parent, a, b)
            total_cost += cost


    return total_cost