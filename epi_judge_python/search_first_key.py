from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:

    low, high = 0, len(A)-1
    found_idx = -1
    while low <= high:
        m = low + (high - low) // 2     # avoid overflow
        if k > A[m]:
            low = m + 1
        elif k < A[m]:
            high = m - 1
        else:
            found_idx = m
            high = m - 1

    return found_idx


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
