n=int(input())
l=[]
for i in range(0,n):
    c=int(input())
    l.append(c)
for i in range(len(l)):
    j=int(l[i]/5)
    k=j+1
    b=k*5
    if l[i]<38:
        print(l[i])
    elif(b-l[i])<3:
        print(b)
    else:
        print(l[i])
