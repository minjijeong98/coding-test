import sys
inputs = sys.stdin.read().splitlines()

for input in inputs:
    a, b = map(int, input.split())
    print(a+b)