# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

# Let's try to understand this with an example.

# You are given an immutable string, and you want to make changes to it.


def mutate_string(string, position, char):
    l = list(string)
    l[position] = char
    modStr = ''.join(l)
    return modStr


# another solution using slicing
def mutate_string2(string, position, char):
    return string[:position] + char + string[position+1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string2(s, int(i), c)
    print(s_new)
