def sieve_naive(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for num, prime in enumerate(primes):
        if prime:
            multiple = 2 * num
            while multiple < len(primes):
                primes[multiple] = False
                multiple += num
    for num, prime in enumerate(primes):
        if prime:
            print(num, end=' ')
    print()
            
def sieve_naive_pythonic(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for num, prime in enumerate(primes):
        if prime:
            for multiple in range(2 * num, len(primes), num):
                primes[multiple] = False
    for num, prime in enumerate(primes):
        if prime:
            print(num, end=' ')
    print()
     
def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    num = 2
    while num * num <= n:
        if primes[num]:
            for multiple in range(num * num, len(primes), num):
                primes[multiple] = False
        num += 1
    for num, prime in enumerate(primes):
        if prime:
            print(num, end=' ')
    print()
            
if __name__ == '__main__':
    
    sieve_naive(156)
    sieve_naive_pythonic(156)
    sieve(156)
        
