'''
  <미로 탈출>
    N x M 크기의 미로를 탈출해야 한다.
    시작 위치는 (1, 1)이고, 출구는 (N, M)이다.
    괴물이 있는 부분은 0, 없는 부분은 1로 표시된다.
    이 미로를 탈출하기 위해 움직이는 최소 칸의 수를 구하시오.

    [input]
      1. 첫째 줄에 세로 N, 가로 M이 주어진다.
      2. 둘째 줄에 미로의 형태가 주어진다.

    [output]
      1. 최소 칸의 수 출력
'''
from collections import deque

n, m = map(int, input().split())
array = []

for i in range(n):
  array.append(list(map(int, input())))

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + move[i][0]
      ny = y + move[i][1]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if array[nx][ny] == 0:
        continue
      if array[nx][ny] == 1:
        array[nx][ny] = array[x][y] + 1
        q.append((nx, ny))
  return array[n - 1][m - 1]

print(bfs(0, 0))
