from list_node import ListNode
from test_framework import generic_test


def search_list1(L: ListNode, key: int) -> ListNode:
    result = None
    node = L
    while node is not None:
        if node.data == key:
            result = node
            break
        node = node.next

    return result


def search_list(L: ListNode, key: int) -> ListNode:

    while L is not None and L.data != key:
        L = L.next

    return L


def search_list_wrapper(L, key):
    result = search_list(L, key)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_in_list.py',
                                       'search_in_list.tsv',
                                       search_list_wrapper))
