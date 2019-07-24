
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    countn=0
    countl=0
    countu=0
    counts=0
    count=0

    for i in password:
        if i in numbers:
            countn+=1
        elif i in lower_case:
            countl+=1
        elif i in upper_case:
            countu+=1
        elif i in special_characters:
            counts+=1
        else:
            pass
    l=[countl,countn,counts,countu]
    for i in l:
        if i ==0:
            count+=1

    if len(password)<6:
        h=6-len(password)
        if h<count:
            print(count)
        else:
            print(h)
    else:
        print(count)
        # Return the minimum number of characters to make the password strong

if __name__ == '__main__':

    n = int(input())

    password = input()

    minimumNumber(n, password)
