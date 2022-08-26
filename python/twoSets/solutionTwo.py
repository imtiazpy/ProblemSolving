def getTotalX(a, b):

    res = 0

    for i in range(1, 101):
        flag = True

        for num_a in a:
            if i % num_a != 0:
                flag = False
                break
        if flag:
            for num_b in b:
                if num_b % i != 0:
                    flag = False
                    break
        if flag:
            res += 1

    return res        


x = getTotalX([2,4], [16,32,96])
print(x)