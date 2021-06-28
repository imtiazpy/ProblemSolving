# Solution #1
def swap_case(s):
    swappedS = ''
    for i in s:
        if i.isupper():
            # i.lower()
            swappedS += i.lower()
        else:
            # i.upper()
            swappedS += i.upper()
    return swappedS

# Solution #2
def swap_case2(s):
    swappedS = ''
    for i in s:
        if i == i.upper():
            swappedS += i.lower()
        else:
            swappedS += i.upper()
    return swappedS


# Solution #3
def swap_case3(s):
    return s.swapcase()


# Solution #4
def swap_case4(s):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in s])


if __name__ == '__main__':
    s = input()
    result = swap_case4(s)
    print(result)