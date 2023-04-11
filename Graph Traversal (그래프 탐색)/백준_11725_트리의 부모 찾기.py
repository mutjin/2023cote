from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
parents=[0 for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    queue=deque([v])
    visited[v]=1

    while(queue):
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                parents[i]=v
                visited[i]=1

bfs(1)
for i in parents[2:]:
    print(i)