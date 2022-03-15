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
import time


n = int(input())
move = input().split()

start = time.time()

'''my solution'''
# x, y = 1, 1
# move_plan = ['L', 'R', 'U', 'D']
# move_step = [[0, -1], [0, 1], [-1, 0], [1, 0]]

# for m in move:
#   for i in range(len(move_plan)):
#     if m == move_plan[i]:
#       nx, ny = x + move_step[i][0], y + move_step[i][1]
#   if nx < 1 or ny < 1 or nx > n or ny > n:
#     continue
#   x, y = nx, ny

'''lecture solution'''
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in move:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue 
  x, y = nx, ny

end = time.time()

print(x, y)
print(f'running time: {end - start:.5f}')
