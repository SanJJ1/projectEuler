
def isprime(n):
    if n == 2:
        return True
    if not n % 2:
        return False
    i = 3
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True

n = 2
np = 1
while np < 10002:
    if isprime(n):
        print(f"prime #{np}: {n}")
        np += 1
    n += 1