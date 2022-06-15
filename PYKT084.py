# câu hỏi theo chủ đề
t = int(input())
res = []
dtc = {}
while t > 0:
    t -= 1
    s = input()
    res.append(s)
k = 0
dtc[res[k]] = 0
for i in range(1, len(res)):
    if i == k:
        continue
    if res[i] == "":
        k = i + 1
        dtc[res[k]] = 0
    else:
        dtc[res[k]] += 1
for i in dtc:
    print(i + ": " + str(dtc[i]))
