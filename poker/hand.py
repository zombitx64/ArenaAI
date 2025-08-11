from collections import Counter
from itertools import combinations
from typing import List, Tuple

from .card import Card, RANKS

RANK_VALUE = {r: i for i, r in enumerate(RANKS, start=2)}

HandScore = Tuple[int, List[int]]


def _evaluate_five(cards: List[Card]) -> HandScore:
    ranks = sorted([RANK_VALUE[c.rank] for c in cards], reverse=True)
    counts = Counter(ranks)
    count_items = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    is_flush = len({c.suit for c in cards}) == 1
    is_straight = False
    if len(counts) == 5:
        high, low = max(ranks), min(ranks)
        if high - low == 4:
            is_straight = True
        elif set(ranks) == {14, 5, 4, 3, 2}:  # wheel straight
            is_straight = True
            ranks = [5, 4, 3, 2, 1]
    if is_straight and is_flush:
        return (8, ranks)
    if count_items[0][1] == 4:
        kicker = [c for c in ranks if c != count_items[0][0]][0]
        return (7, [count_items[0][0], kicker])
    if count_items[0][1] == 3 and count_items[1][1] == 2:
        return (6, [count_items[0][0], count_items[1][0]])
    if is_flush:
        return (5, ranks)
    if is_straight:
        return (4, ranks)
    if count_items[0][1] == 3:
        kickers = [x for x in ranks if x != count_items[0][0]]
        return (3, [count_items[0][0]] + kickers)
    if count_items[0][1] == 2 and count_items[1][1] == 2:
        pair_ranks = sorted([count_items[0][0], count_items[1][0]], reverse=True)
        kicker = [c for c in ranks if c not in pair_ranks][0]
        return (2, pair_ranks + [kicker])
    if count_items[0][1] == 2:
        pair_rank = count_items[0][0]
        kickers = [c for c in ranks if c != pair_rank]
        return (1, [pair_rank] + kickers)
    return (0, ranks)


def evaluate(cards: List[Card]) -> HandScore:
    """Return the best hand score for up to 7 cards."""
    best: HandScore = (-1, [])
    for combo in combinations(cards, 5):
        score = _evaluate_five(list(combo))
        if score > best:
            best = score
    return best
