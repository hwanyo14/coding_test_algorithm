'''
  <BFS 예제>

    큐 형식
    방문하지 않은 인접한 노드들을 큐에 삽입
    큐에서 단계적으로 하나씩 뽑아서 인접한 노드 탐색
'''
from collections import deque

def bfs(graph, start, visited):
  q = deque([start])
  visited[start] = True
  while q:
    n = q.popleft()
    print(n, end=' ')
    for i in graph[n]:
      if not visited[i]:
        q.append(i)
        visited[i] = True

graph = [
  [],         # 0번 노드(없음)
  [2, 3, 8],  # 1번 노드에 연결된 노드
  [1, 7],     # 2번 노드에 연결된 노드
  [1, 4, 5],  # ...
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]      # 9번 노드에 연결된 노드
]

visited = [False] * 9   # 0 ~ 9개의 노드 방문 여부

bfs(graph, 1, visited)