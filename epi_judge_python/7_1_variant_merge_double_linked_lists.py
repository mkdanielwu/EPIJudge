from typing import Optional, List


class DoubleLinkedListNode:

    def __init__(self, data=0, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next


def merge_double_linked_lists(list1: Optional[DoubleLinkedListNode],
                              list2: Optional[DoubleLinkedListNode]) -> Optional[DoubleLinkedListNode]:

    dummy_head = tail = DoubleLinkedListNode()
    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1.pre = tail
            list1 = list1.next
        else:
            tail.next = list2
            list2.pre = tail
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
        list1.pre = tail
    if list2:
        tail.next = list2
        list2.pre = tail

    return dummy_head.next


def make_double_linked_list(vals: List[int]) -> DoubleLinkedListNode:
    dummy_head = tail = DoubleLinkedListNode()
    if vals:
        for val in vals:
            tail.next = DoubleLinkedListNode(val, tail, None)
            tail = tail.next

    return dummy_head.next


def double_linked_list_to_str(n: DoubleLinkedListNode) -> str:
    s = ''
    while n:
        s = "{l}, {n}".format(l=s, n=n.data) if len(s) > 0 \
            else "{n}".format(n=n.data)
        n = n.next
    return s


def test_merge_double_linked_lists():
    list1 = make_double_linked_list(None)
    list2 = make_double_linked_list([])
    list3 = make_double_linked_list([0])
    list4 = make_double_linked_list([0, 0])
    list5 = make_double_linked_list([-1, 0, 1])
    list6 = make_double_linked_list([-11, -7, -5])

    print('l1:', double_linked_list_to_str(list1))
    print('l2:', double_linked_list_to_str(list2))
    print('l1 + l2:', double_linked_list_to_str(merge_double_linked_lists(list1, list2)))

    print('l1:', double_linked_list_to_str(list1))
    print('l3:', double_linked_list_to_str(list3))
    print('l1 + l3:', double_linked_list_to_str(merge_double_linked_lists(list1, list3)))

    print('l2:', double_linked_list_to_str(list2))
    print('l4:', double_linked_list_to_str(list4))
    print('l2 + l4:', double_linked_list_to_str(merge_double_linked_lists(list2, list4)))

    print('l3:', double_linked_list_to_str(list3))
    print('l4:', double_linked_list_to_str(list4))
    print('l3 + l4:', double_linked_list_to_str(merge_double_linked_lists(list3, list4)))

    print('l4:', double_linked_list_to_str(list4))
    print('l5:', double_linked_list_to_str(list5))
    print('l4 + l5:', double_linked_list_to_str(merge_double_linked_lists(list4, list5)))

    print('l5:', double_linked_list_to_str(list5))
    print('l6:', double_linked_list_to_str(list6))
    print('l5 + l6:', double_linked_list_to_str(merge_double_linked_lists(list5, list6)))


test_merge_double_linked_lists()
