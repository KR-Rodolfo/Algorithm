# O(n)
def sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

# O(n)
def recursive_sum_1(n):
    if n == 1:
        return 1
    return recursive_sum_1(n - 1) + n

# O(n)
def recursive_sum_2(a, b):
    if a == b:
        return a
    m = (a + b) // 2
    return recursive_sum_2(a, m) + recursive_sum_2(m + 1, b)

n = 5
print(sum(n))
print(recursive_sum_1(n))
print(recursive_sum_2(1, n))
