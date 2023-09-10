# n의 약수의 개수를 구하는 알고리즘
# O(sqrt(n)) k가 루트 n 만큼 반큼 반복한다.
def number_of_factors(n):
    k = 1
    count = 0
    while k*k <= n:
        if n % k == 0:
            count += 2
        k += 1
    if k*k == n:
        count -= 1
    return count

print(number_of_factors(81))