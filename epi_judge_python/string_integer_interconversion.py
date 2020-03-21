from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools, string

def int_to_string1(x: int) -> str:
    result = '0' if x == 0 else ''
    val = -x if x < 0 else x
    while val > 0:
        result = chr(ord('0') + val % 10) + result
        val //= 10

    return '-'+result if x < 0 else result


def int_to_string(x: int) -> str:

    is_negative = x < 0
    if is_negative:
        x = -x
    s = []
    while True:
        s.append(chr(ord('0') + (x % 10)))
        x //= 10
        if x == 0:
            break

    if is_negative:
        s.append('-')

    return ''.join(reversed(s))


def string_to_int1(s: str) -> int:
    result = 0
    if s is not None and len(s) > 0:
        s_ = s.strip()
        sign = -1 if s_[0] == '-' else 1
        if s_[0] in '-+':
            s_ = s_[1:]
        for c in s_:
            result = result * 10 + (ord(c) - ord('0'))
        result *= sign
    return result


def string_to_int(s: str) -> int:
    result = 0
    if s is not None and len(s) > 0:
        s_ = s.strip()
        sign = -1 if s_[0] == '-' else 1
        if s_[0] in '-+':
            s_ = s_[1:]
        result = sign * functools.reduce(
            lambda running_sum, c: running_sum * 10 + string.digits.index(c),
            s_, 0
        )

    return result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
