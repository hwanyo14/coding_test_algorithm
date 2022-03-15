'''
  <숫자 카드 게임>
    1. N x M 형태의 숫자 카드가 놓여있다.(N은 행, M은 열)
    2. 먼저 뽑고자 하는 행을 선택한다.
    3. 선택된 행의 카드 중 가장 작은 숫자 카드를 뽑는다.
    4. 선택된 행의 가장 작은 숫자가 다른 행의 가장 작은 숫자들보다 커야한다.

    ex> 3 1 2
        4 1 4
        2 2 2   여기서는 각 행의 가장 작은 수가 1, 1, 2 이므로 세번째 행을 고르는 것이 답이다.

    [input]
      1. 행 N, 열 M이 주어진다.
      2. N개의 줄에 걸쳐 숫자가 주어진다.

    [output]
      1. 선택된 카드 출력
'''
n, m = map(int, input().split())
cards = []
result = 0

for _ in range(n):
  row = list(map(int, input().split()))
  min_value = min(row)
  result = max(min_value, result)

print(result)

