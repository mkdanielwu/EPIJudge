import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition1(pivot_index: int, A: List[int]) -> None:
    if A is not None and pivot_index >= 0 and pivot_index < len(A):
        low = 0
        p = A[pivot_index]
        for i in range(len(A)):
            if A[i] < p:
                A[i], A[low] = A[low], A[i]
                low += 1
        high = len(A) - 1
        for i in reversed(range(len(A))):
            if A[i] > p:
                A[i], A[high] = A[high], A[i]
                high -= 1
    return


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    if A is not None and pivot_index >= 0 and pivot_index < len(A):
        p = A[pivot_index]
        # devide array into 4 sections with 3 markers: smaller, equal, larger
        # smaller section: A[:smaller]
        # equal section: A[smaller:equal]
        # unclassified: A[equal:larger]
        # larger section: A[larger]
        smaller, equal, larger = 0, 0, len(A)
        while equal < larger:
            if A[equal] < p:
                A[smaller], A[equal] = A[equal], A[smaller]
                smaller += 1
                equal += 1
            elif A[equal] > p:
                larger -= 1
                A[larger], A[equal] = A[equal], A[larger]
            else:
                equal += 1

    return

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
