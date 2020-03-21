from typing import List, DefaultDict

from test_framework import generic_test, test_utils
import collections, functools, operator


def find_anagrams1(dictionary: List[str]) -> List[List[str]]:
    sorted_string_to_anagrams: DefaultDict[str, List[str]] = collections.defaultdict(list)

    for word in dictionary:
        sorted_string_to_anagrams[''.join(sorted(word))].append(word)   # O(nm log m)

    return [v for v in sorted_string_to_anagrams.values() if len(v) > 1]    # O(n)


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    sorted_string_to_anagrams: DefaultDict[int, List[str]] = collections.defaultdict(list)
    code_of_letters = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                       31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                       73, 79, 83, 89, 97, 101]
    for word in dictionary:
        # functools.reduce(operator.mul, [code_of_letters[l] for l in word])
        sorted_string_to_anagrams[functools.reduce(operator.mul, [code_of_letters[l] for l in word])].append(word)

    return [v for v in sorted_string_to_anagrams.values() if len(v) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
