'''
  <음료수 얼려먹기>
    N x M 크기의 얼음 틀이 있다.
    구멍이 뚫린 칸은 0, 칸막이가 존재하는 곳은 1이다.
    얼음 틀 모양이 주어졌을 때 생성되는 아이스크림의 개수를 구하라

    [input]
      1. 첫번 째 줄에 세로 N, 가로 M
      2. 두번 째 줄부터 N + 1번째 줄까지 얼음 틀 형태
    
    [output]  
      1. 아이스크림의 개수 출력
'''
n, m = map(int, input().split())
array = []

for i in range(n):
  array.append(list(map(int, input())))

cnt = 0

def dfs(x, y):
  if x < 0 or x > n - 1 or y < 0 or y > m - 1:
    return False
  if array[x][y] == 0:
    array[x][y] = 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
    return True
  return False

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      cnt += 1

print(cnt)