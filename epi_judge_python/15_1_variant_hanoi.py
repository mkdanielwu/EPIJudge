import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple


NUM_PEGS = 3


# variant: each move must involve aux_peg (P2)
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


# variant: each move must be F->T (P0->P1), T->A (P1->P2), A->F (P2->P1)
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


# variant: no move F->T (P0->P1), but T->F (P1->P0) is ok
def compute_tower_hanoi3(num_rings: int) -> List[List[int]]:

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


# variant: relaxed size constraint - the largest ring on a peg must be the lowest
# ring on the peg. The remaining rings on the peg can be in any order, e.g., it is fine
# to have the second-largest ring above the third-largest ring.
def compute_tower_hanoi4(num_rings: int) -> List[List[int]]:

    def compute_tower_hanoi_relaxed(num_rings: int,  from_peg: int, to_peg: int,
                                    aux_peg: int) -> List[List[int]]:
        if 0 < num_rings < 3:
            # move as regular Hanoi solution
            compute_tower_hanoi_relaxed(num_rings - 1, from_peg, aux_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_relaxed(num_rings - 1, aux_peg, to_peg, from_peg)
        elif num_rings >= 3:
            # move top smaller n-2 rings F -> T
            compute_tower_hanoi_relaxed(num_rings - 2, from_peg, to_peg, aux_peg)
            # move the n-1th ring F -> A
            pegs[aux_peg].append(pegs[from_peg].pop())
            result.append([from_peg, aux_peg])
            # move top smaller n-2 rings T -> A in reversed order above the n-1th ring
            for i in range(num_rings - 2):
                pegs[aux_peg].append(pegs[to_peg].pop())
                result.append([to_peg, aux_peg])
            # move the nth ring F -> T
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            # move top smaller n-2 rings A -> F in order
            for i in range(num_rings - 2):
                pegs[from_peg].append(pegs[aux_peg].pop())
                result.append([aux_peg, from_peg])
            # move the n-1th ringt A -> T
            pegs[to_peg].append(pegs[aux_peg].pop())
            result.append([aux_peg, to_peg])
            # move top smaller n-2 rings F -> T
            compute_tower_hanoi_relaxed(num_rings - 2, from_peg, to_peg, aux_peg)

    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    result: List[List[int]] = []
    compute_tower_hanoi_relaxed(num_rings, 0, 1, 2)
    print("compute_tower_hanoi_relaxed: {rings}: {ops}".format(rings=num_rings, ops=len(result)))
    return result


# variant: 2n disks of n different sizes, 2 of each size.
def compute_tower_hanoi5(n: int) -> List[List[int]]:

    def compute_tower_hanoi_2_each_size(num_rings: int, from_peg: int, to_peg: int,
                                        aux_peg: int) -> List[List[int]]:
        if num_rings >= 2 and num_rings % 2 == 0:
            # move as regular Hanoi solution
            compute_tower_hanoi_2_each_size(num_rings - 2, from_peg, aux_peg, to_peg)
            for i in range(2):
                pegs[to_peg].append(pegs[from_peg].pop())
                result.append([from_peg, to_peg])
            compute_tower_hanoi_2_each_size(num_rings - 2, aux_peg, to_peg, from_peg)

    pegs = [[i//2 + 1 for i in reversed(range(n))]] + [[] for _ in range(1, NUM_PEGS)]
    print(pegs)
    result: List[List[int]] = []
    compute_tower_hanoi_2_each_size(n, 0, 1, 2)
    print("compute_tower_hanoi_2_each_size: {rings}: {ops}".format(rings=n, ops=len(result)))
    return result


ColorDisk = namedtuple("ColorDisk", ["color", "size"])


# variant: 2n disks of 2n different sizes; top n disks are black, bottom n disks are white.
# a white disk cannot be placed directly on top of a black disk.
# TODO: incomplete! stuck!
def compute_tower_hanoi(n: int) -> List[List[int]]:

    def compute_tower_hanoi_n_black(num_rings: int, from_peg: int, to_peg: int,
                                    aux_peg: int) -> List[List[int]]:
        if num_rings > 0:
            compute_tower_hanoi_n_black(num_rings-1, from_peg, aux_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_n_black(num_rings-1, aux_peg, to_peg, from_peg)

    def compute_tower_hanoi_n_white(num_rings: int, blck_rings: int, from_peg: int, to_peg: int,
                                    aux_peg: int) -> List[List[int]]:
        if num_rings > 0:
            compute_tower_hanoi_n_white(num_rings-1, from_peg, aux_peg, to_peg)
            compute_tower_hanoi_n_black(blck_rings, from_peg, aux_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_n_white(num_rings-1, aux_peg, to_peg, from_peg)


    def compute_tower_hanoi_2n_black_white(num_rings: int, from_peg: int, to_peg: int,
                                           aux_peg: int) -> List[List[int]]:
        if num_rings >= 2 and num_rings % 2 == 0:
            n = num_rings // 2      # number of black disks; number of white disks
            compute_tower_hanoi_n_black(n, from_peg, aux_peg, to_peg)


    pegs = [[ColorDisk(color="B" if i < n else "W", size=i+1) for i in reversed(range(n))]] + \
           [[] for _ in range(1, NUM_PEGS)]
    print(pegs)
    result: List[List[int]] = []
    compute_tower_hanoi_2n_black_white(n, 0, 1, 2)
    print("compute_tower_hanoi_2n_black_white: {rings}: {ops}".format(rings=n, ops=len(result)))
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


@enable_executor_hook
def compute_tower_hanoi_wrapper2n(executor, num_rings):
    # the following 2 lines are needed to test 2n disc cases
    pegs = [[i // 2 + 1 for i in reversed(range(2 * num_rings))]] + [[] for _ in range(1, NUM_PEGS)]
    result = executor.run(functools.partial(compute_tower_hanoi, 2 * num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] > pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], [i // 2 + 1 for i in reversed(range(2 * num_rings))]]
    expected_pegs2 = [[], [i // 2 + 1 for i in reversed(range(2 * num_rings))], []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


@enable_executor_hook
def compute_tower_hanoi_wrapper2n_blackwhite(executor, num_rings):
    # the following 2 lines are needed to test 2n disc cases
    pegs = [[ColorDisk(color="B" if i < num_rings else "W", size=i+1) for i in reversed(range(2*num_rings))]] + \
           [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, 2 * num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and (pegs[from_peg][-1].size >= pegs[to_peg][-1].size
                             or pegs[from_peg][-1].color=="W" and pegs[to_peg][-1].color=="B"):
            raise TestFailure('Illegal move from {}({}) to {}({})'.format(
                pegs[from_peg][-1].size, pegs[from_peg][-1].color,
                pegs[to_peg][-1].size, pegs[to_peg][-1].color))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], [ColorDisk(color="B" if i < num_rings else "W", size=i+1) for i in reversed(range(2*num_rings))]]
    expected_pegs2 = [[], [ColorDisk(color="B" if i < num_rings else "W", size=i+1) for i in reversed(range(2*num_rings))], []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        # generic_test.generic_test_main('15_1_variant_hanoi.py', 'hanoi.tsv',
        #                                compute_tower_hanoi_wrapper))
        # generic_test.generic_test_main('15_1_variant_hanoi.py', 'hanoi.tsv',
        #                                compute_tower_hanoi_wrapper2n))
        generic_test.generic_test_main('15_1_variant_hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper2n_blackwhite))
