import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)

def bfs(v):
    cnt=1
    visited=[0 for _ in range(n+1)]
    queue=deque([v])
    visited[v]=1

    while(queue):
        v=queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=1
                cnt+=1
    return cnt

answer=[]
max_cnt=1
for i in range(1,n+1):
    cnt=bfs(i)
    if max_cnt<cnt:
        max_cnt=cnt
        answer=[i]
    elif max_cnt==cnt:
        answer.append(i)
    
print(*answer)
