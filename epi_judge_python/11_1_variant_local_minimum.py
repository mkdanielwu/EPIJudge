from typing import List


def local_minimum(A: List[int]) -> int:

    def local_min_recurse(A: List[int], low: int, high: int, n: int) -> int:

        mid = low + (high - low) // 2

        if (mid == 0 or A[mid-1] >= A[mid]) and \
                (mid == n-1 or A[mid+1] >= A[mid]):
            return mid

        if A[mid-1] < A[mid]:
            return local_min_recurse(A, low, mid-1, n)

        elif A[mid+1] < A[mid]:
            return local_min_recurse(A, mid+1, high, n)

    return local_min_recurse(A, 0, len(A) - 1, len(A))


def test_local_minimum():
    A1 = [0, 0, 0, 0, 0]
    A2 = [0, 1, 2, 3, 4]
    A3 = [4, 3, 2, 1, 0]
    A4 = [2, 1, 0, 4, 3]
    A5 = [2, 1, 0, 3, 4]

    print(local_minimum(A1))
    print(local_minimum(A2))
    print(local_minimum(A3))
    print(local_minimum(A4))
    print(local_minimum(A5))

    assert local_minimum(A1) in [0, 1, 2, 3, 4, 5]
    assert local_minimum(A2) == 0
    assert local_minimum(A3) == 4
    assert local_minimum(A4) in [2, 4]
    assert local_minimum(A5) == 2


test_local_minimum()
