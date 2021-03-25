import collections

def dfs(visit, u, path, note = {}):
    if u in note:
        return note[u]
    for v in path[u]:
        if v in visit or dfs(visit | {v}, v, path):
            note[v] = True
            return True
    note[u] = False
    return False

def safecycle(begin, path):
    return dfs({begin}, begin, path)


m = int(input())
path = collections.defaultdict(list)
for i in range(m):
    p, q = input().split()
    path[p].append(q)

while True:
    try:
        city = input()
        while city:
            print(city, "safe" if safecycle(city, path) else "trapped")
            city = input()
    except:
        break

