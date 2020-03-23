import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple


NUM_PEGS = 3


# recursive
def compute_tower_hanoi1(num_rings: int) -> List[List[int]]:

    def move_rings(rings: int, src: int, dst: int, spare: int) -> List[List[int]]:
        steps = []
        if rings == 1:
            return [(src, dst)]
        else:
            steps.extend(move_rings(rings-1, src, spare, dst))
            steps.append((src, dst))
            steps.extend(move_rings(rings-1, spare, dst, src))
        return steps

    return move_rings(num_rings, 0, 1, 2)


# 15.1 variant iterative
def compute_tower_hanoi(num_rings: int) -> List[List[int]]:

    StackElement = namedtuple("StackElement", ["count", "src", "dst", "temp"])

    stack = [StackElement(count=num_rings, src=0, dst=1, temp=2)]
    steps = []
    while stack:
        element = stack.pop()
        if element.count == 1:
            steps.append((element.src, element.dst))
        else:
            stack.append(StackElement(element.count - 1, element.temp, element.dst, element.src))
            stack.append(StackElement(1, element.src, element.dst, element.temp))
            stack.append(StackElement(element.count - 1, element.src, element.temp, element.dst))
    return steps


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
