def bitwiseAnd(N, K):

    max = 0

    for i in range(1, N+1):
        for j in range(1, i):
            bitwise = i & j
            if max < bitwise < K:
                max = bitwise
                if max == K - 1:
                    return max
    return max

print(bitwiseAnd(5, 4))