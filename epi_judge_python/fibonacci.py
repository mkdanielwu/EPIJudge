from test_framework import generic_test


def fibonacci(n: int) -> int:
    result = -1

    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        pre2, pre1 = 0, 1
        while n > 1:
            result = pre2 + pre1
            pre2, pre1 = pre1, result
            n -= 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
