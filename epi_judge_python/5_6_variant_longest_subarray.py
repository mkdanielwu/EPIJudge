from typing import List


def find_len_longest_subarray(A: List[int]) -> int:
    max_len = 0

    if A is not None and len(A) > 0:
        current_len, current_val = 0, A[0]

        for val in A:
            if val == current_val:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
                current_val = val

    return max_len


def test_find_len_longest_subarray():
    # test cases
    A1 = []
    A2 = None
    A3 = [3]
    A4 = [1, 2, 3]
    A5 = [3, 2, 1, 3, 2, 1, 1, 1]
    A6 = [1, 2, 3, 3, 2, 1]
    A7 = [2, 2, 3, 3, 1, 1]

    for A in [A1, A2, A3, A4, A5, A6, A7]:
        print(A, find_len_longest_subarray(A))


test_find_len_longest_subarray()
