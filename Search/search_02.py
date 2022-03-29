'''
  <떡볶이 떡 만들기>
    절단기 높이 H를 지정하면 줄지어진 떡을 절단한다.
    높이가 H보다 긴 떡은 윗부분이 잘리고,
    짧은 떡은 잘리지 않는다.
    이때 손님이 요청한 총 길이가 M이면, 적어도 M만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의 최댓값을 구하라
    
    [input]
      1. 첫째 줄에 떡 개수 N과 요청한 떡 길이 M
      2. 둘째 줄에 떡의 개별 높이가 주어진다.
      
    [output]
      1. 절단기 높이의 최댓값을 출력하라
      
    ex> 4 6
        19 15 10 17
                    >> 15
'''
n, m = map(int, input().split())
array = list(map(int, input().split()))

result = 0

start = 0
end = max(array)
while start <= end:
  total = 0
  mid = (start + end) // 2
  for i in array:
    if i > mid:
      total += i - mid
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
      
print(result)  
  