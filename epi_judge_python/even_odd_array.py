import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd1(A: List[int]) -> None:

    if A is not None:
        even_idx, odd_idx = 0, len(A) - 1

        while even_idx < odd_idx:
            while even_idx < len(A) and A[even_idx] % 2 == 0:
                even_idx += 1

            while odd_idx >= 0 and A[odd_idx] % 2 == 1:
                odd_idx -= 1

            if even_idx < odd_idx: # swapping
                # temp = A[even_idx]
                # A[even_idx] = A[odd_idx]
                # A[odd_idx] = temp
                A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
                even_idx += 1
                odd_idx -= 1

    return


def even_odd(A: List[int]) -> None:

    if A is not None:
        even_idx, odd_idx = 0, len(A) - 1

        while even_idx < odd_idx:
            if A[even_idx] % 2 == 0:
                even_idx += 1
            else:
                A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
                odd_idx -= 1
    return

@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
