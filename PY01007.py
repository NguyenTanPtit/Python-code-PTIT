def solution(a, b, c):
    All = a
    year = 0
    while All < c:
        All += All * b / 100
        year += 1
    return year


n = int(input())
while n > 0:
    n -= 1
    a, b, c = list(map(float, input().split()))
    print(solution(a, b, c))
