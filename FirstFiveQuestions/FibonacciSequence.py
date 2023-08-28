def FibonacciSequence(num):
    seq = [0, 1]
    for i in range(2, num):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq
