'''
  <상하좌우>
    N x N 크기의 공간이 주어지고, 가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (N, N)이다.
    시작점은 (1, 1)이며 [L, R, U, D]로 칸을 이동한다.
    여기서 여행 계획이 주어졌을 때, 최종 도착 좌표를 출력하시오.

    [input]
      1. 첫째 줄에 N
      2. 둘째 줄에 여행계획 (L, R, U, D)

    [output]
      1. 최종 좌표 출력
'''
n = int(input())
moves = input().split()

plan = ['L','R','U','D']
steps = [(0, -1), (0, 1), (-1, 0), (1, 0)]

x, y = 1, 1

for m in moves:
  for i in range(len(plan)):
    if m == plan[i]:
      nx = x + steps[i][0]
      ny = y + steps[i][1]
  if nx < 0 or ny < 0 or nx > n or ny > n:
    continue
  x, y = nx, ny
  
print(x, y)

