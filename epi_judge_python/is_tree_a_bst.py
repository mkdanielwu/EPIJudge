from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math
from collections import namedtuple, deque


# fastest approach!!!
def is_binary_tree_bst1(tree: BinaryTreeNode) -> bool:

    def are_keys_in_range(tree: BinaryTreeNode,
                          low = -math.inf,
                          high = math.inf) -> bool:
        if tree is None:
            return True

        elif not low <= tree.data <= high:
            return False

        return are_keys_in_range(tree.left, low, tree.data) \
               and are_keys_in_range(tree.right, tree.data, high)

    return are_keys_in_range(tree)


# BFS approach: early stop if the violating node is near the root
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:

    QueueNode = namedtuple('QueueNode', ['node', 'lower', 'upper'])
    bst_queue = deque([QueueNode(tree, -math.inf, math.inf)])     # add root to queue

    while bst_queue:
        n = bst_queue.popleft()
        if n and n.node:
            if not n.lower <= n.node.data <= n.upper:
                return False

            bst_queue.extend([QueueNode(n.node.left, n.lower, n.node.data),
                             QueueNode(n.node.right, n.node.data, n.upper)])
    return True


# inorder traversal
def is_binary_tree_bst3(tree: BinaryTreeNode) -> bool:

    StackElement = namedtuple("StackElement", ['node', 'left_visited'])
    stack = [StackElement(node=tree, left_visited=False)]

    pre = None
    while stack:
        n = stack.pop()
        if n is not None and n.node is not None:
            if not n.left_visited:
                stack.append(StackElement(node=n.node, left_visited=True))
                if n.node.left is not None:
                    stack.append(StackElement(node=n.node.left, left_visited=False))
            elif pre is not None and n.node.data < pre:
                return False
            else:
                pre = n.node.data
                if n.node.right is not None:
                    stack.append(StackElement(node=n.node.right, left_visited=False))
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
