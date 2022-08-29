# bad solution

s = input()

lowStr = ''
upperStr = ''
oddNum = ''
evenNum = ''

for i in s:
    if i.isdigit() and int(i) % 2 == 0:
        evenNum += i
    elif i.isdigit() and int(i) % 2 != 0:
        oddNum += i
    elif i.islower():
        lowStr += i
    elif i.isupper():
        upperStr += i

print(''.join(sorted(lowStr) + sorted(upperStr) + sorted(oddNum) + sorted(evenNum)))