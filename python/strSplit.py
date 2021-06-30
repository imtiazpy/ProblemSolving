# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    res = '-'.join(line.split(' '))
    return res

def anotherSolution(line):
    res = line.replace(' ', '-')
    return res

if __name__ == '__main__':
    line = input()
    result = anotherSolution(line)
    print(result)