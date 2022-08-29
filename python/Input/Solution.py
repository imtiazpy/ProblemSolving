# Problem   : https://www.hackerrank.com/challenges/input/problem

x, k = map(int, input().split())

equation = input().strip()

print(eval(equation) == k)
