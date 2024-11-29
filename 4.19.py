print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    prime_numbers = tuple(i for i in range(limit + 1) if primes[i])
    return prime_numbers
P = sieve_of_eratosthenes(10**6)
print(P[:20]) 
print(f"Tổng số số nguyên tố nhỏ hơn 1 triệu: {len(P)}")
