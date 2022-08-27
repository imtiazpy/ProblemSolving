# Enhanced solution

def getOccurrence(s):
    return len([a for a in s if a == 'a'])

def repeatedString(s, n):
    initial_occurrence_of_a = getOccurrence(s)
    
    # how many times we have to repeat s roughly
    repeat_s = n // len(s)

    if n % len(s) == 0:
        return repeat_s * initial_occurrence_of_a
    else:
        more_occurrence = getOccurrence(s[:n%len(s)])
        return (repeat_s * initial_occurrence_of_a) + more_occurrence

# s = repeatedStringTwo('kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm', 736778906400)
# print(s)