'''
  <위에서 아래로>
  
    하나의 수열에 다양한 수가 존재한다.
    크기에 상관 없이 나열되어 있다.
    이 수열을 내림차순으로 정렬하는 프로그램을 만들어라
    
    [input]
      1. 첫째 줄에 수의 개수 N
      2. 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다.
      
    [output]
      1. 공백으로 구분하여 결과 출력
      
    ex> 3
        15
        27
        12
              >> 27 15 12
'''
n = int(input())
array = []

for i in range(n):
  array.append(int(input()))
  
array.sort(reverse=True)

print(array)