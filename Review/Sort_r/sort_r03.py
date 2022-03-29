'''
  <두 배열의 원소 교체>
  
    두 개의 배열 A와 B가 있다.
    두 배열은 N개의 원소로 이루어져 있고 모두 자연수이다.
    최대 K번의 바꿔치기 연산을 할 수 있는데 A의 원소 하나와 B의 원소 하나를 골라 서로 바꾸게 된다.
    최종 목표는 A의 모든 원소의 합이 최대가 되게 하는 것이다.
    
    [input]
      1. 첫째 줄에 N, K
      2. 둘째 줄에 A의 원소
      3. 셋째 줄에 B의 원소
      
    [output]
      1. A의 모든 원소의 합
      
    ex> 5 3
        1 2 5 4 3
        5 5 6 6 5
                    >> 26
'''
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break
  
print(a)
print(sum(a))