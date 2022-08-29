# arr = sorted(input().split())

# first_condition = [True if int(arr[0]) >= 0 else False]

# second_condition = any([i == i[::-1] for i in arr])

# """
# We need to improve second condition as it is going all the way to the end of the arr even if it finds a palindrome in the beginning. 
# we have to stop the loop if it finds a palindrome
# """

'''
Title     : Any or All
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
'''

ar = sorted(input().split())

if ar[0] < 0:
    print(False)
else:
    chk = False
    for i in ar:
        if i == i[::-1]:
            chk = True
            break
    print(chk)
    

