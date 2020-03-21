from typing import List

from test_framework import generic_test
import heapq
import collections
from typing import Tuple


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:

    results = []
    min_heap: List[Tuple[int, int]] = []
    iters = [iter(a) for a in sorted_arrays]

    for i, it in enumerate(iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    while min_heap:
        min_element, next_list = heapq.heappop(min_heap)
        results.append(min_element)
        next_element = next(iters[next_list], None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, next_list))

    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
