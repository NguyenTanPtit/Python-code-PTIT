# tính tổng phân thức
def sum(n):
    tong = 0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            tong += float(1 / i)
    else:
        for i in range(1, n + 1, 2):
            tong += float(1 / i)
    return tong


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    print(format(sum(n), '.6f'))
