'''
  <게임 개발>
    N x M 크기의 맵은 육지와 바다로 이루어져 있다.
    캐릭터는 동서남북 중 한 곳을 바라본다.
    캐릭터는 상하좌우 움직일 수 있고, 바다로는 갈 수 없다.
    캐릭터 움직임의 메뉴얼은 다음과 같다.
      
      1. 현재 위치에서 현재 방향을 기준으로 반시계 방향으로 90도씩 돌면서 갈 곳을 정한다.
      2. 왼쪽에 아직 가보지 못한 칸이 있다면 왼쪽으로 회전 후 전진한다.
      3. 네 방향 모두 이미 가본 칸이거나 바다로 된 경우라면,
          바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
          이때, 뒤쪽 방향이 바다라면 움직임을 멈춘다.

    [input]
      1. 첫째 줄에 맵 세로 N, 가로 M
      2. 둘째 줄에 캐릭터가 있는 좌표 (a, b)와
          바라보는 방향(북:0, 동:1, 남:2, 서:3) d를 입력한다.
      3. 셋째 줄에 맵의 정보를 입력한다. (0:육지, 1:바다)
      4. 처음 캐릭터 시작 위치는 육지이다.

    [output]
      1. 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
'''
n, m = map(int, input().split())
x, y, d = map(int, input().split())

array = []
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(n):
  array.append(list(map(int, input().split())))

def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

array[x][y] = 2
cnt = 1
turn_time = 0

while True:
  turn_left()
  nx = x + dir[d][0]
  ny = y + dir[d][1]
  if array[nx][ny] == 0:
    array[nx][ny] = 2
    turn_time = 0
    cnt += 1
    x, y = nx, ny
    continue
  else:
    turn_time += 1
  if turn_time == 4:
    nx = x - dir[d][0]
    ny = y - dir[d][1]
    if array[nx][ny] == 1:
      break
    else:
      x, y = nx, ny
    turn_time = 0

print(cnt)