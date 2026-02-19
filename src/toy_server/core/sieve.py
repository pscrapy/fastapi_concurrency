def prime_sieve(n: int) -> int:
    """
    Long-running, useless operation to compute the N-th prime
    
    AI DISCLAIMER: code generated using Gemini3 model in "fast" mode,
    accessed via web interface at gemini.google.com
    """
    if n < 1:
        return None
    if n == 1:
        return 2
    
    count = 1  # We already accounted for 2
    candidate = 3
    
    while count < n:
        # Check if candidate is prime
        is_prime = True
        # We only need to check up to the square root of the candidate
        for i in range(3, int(candidate**0.5) + 1, 2):
            if candidate % i == 0:
                is_prime = False
                break
        
        if is_prime:
            count += 1
            if count == n:
                return candidate
        
        # Skip even numbers
        candidate += 2