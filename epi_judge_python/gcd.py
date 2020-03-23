from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    # Euclidean algorithm
    return x if y == 0 else gcd(y, x % y)

print(gcd(36,156))
print(gcd(156,36))

if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.py', 'gcd.tsv', gcd))

