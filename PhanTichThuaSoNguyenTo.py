# # phan tich thua so nguyen to
# import math
#
# n = int(input())
# k = n
# res = []
# for i in range(2, int(math.sqrt(n))+1):
#     while n % i == 0:
#         res.append(i)
#         n /= i
# if n > 2:
#     res.append(n)
# print(str(k)+' =', end=' ')
# for i in range(len(res)-1):
#     print(res[i], end='x')
# print(res[len(res)-1])

# # tính tổng các chữ số
# n = int(input())
# s = str(n)
# sums = 0
# for i in s:
#     sums += int(i)
# print(sums)


# # check số thuận nghịch
# def checkthuannghich(n):
#     s = str(n)
#     if s == s[::-1]:
#         return True
#     return False


# in ra số fibonaci nhỏ hơn n, là số nguyên tố
import math


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


n = int(input())
f = []
f[0] = 0
f[1] = 1
for i in range(2, n):
    f[i] = f[i-1] + f[i-2]
for i in range(n):
    if f[i] < n and prime(f[i]):
        print(f[i])
