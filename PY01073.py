# hoán vị kí tự
from itertools import permutations

res = []
s = input()
for i in s:
    res.append(i)
k = list(permutations(res))
for i in k:
    for j in i:
        print(j, end="")
    print()
