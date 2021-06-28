def count_substring(string, sub_string):
    countStr = 0
    len_subStr = len(sub_string)
    for i in range(len(string)):
        temp = string[i:i+len_subStr]
        if temp == sub_string:
            countStr += 1
    return countStr


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

    