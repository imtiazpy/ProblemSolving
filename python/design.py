# create a Pattern like below
# n is an odd number input
# m is 3xn and is the width of the pattern

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

n, m = map(int, input().split())

for i in range(1, n, 2):
    print((i * '.|.').center(m, '-'))

print("WELCOME".center(m, '-'))

for i in range(n-2, -1, -2):
    print((i * '.|.').center(m, '-'))