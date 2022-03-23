'''
  <이진 탐색>
  
    찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하는 방법
'''
def binary_search(target, array, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
  