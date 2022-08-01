isprime(n)              # Test if n is a prime number (True) or not (False).

primerange(a, b)        # Generate a list of all prime numbers in the range [a, b).
randprime(a, b)         # Return a random prime number in the range [a, b).
primepi(n)              # Return the number of prime numbers less than or equal to n.

prime(nth)              # Return the nth prime, with the primes indexed as prime(1) = 2. The nth prime is approximately n*log(n) and can never be larger than 2**n.
prevprime(n, ith=1)     # Return the largest prime smaller than n
nextprime(n)            # Return the ith prime greater than n

sieve.primerange(a, b)  # Generate all prime numbers in the range [a, b), implemented as a dynamically growing sieve of Eratosthenes. 
