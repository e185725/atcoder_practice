import math
import itertools
l = int(input())



def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(combinations_count(l-1, 11))
