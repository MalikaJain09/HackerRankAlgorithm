n = int(input())

p = int(input())
if n%2==0:
    if (n/2)>=p:
        if p%2==0:
            print(int(p/2))
        if p%2!=0:
            print(int((p-1)/2))

    else:

        if p % 2 == 0:
            print(int((n-p)/2))
        if p % 2 != 0:
            print(int((n-p+1)/2))
else:
    if (n / 2) > p:
        if p % 2 == 0:
            print(int(p / 2))
        if p % 2 != 0:
            print(int((p - 1) / 2))

    else:

        if p % 2 == 0:
            print(int((n - p)/2))
        if p % 2 != 0:
            print(int((n - p )/2))
