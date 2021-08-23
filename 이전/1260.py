import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, N+1):
    graph[i].sort()

dfsvisited = [False] * (N+1)
bfsvisited = [False] * (N+1)


def dfs(graph, V, dfsvisited):
    dfsvisited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not dfsvisited[i]:
            dfs(graph, i, dfsvisited)


def bfs(graph, V, bfsvisited):
    queue = deque([V])
    bfsvisited[V] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not bfsvisited[i]:
                queue.append(i)
                bfsvisited[i] = True


dfs(graph, V, dfsvisited)
print('\b')
bfs(graph, V, bfsvisited)
print('\b')
