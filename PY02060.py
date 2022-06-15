# BÀI D. BỘI SỐ CHUNG NHỎ NHẤT
def solution(N):
    res = 1
    i = 2
    while i * i <= N:
        countPower = 0
        while N % i == 0:
            countPower += 1
            N //= i
        res = res * (2 * countPower + 1)
        i += 1
    if N > 1:
        res = res * (2 * 1 + 1)
    return res


def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)


t = int(input())
while t > 0:
    t -= 1
    a, b = list(map(int, input().split()))
    if a == b:
        print(solution(a))
    else:
        n = int(giaiThua(b)/giaiThua(a-1))
        print(solution(n))
