from collections import deque

class Graph:
    def __init__(self):
        self.next = 0
        self.name = []
        self.vertice = {}
        self.edge = {}
        self.r_edge = {}
        self.vertice_used = set()
        self.c = -1

    def add(self, s, dst):
        if s not in self.vertice:
            self.name.append(s)
            self.vertice[s] = self.next
            self.edge[self.next] = set()
            self.r_edge[self.next] = set()
            self.next += 1
        i = self.vertice[s]
        for d in dst:
            if d not in self.vertice:
                self.name.append(d)
                self.vertice[d] = self.next
                self.edge[self.next] = set()
                self.r_edge[self.next] = set()
                self.next += 1
            j = self.vertice[d]
            self.edge[j].add(i)
            self.r_edge[i].add(j)

    def change(self, s):
        self.c = self.vertice[s]

    def dfs(self):
        stack = deque([self.c])
        while stack:
            cur = stack.pop()
            if cur in self.vertice_used:
                continue
            self.vertice_used.add(cur)
            for v in self.edge[cur]:
                stack.append(v)

    def dependency(self):
        stack = deque([(-1, self.c)])
        while stack:
            pt, cur = stack.pop()
            if pt != -1:
                self.r_edge[cur].remove(pt)
                if any(i in self.vertice_used for i in self.r_edge[cur]):
                    continue
            print(self.name[cur])
            for v in self.edge[cur]:
                stack.append((cur, v))
        

g = Graph()
for _ in range(int(input())):
    dst, *s = input().split()
    g.add(dst[:-1], s)
g.change(input().rstrip())
g.dfs()
g.dependency()

