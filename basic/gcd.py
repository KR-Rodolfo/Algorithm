# 최대공약수를 구하는 간단한 알고리즘
def gcd(a, b):
    while a * b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

result = gcd(16 , 8)
print(result)