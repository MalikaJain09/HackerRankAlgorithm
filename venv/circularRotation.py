def circularArrayRotation(a, k, queries):
    # b=a.copy()
    k=k%len(a)
    # while(k!=0):
    #     print("+")
    #     for i in range(len(a)):
    #         j=(i+1)%len(a)
    #         b[j]=a[i]
    #         print(j,i)
    #     a=b.copy()
    #     k-=1
    #     print("k",k)
    #     print("b",b)
    #     print()
    # print("=")
    # print(b)
    for l in range(len(queries)):
        if queries[l]>=k:
           print("======",queries[l])
           print(a[queries[l]-k])
        else:
            print("======", queries[l])

            print(a[len(a)-k+queries[l]])

if __name__ == '__main__':


    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    circularArrayRotation(a, k, queries)


