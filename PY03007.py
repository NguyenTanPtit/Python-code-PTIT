# xử lý văn bản
import re

res = ''
while True:
    try:
        s = input()
        res += s + " "
    except EOFError:
        break
str1 = re.split(r"[.!?]\s*", res.lower())
for i in str1:
    tmp = re.split(r"\s+", i)
    tmp[0] = tmp[0].title()
    for j in tmp:
        print(j, end=" ")
    print()
