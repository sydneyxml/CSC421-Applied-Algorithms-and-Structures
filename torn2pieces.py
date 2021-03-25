graph = {}

def dfs(g, u, v, path, visit = set()):
        visit.add(u)
        path.append(u)
        if u == v:
                return True
        if u not in g:
                path.pop()
                visit.discard(u)
                return False
        for w in g[u]:
                if w not in visit:
                        if dfs(g, w, v, path, visit):
                                return True
                        path.pop()
        visit.discard(u)
        return False


m = int(input())

for _ in range(m):
        n = input().split()
        for v in n:
                if v not in graph:
                        graph[v] = set()
        v1 = n[0]
        n = n[1:]
        for v in n:
                graph[v1].add(v)
                graph[v].add(v1)


u, v = input().split()

path = []

if dfs(graph, u, v, path):
        print(' '.join(path))
else:
        print("no route found")


