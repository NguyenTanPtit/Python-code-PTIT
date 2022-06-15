# tìm số nhỏ nhất/ lớn nhất
import re

t = int(input())
while t > 0:
    t -= 1
    s = input()
    a = re.findall(r"\d+", s)
    a = [int(i) for i in a]
    a.sort()
    print(a[-1])
