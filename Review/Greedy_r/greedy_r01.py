'''
  <큰 수의 법칙>
    다양한 수로 이루어진 배열에서 주어진 수를 K번 초과하지 않게 M번 더하여 가장 큰 수를 만든다.

    예를 들어, [2, 4, 5, 4, 6]일 때, M=8이고, K=3이라면

    3 번 연속으로만 더해지지 않으면 되므로,
    6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46 이다.

      단, 다른 인덱스의 같은 수는 다른 것으로 취급한다. (ex> [3, 4, 3, 4] --> 네 숫자 모두 각각 다름)

    [input]
      1. 첫째 줄에 n, m, k 공백 구분
      2. 둘째 줄에 n개의 자연수

    [output]
      1. 답 출력
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0
cnt = int(m // (k + 1)) * k
cnt += m % (k + 1)
result += cnt * first
result += (m - cnt) * second

print(result)