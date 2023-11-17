# 동전 교환 문제
'''
    - 1원, 10원, 50원, 100원 동전이 있을 때, 373원을 거슬러 주기 위해서는 동전을 최소 몇개 사용해야 하는가?
'''

coins = [100, 50, 10, 1]
money = 373
cnt = 0

for coin in coins:
    cnt += money // coin
    money = money % coin

print(cnt)