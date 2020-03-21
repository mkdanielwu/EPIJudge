from test_framework import generic_test
from test_framework.test_failure import TestFailure
from typing import List
import collections, math


class Stack1:

    def __init__(self):
        self.stack = list()

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self) -> int:
        m = self.stack[0] if not self.empty() else 0
        for s in self.stack:
            m = max(s, m)
        return m

    def pop(self) -> int:
        return self.stack.pop()

    def push(self, x: int) -> None:
        self.stack.append(x)
        return


class Stack:

    StackElement = collections.namedtuple('StackElement', ['val', 'max'])

    def __init__(self):
        self.stack: List[Stack.StackElement] = []

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self) -> int:
        return -math.inf if self.empty() else self.stack[-1].max

    def pop(self) -> int:
        return self.stack.pop().val

    def push(self, x: int) -> None:
        self.stack.append(Stack.StackElement(val=x, max=max(x, self.max())))
        return


class StackVariant:

    MaxElement = collections.namedtuple('MaxElement', ['idx', 'max'])

    def __init__(self):
        self.max_loc: List[StackVariant.MaxElement] = []
        self.stack: List[int] = []

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self) -> int:
        return -math.inf if self.empty() else self.max_loc[-1].max

    def pop(self) -> int:
        if len(self.stack) - 1 <= self.max_loc[-1].idx:
            self.max_loc.pop()
        return self.stack.pop()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x > self.max():
            self.max_loc.append(StackVariant.MaxElement(idx=len(self.stack)-1, max=x))
        return


def stack_tester(ops):
    try:
        # s = Stack()
        s = StackVariant()
        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
