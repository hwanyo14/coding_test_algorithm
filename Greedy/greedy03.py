'''
  <1이 될 때까지>
    어떤 수 N이 1이 될 때까지 다음 두 과정 중 하나를 반복하여 수행한다.
      1. N에서 1 빼기
      2. N을 K로 나누기

    예를 들어, N=17, K=4일 때, (17 - 1), (16 / 4), (4 / 4) = 1
    총 3 번이 최소 횟수이다.

    [input]
      1. 첫째 줄에 N, K (N >= K)
    
    [output]
      1. 최소 횟수 출력
'''
n, k = map(int, input().split())
result = 0

while True:
  target = (n // k) * k
  result += (n - target)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)