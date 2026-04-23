import math

def is_prime(n):
    if n <= 1:
        return False
    else:
        for a in range(2, int(math.sqrt(n)) + 1):
          if n % a == 0:
            return False
        return True

print(is_prime(5))