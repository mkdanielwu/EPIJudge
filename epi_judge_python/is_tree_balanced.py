from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections


def get_binary_tree_height(tree: BinaryTreeNode) -> int:
    if tree is None:
        return -1

    return max(get_binary_tree_height(tree.left), get_binary_tree_height(tree.right)) + 1


def is_balanced_binary_tree1(tree: BinaryTreeNode) -> bool:

    if tree is None:
        return True

    if not is_balanced_binary_tree(tree.left):
        return False

    if not is_balanced_binary_tree(tree.right):
        return False

    h_left, h_right = get_binary_tree_height(tree.left), get_binary_tree_height(tree.right)

    return abs(h_left - h_right) < 2


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    BalanceWithHeight = collections.namedtuple('BalanceWithHeight', ['balance', 'height'])

    def check_balance(tree: BinaryTreeNode) -> BalanceWithHeight:
        if tree is None:
            return BalanceWithHeight(balance=True, height=-1)

        left_result = check_balance(tree.left)
        if not left_result.balance:
            return left_result

        right_result = check_balance(tree.right)
        if not right_result.balance:
            return right_result

        return BalanceWithHeight(balance=abs(left_result.height - right_result.height) < 2,
                                 height=max(left_result.height, right_result.height)+1)

    return check_balance(tree).balance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
