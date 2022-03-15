'''
  <왕실의 나이트>
    8 x 8 좌표 평면에서 나이트는 'L'자로만 이동할 수 있다.
    행 위치는 1 ~ 8로 표현, 열 위치는 a ~ h로 표현한다.
    이때 입력된 위치에서 나이트가 이동할 수 있는 경우의 수를 출력하라.

    [input]
      1. 첫째 줄에 알파벳(열)숫자(행)으로 위치 입력 (ex> a1)

    [output]
      1. 경우의 수 출력
'''
cord = input()
x = int(cord[1])
y = int(ord(cord[0])) - int(ord('a')) + 1

move = [(-2, 1), (-2, -1), (1, 2), (-1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
cnt = 0

for m in move:
  nx = x + m[0]
  ny = y + m[1]
  if nx < 1 or ny <1 or nx > 8 or ny > 8:
    continue
  cnt += 1

print(cnt)