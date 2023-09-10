# 비트수를 계산 알고리즘
# O(log n) -> n = n // 2 가 반복 
def count_bit(n):
    bits = 0
    while n > 0:
        n = n // 2
        bits += 1
    return bits

print(count_bit(21))