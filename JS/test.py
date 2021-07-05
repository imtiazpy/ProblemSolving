# for i in range(6):
#     print(i)


# for i in range(7, 10):
#     print(i)

# Todo: we will check async in python


# name = "Jon"

# def greet():
#     print(f'hello {name}') #name can be accessed
#     name2 = Abraham

# greet()
# print(name2) #throw error

# arr =['a', 'b', 'c']

# for i in range(len(arr)):
#     print(arr[i])

# for i in range(len(arr)-1, -1, -1):
#     print(arr[i])

def func(n):
    return abs(n-50)

l = [100, 50, 65, 82, 23]

l.sort(key=func)
# l.sort()
print(l)


# Apnar array er each item jokhon myfunc() a jay tokhon oi (item-50) = ekta value ashe. oi value er upor vitti kore sorted hoy. see the explanation below:
# thelist = [100, 50, 65, 82, 23]
# thelist.sort(key=myfunc)
# so
# #for first item 100:
# myfunc returns 100-50=50 so 100 er comparison value=50
# #for second item 50:
# myfunc returns 50-50=0 so 50 er comparison value=0
# #for third item 65:
# myfunc returns 65-50=15 so 65 er comparison value=15
# #for fourth item 82:
# myfunc returns 82-50=32 so 82 er comparison value=32
# #for last item 23:
# myfunc returns 23-50= 27 so 23 er comparison value=27
# now daan pasher value egula sorted hobe and ogular respective value printed hobe.
# 0, 15, 27, 32, 50- egular main value print hobe
