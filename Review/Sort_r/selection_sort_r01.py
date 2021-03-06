'''
  <선택 정렬>
  
    가장 작은 데이터를 선택하여 맨 앞의 데이터와 스왑(swap)하고,
    그 다음으로 작은 수를 선택해 앞에서 두 번째로 작은 데이터와 스왑한다.
'''
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_idx = i
  for j in range(i + 1, len(array)):
    if array[min_idx] > array[j]:
      min_idx = j
  array[i], array[min_idx] = array[min_idx], array[i]
  
print(array)