for i in range(0,7):
    l = int(7 / 2)
    # if (i == l):
    #     for j in range(0,21):
    #         if(j==7):
    #             print("WELCOME",end="")
    #         else:
    #             print("-",end="")

    # else:
    for j in range(0,21):

        m=int(21/2)
        n=m-1
        o=m+1
        if (i == l):
            if (j == 7):
                print("WELCOME", end="")

            else:
                print("-", end="")
            continue

        if j==m:
            print("|", end="")
        elif j==n or j==o:
            print(".",end="")
        else:
            print("-",end="")

    print()