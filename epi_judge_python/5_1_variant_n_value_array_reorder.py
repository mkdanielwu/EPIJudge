from typing import List, Tuple


def dutch_flag_variant_3_value_array_reorder(A: List[int], vals: Tuple[int, int, int]) -> None:
    if A is not None:
        # divide A into 4 sections with markers: l, m, r
        # A[:l]: contains first value
        # A[l:m]: contains second value
        # A[m:r]: contains unclassified value
        # A[r:]: contains third value
        l, m, r = 0, 0, len(A)
        while m < r:
            if A[m] == vals[0]:
                A[m], A[l] = A[l], A[m]
                l += 1
                m += 1
            elif A[m] == vals[1]:
                m += 1
            elif A[m] == vals[2]:
                r -= 1
                A[m], A[r] = A[r], A[m]
    return


def test_3_value_array_reorder() -> None:
    # test cases
    A1 = [3, 2, 1, 3, 2, 1, 1, 1]
    A2 = [1, 2, 3, 1, 2, 3, 1, 3]
    A3 = [2, 2, 3, 3, 1, 3, 1, 1]
    A4 = []
    A5 = [3]
    A6 = [1, 2, 3]

    for A in [A1, A2, A3, A4, A5, A6]:
        print("before: ", A)
        dutch_flag_variant_3_value_array_reorder(A, (1, 2, 3))
        print("after: ", A)


def dutch_flag_variant_n_value_array_reorder(A: List[int], vals: List[int]) -> None:
    if A is not None:
        # Go through n passes, where n = len(vals)
        endIdx = 0
        while endIdx < len(A):
            val = A[endIdx]
            for i in range(endIdx, len(A)):
                if A[i] == val:
                    A[i], A[endIdx] = A[endIdx], A[i]
                    endIdx += 1
    return


def test_4_value_array_reorder() -> None:
    # test cases
    A1 = [4, 3, 2, 1, 4, 3, 2, 1]
    A2 = [1, 2, 3, 4, 2, 3, 4, 1]
    A3 = [2, 2, 3, 3, 1, 1, 4, 4]
    A4 = []
    A5 = [3]
    A6 = [1, 2, 3]
    A6 = [4, 1, 2, 3]

    for A in [A1, A2, A3, A4, A5, A6]:
        print("before: ", A)
        dutch_flag_variant_n_value_array_reorder(A, [1, 2, 3, 4])
        print("after: ", A)


def test_3_value_array_reorder2() -> None:
    # test cases
    A1 = [3, 2, 1, 3, 2, 1, 1, 1]
    A2 = [1, 2, 3, 1, 2, 3, 1, 3]
    A3 = [2, 2, 3, 3, 1, 3, 1, 1]
    A4 = []
    A5 = [3]
    A6 = [1, 2, 3]

    for A in [A1, A2, A3, A4, A5, A6]:
        print("before: ", A)
        dutch_flag_variant_n_value_array_reorder(A, [1, 2, 3])
        print("after: ", A)


test_3_value_array_reorder()
test_3_value_array_reor`    der2()
test_4_value_array_reorder()
