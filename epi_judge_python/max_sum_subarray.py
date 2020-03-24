from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    max_seen, current_max = A[0], A[0]
    max_seen_left, max_seen_right = 0, 0
    max_current_left, max_current_right = 0, 0
    for i in range(1, len(A)):
        if current_max + A[i] >= A[i]:
            current_max = current_max + A[i]
            max_current_right = i
        else:
            current_max = A[i]
            max_current_left = max_current_right = i
        if max_seen < current_max:
            max_seen = current_max
            max_seen_left, max_seen_right = max_current_left, max_current_right
    print("max={}, range=[{},{}]".format(max_seen, max_seen_left, max_seen_right))
    return max_seen


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
