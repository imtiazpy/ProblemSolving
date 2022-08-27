"""
This solution works with the small input. with big input it will raise memory error. So we enhanced the performance of the algorithm in the SolutionTwo.py 
"""

def repeatedString(s, n):
    if len(s) == 1 and s == 'a':
        return n
    elif len(s) == 1 and s != 'a':
        return 0
    sub_str = (s * (n//len(s)+ 1))[:n]
    
    return len([i for i in sub_str if i == 'a'])


# res = repeatedString('kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm', 736778906400)
# print(res)


