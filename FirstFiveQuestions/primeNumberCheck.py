def isPrime(num):
    if num <= 1:
        return 'Not Prime'
    for i in range(1, num//2, 1):
        if num % (i + 1) == 0:
            return 'Not Prime'
    return 'Prime'
