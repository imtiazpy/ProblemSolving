# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

def minion_game(string):
    string = string.upper()
    kevin = 0
    stuart = 0
    vowels = 'AEIOU'

    # First attempt:
    # for i in range(len(string)):
    #     for j in range(i, len(string)):
    #         if string[i:j+1][0] in vowels:
    #             kevin += 1
    #         else:
    #             stuart += 1

    # Second solution logic:
    for i in range(len(string)):  # BANANA
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Draw')


minion_game("banana")
