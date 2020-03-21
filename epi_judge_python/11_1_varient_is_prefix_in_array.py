from typing import List


def is_prefix_in_sorted_array(A: List[str], p: str) -> bool:
    found = False

    if A is None or p is None:
        return False

    low, high = 0, len(A)-1

    while low <= high:
        mid = low + (high - low) // 2
        if A[mid].startswith(p):
            return True
        elif A[mid] > p:
            high = mid - 1
        else:
            low = mid + 1

    return found


def test_prefix_in_sorted_array():
    A1 = None
    A2 = []
    A3 = ['']
    A4 = [' ']
    A5 = ['', ' ', 'apple', 'banana', 'crane berry', 'donut']
    A6 = ['ape', 'app', 'apple', 'applicant', 'apply']

    assert not is_prefix_in_sorted_array(A1, None)
    assert not is_prefix_in_sorted_array(A2, '')
    assert is_prefix_in_sorted_array(A3, '')
    assert not is_prefix_in_sorted_array(A3, ' ')
    assert is_prefix_in_sorted_array(A4, '')
    assert is_prefix_in_sorted_array(A4, ' ')
    assert is_prefix_in_sorted_array(A5, '')
    assert is_prefix_in_sorted_array(A5, 'do')
    assert not is_prefix_in_sorted_array(A5, 'Do')
    assert is_prefix_in_sorted_array(A5, 'ban')
    assert is_prefix_in_sorted_array(A5, 'crane ')
    assert is_prefix_in_sorted_array(A5, 'crane')
    assert not is_prefix_in_sorted_array(A5, 'do ')
    assert not is_prefix_in_sorted_array(A6, 'app ')
    assert is_prefix_in_sorted_array(A6, 'ap')
    assert is_prefix_in_sorted_array(A6, 'app')


test_prefix_in_sorted_array()
