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
# abcde
# def print_rangoli(n):
#     charList = list(map(chr, range(97, 97+n)))

#     charSize = charList[n-1::-1]+charList[1:n]
#     rangoli_width = len('-'.join(charSize))

#     for i in range(1, n):
#         print('-'.join(charList[n-1:n-i:-1]+charList[n-i:n]).center(rangoli_width, '-'))
#     for i in range(n, 0, -1):
#         print('-'.join(charList[n-1:n-i:-1]+charList[n-i:n]).center(rangoli_width, '-'))

# print_rangoli(5)


import string
alpha = string.ascii_lowercase

n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))


L = []
for i in range(n):
    s = '-'.join(alpha[i:n])
    
    L.append((s[::-1]+s[1:]).center(4*n-3, '-'))

print(L)
print('\n'.join(L[::-1]+L[1:]))