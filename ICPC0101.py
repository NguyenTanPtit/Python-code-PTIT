# thu gọn dãy số
# def check(a):
#     for i in range(0, len(a) - 1):
#         if (a[i] + a[i+1]) % 2 == 0:
#             return False
#     return True
#
#
# n = int(input())
# s = list(map(int, input().split()))
# while not check(s):
#     i = 0
#     while i < len(s) - 1:
#         if (s[i] + s[i+1]) % 2 == 0:
#             s.pop(i)
#             s.pop(i)
#         else:
#             i += 1
# print(len(s))

n = int(input())
s = list(map(int, input().split()))
i = 0
while i < len(s) - 1:
    if (s[i] + s[i+1]) % 2 == 0:
        s.pop(i)
        s.pop(i)
        if i > 0:
            i -= 1
    else:
        i += 1
print(len(s))
