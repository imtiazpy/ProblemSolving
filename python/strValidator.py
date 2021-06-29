# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        if s[i].isalnum():
            print("True")
            break
        if i == len(s)-1:
            print("False")
    
    for i in range(len(s)):
        if s[i].isalpha():
            print("True")
            break
        if i == len(s)-1:
            print("False")
    
    for i in range(len(s)):
        if s[i].isdigit():
            print("True")
            break
        if i == len(s)-1:
            print("False")

    for i in range(len(s)):
        if s[i].islower():
            print("True")
            break
        if i == len(s)-1:
            print("False")
    
    for i in range(len(s)):
        if s[i].isupper():
            print("True")
            break
        if i == len(s)-1:
            print("False")

    # Another Solution
    # print(any(i.isalnum() for i in s))
    # print(any(i.isalpha() for i in s))
    # print(any(i.isdigit() for i in s))
    # print(any(i.islower() for i in s))
    # print(any(i.isupper() for i in s))


    # Another solution
    # for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    #     print(any(method(i) for i in s))


    # Another solution
    # t = type(s)
    # for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
    #     print(any(method(i) for i in s))
