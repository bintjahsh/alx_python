def fibonacci_sequence(n):
    a = 0
    b = 1
    sequence = []
    if n < 1:
        return sequence
    if n == 1:
        sequence.append(a)
        return sequence
    count = 3
    sequence.append(a)
    sequence.append(b)
    while count <= n:
        fib = a + b
        a = b
        b = fib
        count += 1
        sequence.append(fib)
    return sequence

#print(fibonacci_sequence(20))