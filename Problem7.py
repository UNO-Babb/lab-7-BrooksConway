from NumberTests import sieve_of_eratosthenes

limit = 2000000
prime_numbers = sieve_of_eratosthenes(limit)

if len(prime_numbers) >= 10001:
    PrimeGoal = prime_numbers[10000]
else:
    pass

if (PrimeGoal) is not None:
    print(f"The 10001st prime number is: ", PrimeGoal)
else:
    pass
