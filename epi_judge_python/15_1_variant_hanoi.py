import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


NUM_PEGS = 3


def compute_tower_hanoi1(num_rings: int) -> List[List[int]]:

    def compute_tower_hanoi_must_use_aux_peg(num_rings: int, from_peg: int,
                                             to_peg: int, aux_peg: int) -> List[List[int]]:
        if num_rings > 0:
            compute_tower_hanoi_must_use_aux_peg(num_rings - 1, from_peg, aux_peg, to_peg)
            compute_tower_hanoi_must_use_aux_peg(num_rings - 1, aux_peg, to_peg, from_peg)
            pegs[aux_peg].append(pegs[from_peg].pop())
            result.append([from_peg, aux_peg])
            compute_tower_hanoi_must_use_aux_peg(num_rings - 1, to_peg, aux_peg, from_peg)
            compute_tower_hanoi_must_use_aux_peg(num_rings - 1, aux_peg, from_peg, to_peg)
            pegs[to_peg].append(pegs[aux_peg].pop())
            result.append([aux_peg, to_peg])
            compute_tower_hanoi_must_use_aux_peg(num_rings - 1, from_peg, aux_peg, to_peg)
            compute_tower_hanoi_must_use_aux_peg(num_rings - 1, aux_peg, to_peg, from_peg)

    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    result: List[List[int]] = []
    compute_tower_hanoi_must_use_aux_peg(num_rings, 0, 1, 2)
    print("compute_tower_hanoi_must_use_aux_peg: {rings}: {ops}".format(rings=num_rings, ops=len(result)))
    return result


def compute_tower_hanoi2(num_rings: int) -> List[List[int]]:

    def compute_tower_hanoi_must_use_pegs_in_order(num_rings: int,
                                                   from_peg: int,
                                                   to_peg: int, aux_peg: int) -> List[List[int]]:
        if num_rings > 0:
            compute_tower_hanoi_must_use_pegs_in_order(num_rings - 1, from_peg, to_peg, aux_peg)
            compute_tower_hanoi_must_use_pegs_in_order(num_rings - 1, to_peg, aux_peg, from_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_must_use_pegs_in_order(num_rings - 1, aux_peg, from_peg, to_peg)
            compute_tower_hanoi_must_use_pegs_in_order(num_rings - 1, from_peg, to_peg, aux_peg)

    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    result: List[List[int]] = []
    compute_tower_hanoi_must_use_pegs_in_order(num_rings, 0, 1, 2)
    print("compute_tower_hanoi_must_use_pegs_in_order: {rings}: {ops}".format(rings=num_rings, ops=len(result)))
    return result


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:

    def compute_tower_hanoi_must_no_from_to_pegs(num_rings: int,
                                                 from_peg: int,
                                                 to_peg: int, aux_peg: int) -> List[List[int]]:
        if num_rings > 0:
            compute_tower_hanoi_must_no_from_to_pegs(num_rings - 1, from_peg, aux_peg, to_peg)
            compute_tower_hanoi_must_no_from_to_pegs(num_rings - 1, aux_peg, to_peg, from_peg)
            pegs[aux_peg].append(pegs[from_peg].pop())
            result.append([from_peg, aux_peg])
            compute_tower_hanoi_must_no_from_to_pegs(num_rings - 1, to_peg, from_peg, aux_peg)
            pegs[to_peg].append(pegs[aux_peg].pop())
            result.append([aux_peg, to_peg])
            compute_tower_hanoi_must_no_from_to_pegs(num_rings - 1, from_peg, aux_peg, to_peg)
            compute_tower_hanoi_must_no_from_to_pegs(num_rings - 1, aux_peg, to_peg, from_peg)

    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    result: List[List[int]] = []
    compute_tower_hanoi_must_no_from_to_pegs(num_rings, 0, 1, 2)
    print("compute_tower_hanoi_must_no_from_to_pegs: {rings}: {ops}".format(rings=num_rings, ops=len(result)))
    return result


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
