from typing import List


def search_first_greater_than(A: List[int], t: int) -> int:

    low, high, result = 0, len(A)-1, -1

    while low <= high:
        mid = low + (high - low) // 2

        if t >= A[mid]:
            low = mid + 1

        else:
            result = mid
            high = mid -1

    return result


def test_search_first_greater_than():
    A1 = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    assert search_first_greater_than(A1, 285) == 9
    assert search_first_greater_than(A1, -13) == 1


test_search_first_greater_than()