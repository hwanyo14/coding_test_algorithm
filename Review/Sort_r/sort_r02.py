'''
  <성적이 낮은 순서로 학생 출력하기>
  
    N명의 학생 정보가 있다.
    학생 정보는 이름과 성적으로 구분된다.
    이때 성적이 낮은 순서대로 학생의 이름을 출력하라.
    
    [input]
      1. 첫 번째 줄에 학생수 N
      2. 학생의 이름 A와 성적 B를 공백으로 구분하여 입력
      
    [output]
      1. 성적 순으로 이름 출력
      
    ex> 2
        홍길동 95
        이순신 77
'''
n = int(input())
array = []

for _ in range(n):
  data = input().split()
  array.append((data[0], int(data[1])))
  
array_sorted = sorted(array, key=lambda x: x[1])

print(array_sorted)