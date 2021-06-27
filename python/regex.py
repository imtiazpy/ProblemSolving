import re


if __name__ == '__main__':
    N = int(input().strip())

    pattern = r"@gmail\.com$"
    regex = re.compile(pattern)

    firstNamesList = []

    for _ in range(N):
        # first_multiple_input = input().rstrip().split()
        # firstName = first_multiple_input[0]
        # emailID = first_multiple_input[1]

        firstName, emailID = [i for i in input().rstrip().split()]
        
        if regex.search(emailID):
            firstNamesList.append(firstName)

    firstNamesList.sort()

    for name in firstNamesList:
        print(name)

