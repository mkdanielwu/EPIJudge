from typing import List, DefaultDict
import collections, functools, operator


def find_anagrams1(dictionary: List[str]) -> List[List[str]]:
    sorted_string_to_anagrams: DefaultDict[str, List[str]] = collections.defaultdict(list)

    for word in dictionary:
        sorted_string_to_anagrams[''.join(sorted(word))].append(word)   # O(nm log m)

    return [v for v in sorted_string_to_anagrams.values() if len(v) > 1]    # O(n)


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    sorted_string_to_anagrams: DefaultDict[int, List[str]] = collections.defaultdict(list)
    # prime numbers. any word is represented as product of prime numbers
    code_of_letters = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                       31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                       73, 79, 83, 89, 97, 101]
    for word in dictionary:
        sorted_string_to_anagrams[functools.reduce(operator.mul,
                                                   [code_of_letters[ord(l)-ord('a')] for l in word])].append(word)

    return [v for v in sorted_string_to_anagrams.values() if len(v) > 1]


def test_anagrams():
    D = ["debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money"]
    results = find_anagrams(D)
    for r in results:
        print(r)


test_anagrams()
