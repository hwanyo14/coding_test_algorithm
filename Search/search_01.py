'''
  <부품 찾기>
    (이진 탐색)
    전자 매장에 N개의 부품이 있다. 각 부품은 정수의 고유 번호가 있다.
    어느 날 M개의 종류 부품을 대량으로 구매하려는 견적서를 받았다.
    이때 가게 안에 M갸의 종류 모두 존재하는지 확인하는 프로그램을 만들어라.
    
    [input]
      1. 첫째 줄에 정수 N
      2. 둘째 줄에 공백으로 구분하여 N개의 정수(부품)
      3. 셋째 줄에 견적서 M
      4. 넷째 줄에 공백으로 구분하여 M개의 정수(견적서 부품)
      
    [output]
      1. 각 부품이 존재하면 yes, 없으면 no 출력
      
    
    ex> 5
        8 3 7 9 2
        3 
        5 7 9
                    >> no yes yes
'''
n = int(input())
store = list(map(int, input().split()))

m = int(input())
bill = list(map(int, input().split()))

def binary_search(target, array, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return True
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return False

for i in bill:
  if binary_search(i, store, 0, len(store) - 1):
    print('yes', end=' ')
    continue
  print('no', end=' ')