import math

def is_prime(n):
    if n <= 1:
        return False
    else:
        for a in range(2, int(math.sqrt(n)) + 1):
          if n % a == 0:
            return False
        return True

def sum_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i) == True:
            primes.append(i)
    #print(primes)
    result = sum(primes)
    return result

sum_primes(2)