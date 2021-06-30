# Given an integer, n, print the following values for each integer i from 1 to n:
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary


def print_formatted(num):
    w = len(str(bin(num))[2:])
    for i in range(1, n+1):
        print(str(i).rjust(w), oct(i)[2:].rjust(w), hex(i)[2:].rjust(w).upper(), bin(i)[2:].rjust(w))





if __name__ == '__main__':
    n = int(input())
    print_formatted(n)