from collections import deque

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def dfs(v):
    print(v,end=" ")
    visited[v]=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue=deque([v])
    visited[v]=1
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=1

dfs(v)

visited=[0 for _ in range(n+1)]
print()

bfs(v)