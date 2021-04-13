from typing import List


def latest(scores: List) -> int:
    return scores[-1]


def personal_best(scores: List) -> int:
    return sorted(scores)[-1]


def personal_top_three(scores: List) -> List:
    scores = sorted(scores)[::-1]
    return scores[0:3]
