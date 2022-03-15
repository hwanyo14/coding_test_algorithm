'''
  <시각>
    정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중
    3이 하나라도 포함되는 모든 경우의 수를 출력하라

    [input]
      1. 첫째 줄에 정수 N

    [output]
      1. 경우의 수 출력
'''
n = int(input())
cnt = 0

for i in range(n + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        cnt += 1

print(cnt)