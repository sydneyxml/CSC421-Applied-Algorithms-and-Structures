from sys import stdin
from collections import deque


def dfs(u, adj, visit, s):
    visit.add(u)
    for v in adj[u]:
        if v not in visit:
            dfs(v, adj, visit, s)
    s.append(u)


def kosaraju(n, adj, r_adj):
    stack = deque()
    visit = set()
    for u in range(n):
        if u not in visit:
            dfs(u, adj, visit, stack)
    visit.clear()
    scc = []
    while stack:
        u = stack.pop()
        if u not in visit:
            scc.append([])
            dfs(u, r_adj, visit, scc[-1])
    return scc


def build_graph(adj, scc):
    id = [None] * len(adj)
    for i in range(len(scc)):
        for u in scc[i]:
            id[u] = i
    scc_adj = [[] for _ in range(len(scc))]
    r_scc_adj = [[] for _ in range(len(scc))]
    for i in range(len(scc)):
        for u in scc[i]:
            for v in adj[u]:
                if i == id[v]:
                    continue
                scc_adj[i].append((id[v], (u, v)))
                r_scc_adj[id[v]].append((i, (u, v)))
    return scc_adj, r_scc_adj


def check(scc_adj, r_scc_adj, read):
    if len(scc_adj) == 1:
        return "valid"
    
    outs = {i for i in range(len(scc_adj)) if not scc_adj[i]}
    ins = {i for i in range(len(r_scc_adj)) if not r_scc_adj[i]}
    
    if len(ins) != 1 or len(outs) != 1:
        return "invalid"
    
    noin = ins.pop()
    out = outs.pop()
    
    if (sum(v == out for v, _ in scc_adj[noin]) < 2 and (len(set(v for v, _ in scc_adj[noin])) < 2 or len(set(v for v, _ in r_scc_adj[out])) < 2)):
        return "invalid"
    
    r_edges = []
    for v, e in scc_adj[noin]:
        if v == out:
            r_edges.append(e)
    
    if not r_edges:
        return "invalid"
    return "{} {}".format(*min(r_edges, key=lambda e: read[e]))


mn = stdin.readline().strip()
case = 1
while mn:
    n, m = map(int, mn.split())
    adj = [[] for _ in range(n)]
    r_adj = [[] for _ in range(n)]
    read = {}
    for i in range(m):
        a, b = (int(x) for x in stdin.readline().split())
        read[(a, b)] = i
        adj[a].append(b)
        r_adj[b].append(a)   
    sccs = kosaraju(n, adj, r_adj)
    scc_adj, r_scc_adj = build_graph(adj, sccs)
    print("Case {}:".format(case), check(scc_adj, r_scc_adj, read))
    case += 1
    mn = stdin.readline().strip()

