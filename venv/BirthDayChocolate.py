n = int(input().strip())

s = list(map(int, input().rstrip().split()))
sum=0
count = 0
dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])
for i in range(len(s)):
    y = []
    for l in range(0,m):
        if i+l<len(s):
          y.append(s[i+l])

    print(y)
    for t in range(len(y)):
        sum+=y[t]
    print(sum)
    if sum==d:
        count+=1
    y.clear()
    sum=0
print(count)