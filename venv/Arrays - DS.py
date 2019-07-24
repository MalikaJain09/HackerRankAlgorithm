arr_count = int(input())
arr = list(map(int, input().split()))
c=[]
c=arr.copy()
for i in range (0,arr_count):
    c[arr_count-i-1]=arr[i]
for i in range(0,arr_count):
    print(c[i],end=" ")

