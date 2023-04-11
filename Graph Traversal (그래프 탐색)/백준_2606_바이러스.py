from collections import deque

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue=deque([v])
    visited[v]=1

    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=1

bfs(1)
print(sum(visited)-1)