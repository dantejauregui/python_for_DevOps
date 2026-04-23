import math

def is_prime(n):
    if n <= 1:
        return False
    else:
        for a in range(2, int(math.sqrt(n)) + 1):
          if n % a == 0:
            return False
        return True


def prime_range(a, b):
    prime_list = []

    for i in range(a, b + 1):
        if is_prime(i) == True:
            prime_list.append(i)
    final_result = ", ".join(str(element) for element in prime_list)
    return final_result
print(prime_range(10000, 10050))