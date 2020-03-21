from test_framework import generic_test
import collections


def can_form_palindrome1(s: str) -> bool:
    counter = collections.Counter(s)
    odd = 0
    for v in counter.values():
        odd += v % 2
    return odd <= 1


def can_form_palindrome(s: str) -> bool:
    return sum([v % 2 for v in collections.Counter(s).values()]) < 2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
