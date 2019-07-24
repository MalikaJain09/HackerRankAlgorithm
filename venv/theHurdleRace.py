def hurdleRace(k, height):
    height.sort()
    for i in range(len(height) - 1, -1, -1):
        if k < height[i]:
            c =  height[i]-k
            print(c)
            break
        else:
            print("0")
            break


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    hurdleRace(k, height)
