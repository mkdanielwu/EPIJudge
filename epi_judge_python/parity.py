from test_framework import generic_test


def parity1(x: int) -> int:
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count % 2

def parity2(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def parity3(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= (x - 1)
    return result

def parity(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
