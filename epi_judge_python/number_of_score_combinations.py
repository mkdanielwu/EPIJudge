from typing import List

from test_framework import generic_test


# original: space complexity: O(sn)
def num_combinations_for_final_score1(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    score_combo = [[1] + [0]*final_score for _ in individual_play_scores]
    for i, r in enumerate(individual_play_scores):
        for c in range(1, final_score+1):
            without_this_play = score_combo[i-1][c] if i > 0 else 0
            with_this_play = score_combo[i][c - r] if c >= r else 0
            score_combo[i][c] = without_this_play + with_this_play
    return score_combo[-1][-1]


# variant 1: space complexity: O(s)
def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    score_combo = [1] + [0]*final_score
    for i, r in enumerate(individual_play_scores):
        for c in range(1, final_score+1):
            without_this_play = score_combo[c] if i > 0 else 0
            with_this_play = score_combo[c - r] if c >= r else 0
            score_combo[c] = without_this_play + with_this_play
    return score_combo[-1]


# variant 2: return number of sequences (permutations)
def num_sequences_for_final_score(final_score: int,
                                  individual_play_scores: List[int]) -> int:
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
