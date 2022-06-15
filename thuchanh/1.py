n = int(input())
while n > 0:
    n -= 1
    s = input()
    s1 = input()
    print(s.count(s1, 0, len(s)))
