from typing import List, Tuple

# this variant keeps relative ordering of False's
def dutch_natonal_flag_variant_bool_array_reorder(A: List[Tuple[bool, int]]) -> None:
    if A is not None:
        idx = 0
        for i in range(len(A)):
            if not A[i][0]:
                A[i], A[idx] = A[idx], A[i]
                idx += 1
    return

# this variant keeps relative ordering of True's
def dutch_natonal_flag_variant_bool_array_reorder_keep_true_order(A: List[Tuple[bool, int]]) -> None:
    if A is not None:
        idx = len(A) - 1
        for i in reversed(range(len(A))):
            if A[i][0]:
                A[i], A[idx] = A[idx], A[i]
                idx -= 1
    return


# test cases
A1 = [(True, 1), (False, 2), (True, 3), (False, 4), (True, 5), (False, 6)]
A2 = [(True, 1), (True, 2), (True, 3), (False, 4), (False, 5), (False, 6)]
A3 = [(False, 1), (False, 2), (False, 3), (True, 4), (True, 5), (True, 6)]
A4 = []
A5 = [(True, 1)]
A6 = [(False, 1)]

for A in [A1, A2, A3, A4, A5, A6]:
    print("before: ", A)
    dutch_natonal_flag_variant_bool_array_reorder(A)
    # dutch_natonal_flag_variant_bool_array_reorder_keep_true_order(A)
    print("after: ", A)
