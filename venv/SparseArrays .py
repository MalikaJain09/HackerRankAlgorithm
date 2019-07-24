a = int(input())
b = []
for i in range(0, a):
    b.append(input())
c = int(input())
count = []
for i in range(0, c):
    count.insert(i, 0)

d = []
for j in range(0, c):
    d.append(input())

for i in range(0, a):
    for j in range(0, c):
        if b[i] == d[j]:
            count[j] += 1
for i in range(0, c):
    print(count[i])
