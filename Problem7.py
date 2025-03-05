#Problem7.py
#Project Euler problem 7

from NumberTests import sieve_of_eratosthenes

limit = 2000000
prime_numbers = sieve_of_eratosthenes(limit)
Total = sum(prime_numbers)
print(Total)

