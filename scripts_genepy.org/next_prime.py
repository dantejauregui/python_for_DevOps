import math

def is_prime(n):
    if n <= 1:
        return False
    else:
        for a in range(2, int(math.sqrt(n)) + 1):
          if n % a == 0:
            return False
        return True


def next_prime(a):
    next_prime = 0
    i = a + 1
    while i > a:
        if is_prime(i) == True:
          next_prime = i
          break
        else:
          i = i + 1
    return next_prime

print(next_prime(100000000))


# ANOTHER WAY:
# itertools.count(n) generates numbers indefinitely starting from n (n, n+1, n+2, ...)
# This FOR loop will run forever until we explicitly stop it:

# import itertools
# import sys
# start_search_from = 100000000
# for number in itertools.count(start_search_from + 1):
#     if is_prime(number):
#         # As soon as we find the first prime, print it...
#         print(number)
#         # ...and exit the script immediately.
#         sys.exit()

# "Number" is a placeholder and is assigned the first value from the Generator, so "Number" becomes 100_000_001