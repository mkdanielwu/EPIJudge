from typing import List, Tuple


def search_first_key(A: List[int], k: int, low: int, high: int) -> int:
    loc = -1
    while low <= high:
        mid = low + (high - low) // 2
        if A[mid] > k:
            high = mid - 1
        elif A[mid] < k:
            low = mid + 1
        else:
            loc = mid
            high = mid - 1
    return loc


def search_last_key(A: List[int], k: int, low: int, high: int) -> int:
    loc = -1
    while low <= high:
        mid = low + (high - low) // 2
        if A[mid] > k:
            high = mid - 1
        elif A[mid] < k:
            low = mid + 1
        else:
            loc = mid
            low = mid + 1
    return loc


def search_key_return_range(A: List[int], k: int) -> Tuple[int, int]:

    if A is None:
        return -1, -1

    left, right, low, high = -1, -1, 0, len(A)-1
    while low <= high:

        mid = low + (high-low) // 2
        if A[mid] > k:
            high = mid - 1
        elif A[mid] < k:
            low = mid + 1
        else:
            left = search_first_key(A, k, low, max(mid-1, low))
            left = mid if left < 0 else left
            right = search_last_key(A, k, min(high, mid+1), high)
            right = mid if right < 0 else right
            break

    return left, right


def test_search_key_return_range():
    A1 = None
    A2 = []
    A3 = [0]
    A4 = [0, 0, 0]
    A5 = [0, 1, 2, 2]
    A6 = [0, 0, 1]
    A7 = [0, 0, 1, 1, 2, 2]
    A8 = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13]

    print(search_key_return_range(A1, 0))
    assert search_key_return_range(A1, 0) == (-1, -1)
    print(search_key_return_range(A2, 0))
    assert search_key_return_range(A2, 0) == (-1, -1)
    print(search_key_return_range(A3, 0))
    assert search_key_return_range(A3, 0) == (0, 0)
    print(search_key_return_range(A3, 1))
    assert search_key_return_range(A3, 1) == (-1, -1)
    print(search_key_return_range(A4, 1))
    assert search_key_return_range(A4, 1) == (-1, -1)
    print(search_key_return_range(A4, 0))
    assert search_key_return_range(A4, 0) == (0, 2)
    print(search_key_return_range(A5, 1))
    assert search_key_return_range(A5, 1) == (1, 1)
    print(search_key_return_range(A5, 2))
    assert search_key_return_range(A5, 2) == (2, 3)
    print(search_key_return_range(A6, 1))
    assert search_key_return_range(A6, 1) == (2, 2)
    print(search_key_return_range(A7, 2))
    assert search_key_return_range(A7, 2) == (4, 5)
    assert search_key_return_range(A8, 11) == (7, 8)


test_search_key_return_range()
