import re
def swap_case(s):
    m=""
    for i in range(len(s)):
        if s[i].isupper() is   True:
            k=s[i].lower()
            m+=k

        elif s[i].islower() is True:
            k = s[i].upper()
            m += k
        elif s[i].isspace() is True:
            m+=s[i]
        elif s[i].isdigit() is True:
            m+=s[i]

        else:
            m+=s[i]


    return m

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)