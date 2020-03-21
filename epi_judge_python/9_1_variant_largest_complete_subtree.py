from binary_tree_node import BinaryTreeNode
import collections

def largest_complete_subtree_size(tree: BinaryTreeNode) -> int:

    TreeCompleteness = collections.namedtuple('TreeCompleteness', ['complete', 'size'])

    def check_complete_subtree(tree: BinaryTreeNode) -> TreeCompleteness:

        if not tree:
            return TreeCompleteness(complete=True, size=0)

        left_complete = check_complete_subtree(tree.left)
        right_complete = check_complete_subtree(tree.right)

        complete = left_complete.complete and right_complete.complete

        if left_complete.size > 1 and not tree.right:
            complete = False

        if