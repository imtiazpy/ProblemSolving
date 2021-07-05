import os

# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalized correctly as Alison Heck.


def solve(s):
    # name = s.split()
    # capitalized = []
    # for i in name:
    #     capitalized.append(i.capitalize())
    # return ' '.join(capitalized)

    return ' '.join((word.capitalize() for word in s.split()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
