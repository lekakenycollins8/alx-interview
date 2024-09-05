def isWinner(x, nums):
    """Sieve of Eratosthenes to precompute prime numbers up to the largest n"""
    def sieve_of_eratosthenes(limit):
        """Sieve of Eratosthenes to precompute prime numbers up to limit"""
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        for p in range(2, int(limit**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, limit + 1, p):
                    is_prime[multiple] = False

        # Compute the number of primes up to each index
        prime_count_up_to = [0] * (limit + 1)
        count = 0
        for i in range(2, limit + 1):
            if is_prime[i]:
                count += 1
            prime_count_up_to[i] = count
        return prime_count_up_to
    if not nums or x <= 0:
        return None
    # Get the maximum value of n in nums to limit the sieve
    max_n = max(nums)
    # Precompute the number of primes up to each number up to max_n
    prime_count_up_to = sieve_of_eratosthenes(max_n)
    # Track wins
    maria_wins = 0
    ben_wins = 0
    # Simulate each round
    for n in nums:
        # Number of primes up to n
        prime_count = prime_count_up_to[n]
        # If the number of primes is odd, Maria wins (since she plays first)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:  # If even, Ben wins
            ben_wins += 1
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
