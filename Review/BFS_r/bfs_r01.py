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
n, m = map(int, input().split())
array = []

for _ in range(n):
  array.append(list(map(int, input().split())))
  