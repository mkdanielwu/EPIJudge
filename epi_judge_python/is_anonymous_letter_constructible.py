from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine1(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_counter = Counter(letter_text.replace(" ", "").lower())
    magazine_counter = Counter(magazine_text.replace(" ", "").lower())

    return len((letter_counter - magazine_counter).keys()) == 0


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_counter = Counter(letter_text.replace(" ", "").lower())
    magazine_counter = Counter(magazine_text.replace(" ", "").lower())

    return not letter_counter - magazine_counter


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
