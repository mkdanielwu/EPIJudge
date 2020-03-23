from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays1(A: List[int], B: List[int]) -> List[int]:
    return sorted(set(A) & set(B))


def intersect_two_sorted_arrays2(A: List[int], B: List[int]) -> List[int]:
    results = []
    i_a, i_b = iter(A), iter(B)
    a, b = next(i_a, None), next(i_b, None)
    while a and b:
        if a > b:
            b = next(i_b, None)
        elif a < b:
            a = next(i_a, None)
        else:
            if len(results) == 0 or results[-1] != a:
                results.append(a)
            a, b = next(i_a, None), next(i_b, None)

    it = i_a if not b else i_b

    while True:
        i = next(it, None)
        if not i:
            break
        else:
            results.append(i)

    return results


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    results = []

    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            if len(results) == 0 or results[-1] != A[i]:
                results.append(A[i])
            i += 1
            j += 1

    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
