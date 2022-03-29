'''
  <삽입 정렬>

    데이터를 적절한 위치에 삽입하여 정렬
    특정 데이터의 앞 데이터들은 정렬이 되어있는 것으로 가정한다.
    따라서 두 번째 데이터부터 정렬을 시작한다.
'''
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    else:
      break
    
print(array)