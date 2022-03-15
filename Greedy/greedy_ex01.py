'''
  <거스름돈 문제>
    동전 500, 100, 50, 10원이 무한하게 존재하고
    손님에게 거슬러줘야 할 돈이 N원일 때, 최소 동전 개수를 구하여라 (단, N은 10의 배수)
'''

n = int(input())
cnt = 0

coins = [500, 100, 50, 10]

for coin in coins:
  cnt += n // coin
  n %= coin

print(cnt)