def kangaroo(x1, v1, x2, v2):
    c = 0
    while (c == 0):
        if x1 >= x2:
            x1 = x1 + v1
            x2 = x2 + v2
            print(x1,x2)
            if x1>=100000000:
                print("NO")
                break
            if (x1 == x2):
                print("Yes")
                break
        else:
            if v2 < v1:
                x1 = x1 + v1
                x2 = x2 + v2
                print(x1,x2)
                if (x2>=100000000):
                    print("NO")
                    break
                if (x1 == x2):
                    print("Yes")
                    break
            else:
                print("No")
                c=1
                break
        c = 0


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    kangaroo(x1, v1, x2, v2)