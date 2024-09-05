#!/usr/bin/python3

def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    def sieve_of_eratosthenes(n):
        """Generate a list of prime numbers up to n
        using the Sieve of Eratosthenes."""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, n + 1, i):
                    sieve[multiple] = False
        return sieve

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Cache the number of moves for each possible n
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
