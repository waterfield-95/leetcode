cnt = 0

def dfs(g, u, parent, discover, finish):
    global cnt
    discover[u] = cnt
    cnt += 1

    for i in range(len(g(u))):
        v = g[u][i]
        if v != parent:
            dfs(g, v, u, discover, finish)
    
    finish[u] = cnt
    cnt += 1

def process(edges, V, discover, finish):
    global cnt
    g = [[] for i in range(V)]

    for i in range(V - 1):
        u = edges[i][0]
        v = edges[i][1]
        g[u].append(v)
        g[v].append(u)

    cnt = 0
    dfs(g, 0, -1, discover, finish)