#1 завдання
def fibonacci_seq_generator():
    a = 1
    b = 2

    while True:
        yield a
        a, b = b, a + b

fibonacci_gen = fibonacci_seq_generator()

for numbers in range(10):
    print(next(fibonacci_gen))


#2 завдання

def prime_num_generator():
    num = 2
    while True:
        if all(num % i for i in range(2, int(num**0.5) + 1)):
            yield num
        num += 1

def prime_num_getter(n):
    primes = []
    gen = prime_num_generator()
    for _ in range(n):
        primes.append(next(gen))
    print(primes)

prime_num_getter(10)