def repeatedString(s, n):
    c=s
    count = 0
    for _ in range(1, n):
        for i in range(len(s)):
            if len(c) != n:
                c = c + s[i]
            else:
                break
    if 'a' in c:
        print(c.count('a'))


if __name__ == '__main__':

    s = input()

    n = int(input())

    repeatedString(s, n)

