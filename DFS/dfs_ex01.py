'''
  <DFS 예제>

    (스택 형식)
    재귀함수를 통해 인접한 노드가 스택에 들어가자마자 또다른 인접한 노드에 대해 탐색
'''
def dfs(graph, start, visited):
  visited[start] = True
  print(start, end=' ')
  for i in graph[start]:
    if not visited[i]:
      dfs(graph, i, visited)

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

dfs(graph, 1, visited)