def birthday(s, d, m):
    segment_count = 0

    for i in range(len(s)-1):
        if sum(s[i:m+i]) == d:
            segment_count += 1 

    return segment_count


# s = [1, 2, 1, 3, 2]
# m = 2
# d = 3
# x = birthday(s, d, m)
# print(x)