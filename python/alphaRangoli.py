# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# N = 5
"""
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

# Solution:


def print_rangoli(size):
    n = size
    charList = list(map(chr, range(97, 123)))

    charSize = charList[n-1::-1] + charList[1:n]
    rangoli_width = len('-'.join(charSize))
    
    print(charSize)
    for i in range(1, n):
        print('-'.join(charList[n-1:n-i:-1]+charList[n-i:n]).center(rangoli_width, '-'))
    # print('-'.join(charList[n-1::-1]+charList[1:n]))
    for i in range(n, 0, -1):
        print('-'.join(charList[n-1:n-i:-1]+charList[n-i:n]).center(rangoli_width, '-'))

  
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



# another solution:

# import string
# alpha = string.ascii_lowercase

# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))