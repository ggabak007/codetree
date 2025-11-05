n, m = map(int, input().split())
from collections import deque
# Please write your code here.
visited = [False] * (n+1)
graph = [[]for i in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(v):
    queue = deque([1])
    count = 0
    visited[1] = True

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count+=1
    return count


print(BFS(1))
